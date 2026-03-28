# -*- coding: utf-8 -*-
# PDFSvgTextRenderer.py — Pixel-perfect text via pdftocairo SVG glyphs
# BlueCollar Systems — BUILT. NOT BOUGHT.
#
# Renders text as vector glyph outlines using pdftocairo.
# Each unique glyph is built once as a Part.Shape, then translated
# and compounded into a single Part::Feature for all text on the page.
#
# Falls back gracefully if pdftocairo is not available.

from __future__ import annotations

import os
import re
import shutil
import subprocess
import sys
import tempfile
from typing import Dict, List, Optional

try:
    import FreeCAD
    from FreeCAD import Vector
    import Part
except ImportError:
    FreeCAD = Part = None
    Vector = None

PDF_PT_TO_MM = 25.4 / 72.0


def find_pdftocairo() -> Optional[str]:
    """Find pdftocairo executable on the system.

    Resolution order:
      1. BC_PDFTOCAIRO_PATH environment variable (manual override)
      2. Plugin bundled bin/ directory — place pdftocairo here to make
         the plugin self-contained without any system install:
           <FreeCAD Mod>/PDFVectorImporter/src/lib/bin/pdftocairo[.exe]
      3. System PATH (shutil.which — cross-platform)
      4. Common Windows locations (MiKTeX, Poppler installs)
    """
    # 1) Explicit override
    env = os.environ.get("BC_PDFTOCAIRO_PATH", "")
    if env and os.path.isfile(env):
        return env

    # 2) Bundled bin/ inside the plugin — highest-priority so a bundled
    #    copy always wins over any system version.
    _this_dir = os.path.dirname(os.path.abspath(__file__))
    _lib_bin = os.path.join(_this_dir, "lib", "bin")
    for _name in ("pdftocairo.exe", "pdftocairo"):
        _candidate = os.path.join(_lib_bin, _name)
        if os.path.isfile(_candidate):
            return _candidate

    # 3) System PATH
    found = shutil.which("pdftocairo")
    if found:
        return found

    # 4) Common Windows locations
    if sys.platform == "win32":
        for pattern_base in [
            os.path.join(os.environ.get("LOCALAPPDATA", ""),
                         "Programs", "MiKTeX", "miktex", "bin", "x64"),
            r"C:\Program Files\MiKTeX\miktex\bin\x64",
            r"C:\poppler\bin",
            r"C:\tools\poppler\bin",
        ]:
            candidate = os.path.join(pattern_base, "pdftocairo.exe")
            if os.path.isfile(candidate):
                return candidate

    return None


