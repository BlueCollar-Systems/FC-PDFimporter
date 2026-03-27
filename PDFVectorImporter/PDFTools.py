# -*- coding: utf-8 -*-
# PDFTools.py — utility commands: Check Env, Batch Import, Install PyMuPDF
# BlueCollar Systems — BUILT. NOT BOUGHT.
from __future__ import annotations

import os
import sys
import traceback

try:
    import FreeCAD
    import FreeCADGui
except ImportError:
    FreeCAD = FreeCADGui = None

try:
    from PySide6 import QtWidgets, QtCore
except ImportError:
    try:
        from PySide2 import QtWidgets, QtCore
    except ImportError:
        QtWidgets = QtCore = None


def _msg(s):
    if FreeCAD:
        FreeCAD.Console.PrintMessage(s + "\n")
    else:
        print(s)

def _warn(s):
    if FreeCAD:
        FreeCAD.Console.PrintWarning(s + "\n")
    else:
        print("WARN:", s)

def _err(s):
    if FreeCAD:
        FreeCAD.Console.PrintError(s + "\n")
    else:
        print("ERR:", s)


def _find_python() -> str:
    """Find the real python.exe — sys.executable may point to freecad.exe."""
    exe = sys.executable
    bindir = os.path.dirname(exe)
    # FreeCAD 1.0+ (conda-based) puts python.exe alongside freecad.exe
    for name in ("python.exe", "python3.exe", "python"):
        candidate = os.path.join(bindir, name)
        if os.path.isfile(candidate):
            return candidate
    # Check parent directories
    for name in ("python.exe", "python3.exe", "python"):
        candidate = os.path.join(os.path.dirname(bindir), name)
        if os.path.isfile(candidate):
            return candidate
    # Last resort
    return exe


def _wb_base() -> str:
    """Return workbench root directory."""
    for root in (FreeCAD.getUserAppDataDir(), FreeCAD.getResourceDir()):
        candidate = os.path.join(root, "Mod", "PDFVectorImporter")
        if os.path.isdir(candidate):
            return candidate
    return ""


# ──────────────────────────────────────────────────────────────────────
class CheckEnvironmentCommand:
    def GetResources(self):
        return {
            "Pixmap": "",
            "MenuText": "Check Environment",
            "ToolTip": "Print Python paths, library versions, and FreeCAD module status.",
        }

    def IsActive(self):
        return True

    def Activated(self):
        _msg("\n════════════════════════════════════════════════════")
        _msg("  PDF Vector Importer — Environment Check")
        _msg("════════════════════════════════════════════════════")

        _msg(f"  Workbench dir: {_wb_base()}")

        # Python
        _msg(f"  sys.executable: {sys.executable}")
        _msg(f"  Real python:    {_find_python()}")

        # PyMuPDF
        try:
            import fitz
            ver = getattr(fitz, "version", ("?", "?", "?"))
            _msg(f"  PyMuPDF:  version={ver}  file={getattr(fitz, '__file__', '?')}")
        except (ImportError, AttributeError, OSError, RuntimeError) as e:
            _err(f"  PyMuPDF:  IMPORT FAILED — {e}")

        # Workbench package
        try:
            import PDFVectorImporter
            base = os.path.dirname(getattr(PDFVectorImporter, "__file__", "") or "")
            _msg(f"  Workbench package: {base or '(unknown path)'}")
        except (ImportError, AttributeError, OSError, RuntimeError) as e:
            _err(f"  Workbench package: NOT FOUND — {e}")

        # Core modules
        for mod in ("Draft", "Part"):
            try:
                __import__(mod)
                _msg(f"  {mod}: OK")
            except (ImportError, ModuleNotFoundError) as e:
                _warn(f"  {mod}: MISSING — {e}")

        # Image WB
        try:
            import ImageGui  # noqa: F401
            _msg("  Image Workbench: available")
        except ImportError:
            _warn("  Image Workbench: NOT available (embedded image import disabled)")

        # PySide version
        try:
            from PySide6 import __version__ as pv
            _msg(f"  PySide6: {pv}")
        except ImportError:
            try:
                from PySide2 import __version__ as pv
                _msg(f"  PySide2: {pv}")
            except ImportError:
                _warn("  PySide: NOT FOUND")

        _msg(f"  sys.path ({len(sys.path)} entries):")
        for p in sys.path:
            _msg(f"    {p}")
        _msg("════════════════════════════════════════════════════\n")


