# BlueCollar Systems — BUILT. NOT BOUGHT.
#
# FreeCAD QA harness for PDF Vector Importer.
#
# Run with:
#   FreeCADCmd.exe adapters/freecad_harness.py
#
# Reads ENV["BC_PDF_QA_PAYLOAD"], performs the import, writes result JSON.

from __future__ import annotations

import importlib
import json
import os
import shutil
import subprocess
import sys
import time
import traceback
from pathlib import Path
from typing import List, Optional, Set


def resolve_path(value: Optional[str], base_dir: Optional[str] = None) -> Optional[str]:
    if value is None:
        return None
    raw = os.path.expandvars(str(value))
    p = Path(raw).expanduser()
    if not p.is_absolute() and base_dir:
        p = Path(base_dir) / p
    return str(p.resolve())


def parse_pages(spec: Optional[str], pdf_path: str):
    s = (spec or "").strip()
    if not s:
        return [1]

    if s.lower() == "all":
        try:
            import fitz  # type: ignore

            doc = fitz.open(pdf_path)
            total = len(doc)
            doc.close()
            return list(range(1, total + 1))
        except (ImportError, OSError, RuntimeError):
            return [1]

    pages: Set[int] = set()
    for part in [p.strip() for p in s.replace(";", ",").split(",") if p.strip()]:
        if "-" in part:
            a, b = [x.strip() for x in part.split("-", 1)]
            if a.isdigit() and b.isdigit():
                start, end = sorted((int(a), int(b)))
                for n in range(start, end + 1):
                    if n > 0:
                        pages.add(n)
        elif part.isdigit():
            n = int(part)
            if n > 0:
                pages.add(n)
    return sorted(pages) if pages else [1]


def preset_to_opts(preset_name: str):
    # Mirrors defaults used by the FreeCAD UI command.
    presets = {
        "Fast Preview": dict(curve_step=2.0, join_tol=0.5, detect_arcs=False, map_dashes=False, make_faces=False, text="No text", hatch_mode="skip", strict_text_fidelity=False),
        "General Vector": dict(curve_step=1.0, join_tol=0.2, detect_arcs=False, map_dashes=False, make_faces=True, text="Geometry", hatch_mode="import", strict_text_fidelity=True),
        "Technical Drawing": dict(curve_step=0.5, join_tol=0.1, detect_arcs=True, map_dashes=True, make_faces=True, text="Geometry", hatch_mode="group", strict_text_fidelity=True),
        "Shop Drawing": dict(curve_step=0.5, join_tol=0.1, detect_arcs=True, map_dashes=True, make_faces=True, text="Geometry", hatch_mode="group", strict_text_fidelity=True),
        "Max Fidelity": dict(curve_step=0.2, join_tol=0.05, detect_arcs=True, map_dashes=True, make_faces=True, text="Geometry", hatch_mode="import", strict_text_fidelity=True),
        # Cross-host alias used by SketchUp side:
        "Full": dict(curve_step=0.5, join_tol=0.1, detect_arcs=True, map_dashes=True, make_faces=True, text="Geometry", hatch_mode="group", strict_text_fidelity=True),
    }
    return presets.get(preset_name or "", presets["Shop Drawing"])


def setup_import_paths(payload: dict, payload_dir: str) -> None:
    mod_dir = resolve_path(payload.get("mod_dir"), payload_dir)
    if mod_dir and os.path.isdir(mod_dir):
        p = Path(mod_dir)
        if p.name.lower() == "pdfvectorimporter":
            sys.path.insert(0, str(p.parent))
            sys.path.insert(0, str(p))
            src = p / "src"
            if src.is_dir():
                sys.path.insert(0, str(src))
        else:
            sys.path.insert(0, str(p))
            pkg = p / "PDFVectorImporter"
            if pkg.is_dir():
                sys.path.insert(0, str(pkg.parent))
                src = pkg / "src"
                if src.is_dir():
                    sys.path.insert(0, str(src))


def import_core_module():
    errors = {}
    for name in (
        "PDFVectorImporter.src.PDFImporterCore",
        "src.PDFImporterCore",
        "PDFImporterCore",
    ):
        try:
            return importlib.import_module(name)
        except (ImportError, ModuleNotFoundError, AttributeError, RuntimeError, ValueError, SyntaxError) as exc:
            errors[name] = f"{exc.__class__.__name__}: {exc}"
            continue
    raise RuntimeError(
        "Could not import PDFImporterCore module from configured mod_dir. "
        f"Attempts: {errors}"
    )


def _looks_like_python(path_or_name: str) -> bool:
    name = Path(path_or_name).name.lower()
    return name.startswith("python") or name in ("py", "py.exe")