def render_text(pdf_path: str, page_num: int, page_h: float,
                scale: float, fc_doc=None, parent_group=None,
                flip_y: bool = True) -> Optional[dict]:
    """Render text from a PDF page as vector glyph geometry.

    Returns {"shapes": int, "glyphs": int} or None if unavailable.
    """
    exe = find_pdftocairo()
    if exe is None:
        if FreeCAD:
            FreeCAD.Console.PrintMessage(
                "PDFSvgTextRenderer: pdftocairo not found — "
                "text-as-geometry skipped. Place pdftocairo(.exe) in "
                "src/lib/bin/ or install Poppler to enable this feature.\n"
            )
        return None

    doc = fc_doc or FreeCAD.ActiveDocument
    if doc is None:
        return None

    # Generate SVG — always clean up temp file regardless of outcome
    fd, svg_path = tempfile.mkstemp(suffix=".svg", prefix=f"bc_fc_svg_{page_num}_")
    os.close(fd)  # close fd so subprocess can write to the path
    svg = None

    try:
        kw = {}
        if sys.platform == "win32":
            kw["creationflags"] = 0x08000000  # CREATE_NO_WINDOW
        subprocess.run(
            [exe, "-svg", "-f", str(page_num), "-l", str(page_num),
             pdf_path, svg_path],
            check=True, timeout=90, capture_output=True, **kw)

        if not os.path.isfile(svg_path):
            return None

        with open(svg_path, "r", encoding="utf-8") as f:
            svg = f.read()

    except subprocess.TimeoutExpired:
        if FreeCAD:
            FreeCAD.Console.PrintWarning(
                f"PDFSvgTextRenderer: pdftocairo timed out on page {page_num} — "
                "text-as-geometry skipped.\n"
            )
        return None
    except (subprocess.SubprocessError, OSError, ValueError, UnicodeError) as e:
        if FreeCAD:
            FreeCAD.Console.PrintWarning(
                f"PDFSvgTextRenderer: pdftocairo failed on page {page_num}: {e}\n"
            )
        return None
    finally:
        try:
            os.remove(svg_path)
        except OSError:
            pass

    if not svg:
        return None

    # Parse SVG dimensions
    m = re.search(r'height="([^"]+)"', svg)
    svg_h = float(m.group(1)) if m else page_h

    # Parse glyph definitions
    glyph_defs = {}
    for gid, path_d in re.findall(
            r'<g id="(glyph-\d+-\d+)">\s*<path d="([^"]*)"', svg, re.DOTALL):
        if path_d.strip():
            glyph_defs[gid] = path_d

    # Parse use placements
    placements = []
    for gid, x, y in re.findall(
            r'<use xlink:href="#(glyph-\d+-\d+)" x="([^"]+)" y="([^"]+)"', svg):
        placements.append((gid, float(x), float(y)))

    if not placements:
        return {"shapes": 0, "glyphs": 0}

    # Build Part.Shape for each unique glyph
    glyph_shapes: Dict[str, Part.Shape] = {}
    for gid, path_d in glyph_defs.items():
        edges = _svg_path_to_edges(path_d, scale)
        if edges:
            try:
                compound = Part.makeCompound(edges)
                glyph_shapes[gid] = compound
            except (RuntimeError, ValueError, TypeError):
                pass

    # Place all glyphs
    all_shapes = []
    glyph_count = 0

    for gid, use_x, use_y in placements:
        shape = glyph_shapes.get(gid)
        if shape is None:
            continue

        # SVG coords → FreeCAD coords
        # Glyph use positions are in viewBox coords (PDF points)
        fc_x = use_x * scale
        if flip_y:
            fc_y = (svg_h - use_y) * scale
        else:
            fc_y = use_y * scale

        try:
            placed = shape.translated(Vector(fc_x, fc_y, 0.0))
            all_shapes.append(placed)
            glyph_count += 1
        except (AttributeError, RuntimeError, TypeError):
            pass

    if not all_shapes:
        return {"shapes": 0, "glyphs": 0}

    # Combine all text into one compound object
    try:
        text_compound = Part.makeCompound(all_shapes)
        text_obj = doc.addObject("Part::Feature", "Text_Glyphs")
        text_obj.Shape = text_compound
        try:
            text_obj.ViewObject.LineWidth = 1.0
            text_obj.ViewObject.LineColor = (0.0, 0.0, 0.0)
        except (AttributeError, RuntimeError, TypeError):
            pass
        if parent_group:
            parent_group.addObject(text_obj)
        return {"shapes": len(glyph_shapes), "glyphs": glyph_count}
    except (RuntimeError, ValueError, TypeError):
        return None