# ──────────────────────────────────────────────────────────────────────
class ImportViaConsoleCommand:
    """Pick a file and pages, import via console (no full dialog)."""

    def GetResources(self):
        return {
            "Pixmap": "",
            "MenuText": "Import via Console…",
            "ToolTip": "Quick file + page picker, runs import with default settings.",
        }

    def IsActive(self):
        return QtWidgets is not None

    def Activated(self):
        pdf, _ = QtWidgets.QFileDialog.getOpenFileName(
            None, "Select PDF", "", "PDF Files (*.pdf)")
        if not pdf:
            return
        pages_str, ok = QtWidgets.QInputDialog.getText(
            None, "Pages", "Pages (e.g. 1  or  1,3-5  or  all):", text="1")
        if not ok:
            return
        try:
            import PDFVectorImporter.src.PDFImporterCore as core
            pages = _parse_page_spec(pages_str, pdf)
            opts = core.ImportOptions(pages=pages)
            core.import_pdf(pdf, opts)
            _msg("Import completed.")
        except (RuntimeError, ValueError, TypeError, OSError, AttributeError, ImportError) as e:
            _err(f"Console import failed: {e}")
            _msg(traceback.format_exc())


# ──────────────────────────────────────────────────────────────────────
class ImportSKPCommand:
    """Import a SketchUp SKP file into the active FreeCAD document."""

    def GetResources(self):
        return {
            "Pixmap": "",
            "MenuText": "Import SKP…",
            "ToolTip": "Import a SketchUp .skp file with FreeCAD's available SKP importer.",
        }

    def IsActive(self):
        return QtWidgets is not None and FreeCAD is not None

    def Activated(self):
        skp, _ = QtWidgets.QFileDialog.getOpenFileName(
            None, "Select SKP", "", "SketchUp Files (*.skp)")
        if not skp:
            return

        if FreeCAD.ActiveDocument is None:
            FreeCAD.newDocument("SKP_Import")
        doc = FreeCAD.ActiveDocument

        # ── Backend 1: FreeCAD native Import module ──────────────────────
        backend_available = False
        try:
            import Import
            backend_available = True
        except ImportError:
            pass

        if not backend_available:
            _err("FreeCAD SKP importer module is unavailable (Import module missing).")
            if QtWidgets:
                QtWidgets.QMessageBox.warning(
                    None,
                    "SKP Import — Backend Not Found",
                    "FreeCAD could not find an SKP importer backend.\n\n"
                    "Possible solutions:\n"
                    "  1. Install the SketchUp Importer plugin from the FreeCAD\n"
                    "     addon manager (Tools → Addon Manager → search 'SKP')\n"
                    "  2. Export your file from SketchUp as COLLADA (.dae) or\n"
                    "     IFC (.ifc) — both are supported natively by FreeCAD\n"
                    "  3. Use SketchUp's free viewer to open the file, then\n"
                    "     re-export to a compatible format\n\n"
                    "Note: SKP is a proprietary format — native support requires\n"
                    "an optional FreeCAD module that may not be installed.")
            return

        # ── Backend 2: Try Import.insert (native path) ───────────────────
        try:
            Import.insert(skp, doc.Name)
            doc.recompute()
            _msg(f"SKP import completed: {skp}")
            if FreeCADGui and FreeCADGui.ActiveDocument and FreeCADGui.ActiveDocument.ActiveView:
                FreeCADGui.ActiveDocument.ActiveView.fitAll()
            return
        except (RuntimeError, ValueError, TypeError, OSError, AttributeError) as e:
            raw_err = str(e)
            _err(f"SKP import failed via native backend: {raw_err}")

        # ── Backend 3: Try Mesh module as fallback ────────────────────────
        mesh_ok = False
        try:
            import Mesh
            Mesh.insert(skp, doc.Name)
            doc.recompute()
            _msg(f"SKP imported as mesh (fallback): {skp}")
            if FreeCADGui and FreeCADGui.ActiveDocument and FreeCADGui.ActiveDocument.ActiveView:
                FreeCADGui.ActiveDocument.ActiveView.fitAll()
            mesh_ok = True
        except Exception:
            pass

        if mesh_ok:
            return

        # ── All backends failed — show actionable guidance ────────────────
        if QtWidgets:
            QtWidgets.QMessageBox.warning(
                None,
                "SKP Import — Format Not Supported",
                "This version of FreeCAD could not open the SKP file.\n\n"
                "The SKP format is proprietary to Trimble/SketchUp and requires\n"
                "a special importer that may not be installed or may not support\n"
                "this SKP version.\n\n"
                "Best alternatives:\n"
                "  1. Open the file in SketchUp (free web version at app.sketchup.com)\n"
                "     and export as COLLADA (.dae) — FreeCAD opens these natively\n"
                "  2. Export as IFC (.ifc) from SketchUp if you need BIM data\n"
                "  3. Export as OBJ (.obj) for mesh-only geometry\n\n"
                "Then use FreeCAD's File → Import to open the converted file.")