def _candidate_python_interpreters() -> List[str]:
    candidates: List[str] = []

    env_py = os.environ.get("BC_PDF_QA_PYTHON", "").strip()
    if env_py:
        candidates.append(env_py)

    exe = sys.executable or ""
    if exe:
        candidates.append(exe)
        try:
            bindir = Path(exe).resolve().parent
        except (OSError, RuntimeError, ValueError):
            bindir = Path(exe).parent

        for folder in (bindir, bindir / "Scripts", bindir.parent, bindir.parent / "Scripts"):
            for name in ("python.exe", "python3.exe", "python", "py.exe"):
                p = folder / name
                if p.is_file():
                    candidates.append(str(p))

    for name in ("python", "python3", "py"):
        found = shutil.which(name)
        if found:
            candidates.append(found)

    out: List[str] = []
    seen = set()
    for c in candidates:
        if not c:
            continue
        norm = os.path.normcase(os.path.abspath(os.path.expandvars(c)))
        if norm in seen:
            continue
        seen.add(norm)
        out.append(c)
    return out


def _run_cmd(cmd: List[str], timeout_s: int = 300) -> dict:
    kwargs = {
        "capture_output": True,
        "text": True,
        "timeout": timeout_s,
    }
    if sys.platform.startswith("win"):
        kwargs["creationflags"] = 0x08000000  # CREATE_NO_WINDOW

    proc = subprocess.run(cmd, **kwargs)
    return {
        "cmd": cmd,
        "returncode": int(proc.returncode),
        "stdout_tail": (proc.stdout or "")[-1500:],
        "stderr_tail": (proc.stderr or "")[-1500:],
    }


def ensure_pymupdf(mod_dir: Optional[str]) -> dict:
    try:
        import fitz  # type: ignore  # noqa: F401
        return {"status": "available", "installed_now": False}
    except ImportError as first_exc:
        if not mod_dir:
            raise RuntimeError(f"PyMuPDF missing and mod_dir not provided: {first_exc}") from first_exc

        p = Path(mod_dir)
        if p.name.lower() == "pdfvectorimporter":
            lib_dir = p / "src" / "lib"
        else:
            lib_dir = p / "PDFVectorImporter" / "src" / "lib"

        lib_dir.mkdir(parents=True, exist_ok=True)
        if str(lib_dir) not in sys.path:
            sys.path.insert(0, str(lib_dir))

        # Try once more in case it already exists in bundled lib.
        try:
            import fitz  # type: ignore  # noqa: F401
            return {"status": "available_from_lib_dir", "installed_now": False, "lib_dir": str(lib_dir)}
        except ImportError:
            pass

        attempts = []
        interpreters = _candidate_python_interpreters()
        for py in interpreters:
            if not _looks_like_python(py):
                attempts.append({
                    "python": py,
                    "status": "skipped_non_python_exe",
                })
                continue

            step_results = []

            pip_check = None
            try:
                pip_check = _run_cmd([py, "-m", "pip", "--version"], timeout_s=120)
                step_results.append(pip_check)
            except (subprocess.SubprocessError, OSError, ValueError, RuntimeError) as exc:
                step_results.append({"cmd": [py, "-m", "pip", "--version"], "error": str(exc)})

            if not isinstance(pip_check, dict) or pip_check.get("returncode") != 0:
                try:
                    step_results.append(_run_cmd([py, "-m", "ensurepip", "--upgrade"], timeout_s=180))
                except (subprocess.SubprocessError, OSError, ValueError, RuntimeError) as exc:
                    step_results.append({"cmd": [py, "-m", "ensurepip", "--upgrade"], "error": str(exc)})

            install_result = None
            try:
                install_result = _run_cmd(
                    [
                        py,
                        "-m",
                        "pip",
                        "install",
                        "--only-binary",
                        ":all:",
                        "--disable-pip-version-check",
                        "--target",
                        str(lib_dir),
                        "PyMuPDF",
                    ],
                    timeout_s=600,
                )
                step_results.append(install_result)
            except (subprocess.SubprocessError, OSError, ValueError, RuntimeError) as exc:
                step_results.append(
                    {
                        "cmd": [py, "-m", "pip", "install", "--target", str(lib_dir), "PyMuPDF"],
                        "error": str(exc),
                    }
                )

            importlib.invalidate_caches()
            if str(lib_dir) not in sys.path:
                sys.path.insert(0, str(lib_dir))

            try:
                import fitz  # type: ignore  # noqa: F401
                return {
                    "status": "installed_to_lib_dir",
                    "installed_now": True,
                    "lib_dir": str(lib_dir),
                    "python": py,
                    "attempts": attempts + [{"python": py, "steps": step_results}],
                }
            except ImportError as exc:
                attempts.append(
                    {
                        "python": py,
                        "status": "import_failed_after_install",
                        "final_error": f"{exc.__class__.__name__}: {exc}",
                        "steps": step_results,
                        "install_returncode": (
                            install_result.get("returncode")
                            if isinstance(install_result, dict)
                            else None
                        ),
                    }
                )

        raise RuntimeError(
            f"PyMuPDF unavailable after install attempts. lib_dir={lib_dir}. "
            f"first_error={first_exc}. attempts={attempts}"
        ) from first_exc