def _svg_path_to_edges(d: str, scale: float) -> List:
    """Parse SVG path d="" into Part edges.

    Glyph coordinates are in PDF points, Y-down.
    We flip Y and scale to mm for FreeCAD.
    """
    tokens = re.findall(r'[MLHVCSZmlhvcsz]|[-+]?\d*\.?\d+(?:[eE][-+]?\d+)?', d)
    edges = []
    subpath_pts = []
    start_pt = None
    cx, cy = 0.0, 0.0
    cmd = None
    nums: List[float] = []
    prev_cubic_cp2: Optional[List[float]] = None  # second control point of previous cubic (in abs coords)

    def mk(gx: float, gy: float) -> Vector:
        return Vector(gx * scale, -gy * scale, 0.0)

    def flush_subpath():
        nonlocal subpath_pts
        if len(subpath_pts) >= 2:
            for i in range(len(subpath_pts) - 1):
                p1, p2 = subpath_pts[i], subpath_pts[i + 1]
                if p1.distanceToPoint(p2) > 1e-4:
                    try:
                        edges.append(Part.LineSegment(p1, p2).toShape())
                    except (RuntimeError, ValueError, TypeError):
                        pass
        subpath_pts = []

    def run():
        nonlocal cx, cy, start_pt, subpath_pts, is_relative, prev_cubic_cp2

        if cmd == "M":
            prev_cubic_cp2 = None
            while len(nums) >= 2:
                flush_subpath()
                nx, ny = nums.pop(0), nums.pop(0)
                if is_relative:
                    cx, cy = cx + nx, cy + ny
                else:
                    cx, cy = nx, ny
                start_pt = mk(cx, cy)
                subpath_pts = [start_pt]
                # After first M pair, implicit coords are treated as L
                is_relative = is_relative  # keep relative state for implicit L
        elif cmd == "L":
            prev_cubic_cp2 = None
            while len(nums) >= 2:
                nx, ny = nums.pop(0), nums.pop(0)
                if is_relative:
                    cx, cy = cx + nx, cy + ny
                else:
                    cx, cy = nx, ny
                subpath_pts.append(mk(cx, cy))
        elif cmd == "H":
            prev_cubic_cp2 = None
            while nums:
                nx = nums.pop(0)
                if is_relative:
                    cx = cx + nx
                else:
                    cx = nx
                subpath_pts.append(mk(cx, cy))
        elif cmd == "V":
            prev_cubic_cp2 = None
            while nums:
                ny = nums.pop(0)
                if is_relative:
                    cy = cy + ny
                else:
                    cy = ny
                subpath_pts.append(mk(cx, cy))
        elif cmd == "C":
            while len(nums) >= 6:
                rx1, ry1, rx2, ry2, rx, ry = [nums.pop(0) for _ in range(6)]
                if is_relative:
                    x1, y1 = cx + rx1, cy + ry1
                    x2, y2 = cx + rx2, cy + ry2
                    x, y = cx + rx, cy + ry
                else:
                    x1, y1 = rx1, ry1
                    x2, y2 = rx2, ry2
                    x, y = rx, ry
                p0 = subpath_pts[-1] if subpath_pts else mk(cx, cy)
                p1 = mk(x1, y1)
                p2 = mk(x2, y2)
                p3 = mk(x, y)
                chord = p0.distanceToPoint(p3)
                n = 6 if chord < 0.5 else (8 if chord < 2.0 else 12)
                for i in range(1, n + 1):
                    t = i / n
                    mt = 1.0 - t
                    bx = mt**3*p0.x + 3*mt**2*t*p1.x + 3*mt*t**2*p2.x + t**3*p3.x
                    by = mt**3*p0.y + 3*mt**2*t*p1.y + 3*mt*t**2*p2.y + t**3*p3.y
                    pt = Vector(bx, by, 0.0)
                    subpath_pts.append(pt)
                prev_cubic_cp2 = [x2, y2]
                cx, cy = x, y
        elif cmd == "S":
            while len(nums) >= 4:
                rx2, ry2, rx, ry = nums.pop(0), nums.pop(0), nums.pop(0), nums.pop(0)
                if is_relative:
                    x2, y2 = cx + rx2, cy + ry2
                    x, y = cx + rx, cy + ry
                else:
                    x2, y2 = rx2, ry2
                    x, y = rx, ry
                # Reflect the second control point of the previous cubic
                if prev_cubic_cp2 is not None:
                    x1 = 2 * cx - prev_cubic_cp2[0]
                    y1 = 2 * cy - prev_cubic_cp2[1]
                else:
                    x1, y1 = cx, cy
                p0 = subpath_pts[-1] if subpath_pts else mk(cx, cy)
                p1 = mk(x1, y1)
                p2 = mk(x2, y2)
                p3 = mk(x, y)
                chord = p0.distanceToPoint(p3)
                n = 6 if chord < 0.5 else (8 if chord < 2.0 else 12)
                for i in range(1, n + 1):
                    t = i / n
                    mt = 1.0 - t
                    bx = mt**3*p0.x + 3*mt**2*t*p1.x + 3*mt*t**2*p2.x + t**3*p3.x
                    by = mt**3*p0.y + 3*mt**2*t*p1.y + 3*mt*t**2*p2.y + t**3*p3.y
                    pt = Vector(bx, by, 0.0)
                    subpath_pts.append(pt)
                prev_cubic_cp2 = [x2, y2]
                cx, cy = x, y
        elif cmd == "Z":
            prev_cubic_cp2 = None
            if subpath_pts and start_pt:
                if subpath_pts[-1].distanceToPoint(start_pt) > 1e-4:
                    subpath_pts.append(start_pt)
            flush_subpath()
            if start_pt:
                subpath_pts = [start_pt]

    is_relative = False
    for tok in tokens:
        if re.match(r'^[A-Za-z]$', tok):
            if cmd is not None:
                run()
            is_relative = tok.islower()
            cmd = tok.upper()
            nums = []
        else:
            nums.append(float(tok))
    if cmd is not None:
        run()
    flush_subpath()

    return edges