# ──────────────────────────────────────────────────────────────────────
class BatchImportCommand:
    """Import all PDFs in a folder."""

    def GetResources(self):
        return {
            "Pixmap": "",
            "MenuText": "Batch Import…",
            "ToolTip": "Import all PDF files in a folder (optionally recursive).",
        }

    def IsActive(self):
        return QtWidgets is not None

    def Activated(self):
        import PDFVectorImporter.src.PDFImporterCore as core

        folder = QtWidgets.QFileDialog.getExistingDirectory(None, "Select folder")
        if not folder:
            return

        pages_str, ok = QtWidgets.QInputDialog.getText(
            None, "Pages", "all | first | 1,3-5", text="all")
        if not ok:
            return

        recurse = (
            QtWidgets.QMessageBox.question(
                None, "Recurse?", "Include subfolders?",
                QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
                QtWidgets.QMessageBox.No)
            == QtWidgets.QMessageBox.Yes)

        pdfs = []
        if recurse:
            for root, _, files in os.walk(folder):
                for f in files:
                    if f.lower().endswith(".pdf"):
                        pdfs.append(os.path.join(root, f))
        else:
            for f in os.listdir(folder):
                if f.lower().endswith(".pdf"):
                    pdfs.append(os.path.join(folder, f))

        if not pdfs:
            _warn("No PDF files found in the selected folder.")
            return

        ok_count = fail_count = 0
        _msg(f"\n═══ Batch Import: {len(pdfs)} PDF files ═══")
        for pdf_path in sorted(pdfs):
            pages = _parse_page_spec(pages_str, pdf_path)
            for pg in pages:
                try:
                    if FreeCAD.ActiveDocument is None:
                        FreeCAD.newDocument()
                    opts = core.ImportOptions(pages=[pg])
                    core.import_pdf(pdf_path, opts)
                    ok_count += 1
                except (RuntimeError, ValueError, TypeError, OSError, AttributeError) as e:
                    fail_count += 1
                    _err(f"  FAIL: {pdf_path} page {pg} — {e}")
        _msg(f"═══ Batch done: {ok_count} ok, {fail_count} failed ═══\n")


# ──────────────────────────────────────────────────────────────────────
class InstallPyMuPDFCommand:
    """One-click installer for PyMuPDF into the workbench's lib folder."""

    def GetResources(self):
        return {
            "Pixmap": "",
            "MenuText": "Install / Update PyMuPDF",
            "ToolTip": "Download and install PyMuPDF into this workbench (no admin needed).",
        }

    def IsActive(self):
        return True

    def Activated(self):
        import subprocess

        base = _wb_base()
        if not base:
            _err("Cannot find workbench directory!")
            return

        target = os.path.join(base, "src", "lib")
        os.makedirs(target, exist_ok=True)

        py = _find_python()

        _msg(f"Installing PyMuPDF to: {target}")
        _msg(f"Using Python: {py}")

        _kw = {}
        if sys.platform == "win32":
            _kw["creationflags"] = 0x08000000  # CREATE_NO_WINDOW

        try:
            subprocess.check_call(
                [py, "-m", "ensurepip", "--upgrade"],
                timeout=120, **_kw)
        except (subprocess.CalledProcessError, subprocess.TimeoutExpired, OSError):
            _warn("ensurepip skipped (may already be present)")

        try:
            subprocess.check_call(
                [py, "-m", "pip", "install", "--upgrade",
                 "--only-binary", ":all:", "--target", target, "PyMuPDF"],
                timeout=300, **_kw)
            _msg("PyMuPDF installed successfully.  Please restart FreeCAD.")
            if QtWidgets:
                QtWidgets.QMessageBox.information(
                    None, "Success",
                    f"PyMuPDF installed to:\n{target}\n\n"
                    "Please restart FreeCAD.")
        except subprocess.CalledProcessError as e:
            _err(f"pip install failed: {e}")
            if QtWidgets:
                QtWidgets.QMessageBox.critical(
                    None, "Install Failed",
                    f"pip install PyMuPDF failed:\n{e}\n\n"
                    "Try running manually in a terminal:\n"
                    f'  "{py}" -m pip install --target "{target}" PyMuPDF')
        except (subprocess.SubprocessError, OSError, RuntimeError, ValueError) as e:
            _err(f"Installer error: {e}\n{traceback.format_exc()}")


# ──────────────────────────────────────────────────────────────────────
# Helpers
# ──────────────────────────────────────────────────────────────────────
def _parse_page_spec(spec: str, pdf_path: str) -> list:
    """Parse a page specification string into a list of 1-based page numbers."""
    try:
        import fitz
        pdoc = fitz.open(pdf_path)
        n = len(pdoc)
        pdoc.close()
    except (ImportError, OSError, RuntimeError):
        n = 9999

    s = (spec or "1").strip().lower()
    if s in ("all", "a", "*"):
        return list(range(1, n + 1))
    if s in ("first", "1st"):
        return [1]
    out = []
    for part in s.split(","):
        part = part.strip()
        if not part:
            continue
        try:
            if "-" in part:
                a, b = part.split("-", 1)
                out += list(range(int(a), int(b) + 1))
            else:
                out.append(int(part))
        except ValueError:
            continue  # skip non-numeric page specs
    return out or [1]