def count_doc_objects(doc) -> dict:
    objects = list(getattr(doc, "Objects", []) or [])
    out = {
        "objects_total": len(objects),
        "groups": 0,
        "wires": 0,
        "faces": 0,
        "texts": 0,
    }
    for obj in objects:
        t = getattr(obj, "TypeId", "") or ""
        if "DocumentObjectGroup" in t:
            out["groups"] += 1
        if "Part::Feature" in t and hasattr(obj, "Shape"):
            try:
                sh = obj.Shape
                if getattr(sh, "Wires", None):
                    out["wires"] += len(sh.Wires)
                if getattr(sh, "Faces", None):
                    out["faces"] += len(sh.Faces)
            except (AttributeError, TypeError, RuntimeError):
                pass
        if "Text" in t:
            out["texts"] += 1
    return out


def main() -> int:
    payload_path = os.environ.get("BC_PDF_QA_PAYLOAD", "").strip()
    if not payload_path:
        raise RuntimeError("BC_PDF_QA_PAYLOAD not set")

    with open(payload_path, "r", encoding="utf-8") as f:
        payload = json.load(f)

    payload_dir = str(Path(payload_path).resolve().parent)
    result_path = payload["result_json"]
    start = time.time()

    result = {
        "test_id": payload.get("test_id"),
        "platform": "FC",
        "status": "FAIL",
        "message": "",
        "started_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime(start)),
    }

    try:
        setup_import_paths(payload, payload_dir)
        resolved_mod_dir = resolve_path(payload.get("mod_dir"), payload_dir)
        result["mod_dir"] = resolved_mod_dir
        result["sys_path_head"] = list(sys.path[:12])
        result["pymupdf"] = ensure_pymupdf(resolved_mod_dir)

        import FreeCAD  # type: ignore

        core = import_core_module()

        input_pdf = resolve_path(payload.get("input_pdf"), payload_dir)
        if not input_pdf or not os.path.isfile(input_pdf):
            raise FileNotFoundError(f"Input PDF not found: {input_pdf}")

        pages = parse_pages(payload.get("page_range"), input_pdf)
        preset = preset_to_opts((payload.get("preset") or "").strip())
        text_mode = "geometry" if preset["text"] == "Geometry" else ("none" if preset["text"] == "No text" else "labels")
        import_text = text_mode != "none"

        opts = core.ImportOptions(
            pages=pages,
            scale_to_mm=True,
            user_scale=1.0,
            flip_y=True,
            join_tol=float(preset["join_tol"]),
            curve_step_mm=float(preset["curve_step"]),
            make_faces=bool(preset["make_faces"]),
            import_text=import_text,
            text_mode=text_mode,
            strict_text_fidelity=bool(preset.get("strict_text_fidelity", True)),
            hatch_mode=str(preset["hatch_mode"]),
            group_by_color=True,
            assign_linewidth=True,
            map_dashes=bool(preset["map_dashes"]),
            detect_arcs=bool(preset["detect_arcs"]),
            ignore_images=True,
            raster_fallback=True,
            create_top_group=True,
            verbose=False,
        )

        doc = FreeCAD.ActiveDocument or FreeCAD.newDocument("BC_QA")
        before = count_doc_objects(doc)

        ok = core.import_pdf(input_pdf, opts)
        doc.recompute()

        after = count_doc_objects(doc)
        delta = {k: after.get(k, 0) - before.get(k, 0) for k in after.keys()}

        result["status"] = "PASS" if ok is not False else "FAIL"
        result["message"] = "Import completed." if ok is not False else "core.import_pdf returned False."
        result["input_pdf"] = input_pdf
        result["preset"] = payload.get("preset")
        result["page_range"] = payload.get("page_range")
        result["pages"] = pages
        result["counts_before"] = before
        result["counts_after"] = after
        result["counts_delta"] = delta
    except (RuntimeError, OSError, ValueError, TypeError, AttributeError, ImportError) as exc:
        result["status"] = "FAIL"
        result["message"] = f"{exc.__class__.__name__}: {exc}"
        result["traceback"] = traceback.format_exc()
    finally:
        finish = time.time()
        result["finished_at"] = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime(finish))
        result["runtime_seconds"] = round(finish - start, 3)
        with open(result_path, "w", encoding="utf-8") as f:
            json.dump(result, f, indent=2)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
elif os.environ.get("BC_PDF_QA_PAYLOAD"):
    # FreeCADCmd may execute script files with a non-"__main__" module name.
    # In that case still run the harness when payload is explicitly provided.
    main()
