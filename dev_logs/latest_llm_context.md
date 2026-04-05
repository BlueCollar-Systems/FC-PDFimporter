# LLM Context Pack — FreeCAD PDF Importer

- Generated: `2026-04-05 11:14:52`
- Project Root: `C:/1FC-PDFimporter`
- Output File: `C:/1FC-PDFimporter/dev_logs/llm_context_20260405_111452.md`
- Formatting Safety: dynamic fenced blocks are used to avoid fence collisions.

## Project Inventory

Filtered inventory for context quality. Heavy/generated folders are excluded.

- `.gitattributes`: 66.00 B
- `.github/`: 3 files
- `.gitignore`: 667.00 B
- `0build_master_output_1FC-PDFimporter.cmd`: 135.00 B
- `0build_master_output_1FC-PDFimporter.py`: 2.27 KB
- `build_release.py`: 3.25 KB
- `build_windows_installer.py`: 3.71 KB
- `installer/`: 1 files
- `LICENSE`: 1.08 KB
- `PDFVectorImporter/`: 104 files
- `PDFVectorImporter_v3.6.0.zip`: 90.51 KB
- `PDFVectorImporter_v3.6.6.zip`: 78.40 KB
- `pyproject.toml`: 196.00 B
- `qa_sweep_workbook.xlsx`: 6.65 KB
- `README.md`: 3.79 KB
- `repo_context_builder_core.py`: 22.10 KB
- `requirements-dev.txt`: 167.00 B
- `tests/`: 1 files

## Repo Tree

Depth-limited tree. Full depth for selected roots, shallow for noisy areas.

```text
1FC-PDFimporter/
├── .github/
│   └── workflows/
│       ├── auto-release.yml
│       ├── fc-pdfimporter-ci.yml
│       └── windows-release.yml
├── installer/
│   └── PDFVectorImporter.iss
├── PDFVectorImporter/
│   ├── adapters/
│   │   ├── blender_adapter.py
│   │   ├── freecad_adapter.py
│   │   ├── freecad_harness.py
│   │   ├── librecad_adapter.py
│   │   ├── sketchup_adapter.py
│   │   └── sketchup_harness.rb
│   ├── pdfcadcore/
│   │   ├── tests/
│   │   ├── __init__.py
│   │   ├── auto_mode.py
│   │   ├── dimension_parser.py
│   │   ├── document_profiler.py
│   │   ├── generic_classifier.py
│   │   ├── generic_recognizer.py
│   │   ├── geometry_cleanup.py
│   │   ├── hatch_detector.py
│   │   ├── import_config.py
│   │   ├── primitive_extractor.py
│   │   ├── primitives.py
│   │   ├── recognition.py
│   │   ├── regions.py
│   │   └── validation.py
│   ├── qa_runs/
│   │   ├── 20260329_205803/
│   │   │   ├── su_manual_probe/
│   │   │   │   ├── autoload_probe_marker.txt
│   │   │   │   ├── env_probe_marker.txt
│   │   │   │   ├── harness_debug_log.txt
│   │   │   │   ├── harness_debug_map_log.txt
│   │   │   │   ├── json_probe_marker.txt
│   │   │   │   ├── payload.json
│   │   │   │   ├── payload_map.json
│   │   │   │   ├── result.json
│   │   │   │   ├── result_map.json
│   │   │   │   └── startup_probe.rb
│   │   │   ├── fc_verify_map.json
│   │   │   ├── fc_verify_plant.json
│   │   │   ├── fc_verify_weld.json
│   │   │   ├── su_smoke_test.txt
│   │   │   ├── su_verify_map.json
│   │   │   ├── su_verify_plant.json
│   │   │   └── su_verify_weld.json
│   │   ├── 20260329_213208/
│   │   │   ├── consolidated_alvord_report.json
│   │   │   ├── consolidated_alvord_report.md
│   │   │   ├── FC-ALV-01.json
│   │   │   ├── FC-ALV-02.json
│   │   │   ├── FC-ALV-03.json
│   │   │   ├── FC-ALV-04.json
│   │   │   ├── FC-ALV-05.json
│   │   │   ├── SU-ALV-01.json
│   │   │   ├── SU-ALV-02.json
│   │   │   ├── SU-ALV-03.json
│   │   │   ├── SU-ALV-04.json
│   │   │   └── SU-ALV-05.json
│   │   ├── cross_platform_20260403/
│   │   │   ├── bl_results.csv
│   │   │   ├── bl_results.json
│   │   │   ├── lc_results.csv
│   │   │   ├── lc_results.json
│   │   │   ├── qa_config_cross_platform.json
│   │   │   ├── qa_cross_platform.xlsx
│   │   │   ├── qa_cross_platform_bl.xlsx
│   │   │   └── qa_cross_platform_lc.xlsx
│   │   ├── feature_compare_20260404_033716/
│   │   │   ├── feature_matrix.json
│   │   │   └── feature_matrix.md
│   │   ├── feature_compare_20260404_034635/
│   │   │   ├── feature_matrix.json
│   │   │   └── feature_matrix.md
│   │   ├── feature_compare_20260404_034914/
│   │   │   ├── feature_matrix.json
│   │   │   └── feature_matrix.md
│   │   └── feature_compare_20260404_034940/
│   │       ├── feature_matrix.json
│   │       └── feature_matrix.md
│   ├── resources/
│   │   └── ImportPDFVector.svg
│   ├── src/
│   │   ├── __init__.py
│   │   ├── PDFDimensionParser.py
│   │   ├── PDFDocumentProfiler.py
│   │   ├── PDFGenericClassifier.py
│   │   ├── PDFGenericRecognizer.py
│   │   ├── PDFGeometryCleanup.py
│   │   ├── PDFHatchDetector.py
│   │   ├── PDFImportConfig.py
│   │   ├── PDFImporterCmd.py
│   │   ├── PDFImporterCore.py
│   │   ├── PDFPrimitiveExtractor.py
│   │   ├── PDFPrimitives.py
│   │   ├── PDFRecognition.py
│   │   ├── PDFRegions.py
│   │   ├── PDFScaleTool.py
│   │   ├── PDFSvgTextRenderer.py
│   │   └── PDFValidation.py
│   ├── .gitignore
│   ├── __init__.py
│   ├── compare_feature_matrix.py
│   ├── fc_check_fitz.py
│   ├── fc_smoke_payload.json
│   ├── Init.py
│   ├── InitGui.py
│   ├── LICENSE
│   ├── package.xml
│   ├── PDF with embedded images.pdf
│   ├── PDFImportHandler.py
│   ├── PDFTools.py
│   ├── qa_config_example.json
│   ├── qa_config_local_live.json
│   ├── qa_config_template.json
│   ├── qa_results.csv
│   ├── qa_results.json
│   ├── README.md
│   ├── run_pdf_vector_importer_tests.py
│   ├── su_manual_verification_checklist.md
│   └── THIRD_PARTY_NOTICES.md
├── tests/
│   └── test_pdf_primitive_extractor.py
├── .gitattributes
├── .gitignore
├── 0build_master_output_1FC-PDFimporter.cmd
├── 0build_master_output_1FC-PDFimporter.py
├── build_release.py
├── build_windows_installer.py
├── LICENSE
├── PDFVectorImporter_v3.6.0.zip
├── PDFVectorImporter_v3.6.6.zip
├── pyproject.toml
├── qa_sweep_workbook.xlsx
├── README.md
├── repo_context_builder_core.py
└── requirements-dev.txt
```

## Dependency Summary

### requirements-dev.txt

```text
ruff>=0.4.0
openpyxl>=3.1.0
```

## Missing Expected Files

### Expected Everywhere

None missing.

### Expected In Some Environments

None missing.

## Core Configuration Files

### README.md

- Path: `README.md`
- Size: `3.79 KB`
- Modified: `2026-04-04 04:18:12`

~~~markdown
# PDF Vector Importer for FreeCAD

**BUILT. NOT BOUGHT.**

![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)
![Version: 4.0.2](https://img.shields.io/badge/Version-4.0.2-blue.svg)
![Platform: FreeCAD 0.21+](https://img.shields.io/badge/Platform-FreeCAD%200.21%2B-orange.svg)

Import vector geometry, text, and images from PDF files into FreeCAD as editable Part objects.

Arc reconstruction, dash mapping, color grouping, OCG layer support, and reference-based scaling -- all powered by pure-Python PDF parsing via PyMuPDF.

> BlueCollar Systems -- BUILT. NOT BOUGHT.

## Key Features

| Category | Capability |
|----------|-----------|
| PDF Parsing | PyMuPDF-powered vector extraction with full path, text, and image support |
| Import Presets | Fast Preview, General Vector, Technical Drawing, Shop Drawing, Max Fidelity |
| Arc Reconstruction | Kasa algebraic circle fit converts polyline segments back to true arcs |
| Layer Support | OCG layers (PDF Optional Content Groups) map to FreeCAD groups |
| Color Grouping | Geometry automatically organized by stroke/fill color |
| Dash Patterns | PDF dash arrays mapped to FreeCAD line styles |
| Text Import | PDF text extracted with font size, position, and rotation |
| Image Import | Embedded raster images extracted and placed at correct coordinates |
| Scale Detection | Reference-based scaling from known dimensions on the drawing |
| Steel Detection | Recognizes common structural steel shape profiles |

## Installation

### From FreeCAD Addon Manager (Recommended)
1. Open FreeCAD → **Tools** → **Addon Manager**
2. Search for **PDF Vector Importer**
3. Click **Install**
4. Restart FreeCAD

### Windows Setup.exe (Easy Manual Install)
1. Download `PDFVectorImporter_Setup_vX.Y.Z.exe` from Releases.
2. Close FreeCAD.
3. Run the installer (no admin rights required).
4. Restart FreeCAD.

### Manual Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/BlueCollar-Systems/FC-PDFimporter.git
   ```
2. Copy the `PDFVectorImporter` folder into your FreeCAD Mod directory:
   - **Windows:** `%APPDATA%\FreeCAD\Mod\`
   - **macOS:** `~/Library/Application Support/FreeCAD/Mod/`
   - **Linux:** `~/.local/share/FreeCAD/Mod/`
3. Install PyMuPDF:
   ```bash
   pip install PyMuPDF
   ```
4. Restart FreeCAD

## Building Release Artifacts

### Build Addon ZIP
```bash
python build_release.py
```

### Build Windows Installer (.exe)
1. Install [Inno Setup 6](https://jrsoftware.org/isinfo.php)
2. Run:
   ```bash
   python build_windows_installer.py
   ```
3. Output files are written to `dist/`:
   - `PDFVectorImporter_vX.Y.Z.zip`
   - `PDFVectorImporter_Setup_vX.Y.Z.exe`

### Auto-Build on GitHub Releases
1. Push a tag in `vX.Y.Z` format (example: `v3.5.1`).
2. GitHub Actions workflow `windows-release` builds both artifacts.
3. The workflow attaches the ZIP and Setup.exe to that GitHub Release.

## Usage

1. Open FreeCAD
2. Go to **File** → **Import** or use the **PDF Vector Importer** workbench
3. Select a PDF file
4. Choose an import preset (or customize settings)
5. Click **Import**

## Import Presets

| Preset | Best For | Speed |
|--------|----------|-------|
| **Fast Preview** | Quick look at PDF contents | Fastest |
| **General Vector** | Most PDF files | Fast |
| **Technical Drawing** | Engineering drawings with dimensions | Medium |
| **Shop Drawing** | Fabrication shop drawings with steel shapes | Medium |
| **Max Fidelity** | Maximum accuracy, all features enabled | Slower |

## Requirements

- **FreeCAD** 0.21 or later
- **Python** 3.10+ (adapters use PEP 604 union types)
- **PyMuPDF** (automatically installed via Addon Manager)

## License

MIT License — see [LICENSE](LICENSE) for details.

Copyright (c) 2024-2026 BlueCollar Systems
~~~

### pyproject.toml

- Path: `pyproject.toml`
- Size: `196.00 B`
- Modified: `2026-04-02 17:11:20`

```toml
[tool.ruff]
target-version = "py38"
exclude = [
    "dist",
    "__pycache__",
    ".ruff_cache",
    "build_release.py",
    "build_windows_installer.py",
]

[tool.ruff.lint]
select = ["F", "B"]
```

### requirements-dev.txt

- Path: `requirements-dev.txt`
- Size: `167.00 B`
- Modified: `2026-04-01 20:04:25`

```text
# Development dependencies for PDF Vector Importer
# Runtime dependency (PyMuPDF) is managed via FreeCAD Addon Manager — see package.xml
ruff>=0.4.0
openpyxl>=3.1.0
```

### build_release.py

- Path: `build_release.py`
- Size: `3.25 KB`
- Modified: `2026-04-01 17:16:06`

```python
#!/usr/bin/env python3
"""build_release.py — BlueCollar Systems
Produces a clean PDFVectorImporter release zip suitable for FreeCAD Addon Manager
distribution and manual install.

Excluded:
  - __pycache__/ and *.pyc
  - .ruff_cache/
  - .github/
  - .git/
  - test PDFs, QA configs, and internal harness files
  - this script itself

Usage:
  python build_release.py
  python build_release.py --out /path/to/output_dir

Output:
  PDFVectorImporter_v<VERSION>.zip  (next to this script, or --out dir)
"""

import argparse
import re
import zipfile
from pathlib import Path

# ---------------------------------------------------------------------------
# Config
# ---------------------------------------------------------------------------

REPO_ROOT = Path(__file__).parent.resolve()
ADDON_DIR = REPO_ROOT / "PDFVectorImporter"

# Files / dirs to always exclude (matched against each path component)
EXCLUDE_DIRS = {
    "__pycache__",
    ".ruff_cache",
    ".github",
    ".git",
    "qa_runs",
    "adapters",  # CLI test harnesses — not needed at FreeCAD runtime
}

EXCLUDE_FILES = {
    ".gitignore",
    ".gitattributes",
    "build_release.py",
    "qa_config_example.json",
    "qa_config_template.json",
    "fc_smoke_payload.json",
    "fc_check_fitz.py",
    "run_pdf_vector_importer_tests.py",
    "su_manual_verification_checklist.md",
    "qa_config_local_live.json",
}

EXCLUDE_SUFFIXES = {
    ".pyc",
    ".pyo",
    ".pdf",       # test PDFs should not ship
    ".bak",
    ".swp",
}


def _should_exclude(rel: Path) -> bool:
    for part in rel.parts:
        if part in EXCLUDE_DIRS:
            return True
    if rel.name in EXCLUDE_FILES:
        return True
    if rel.suffix.lower() in EXCLUDE_SUFFIXES:
        return True
    return False


def _read_version() -> str:
    pkg_xml = ADDON_DIR / "package.xml"
    if pkg_xml.exists():
        text = pkg_xml.read_text(encoding="utf-8")
        m = re.search(r"<version>(.*?)</version>", text)
        if m:
            return m.group(1).strip()
    return "0.0.0"


def build(out_dir: Path) -> Path:
    version = _read_version()
    zip_name = f"PDFVectorImporter_v{version}.zip"
    zip_path = out_dir / zip_name

    out_dir.mkdir(parents=True, exist_ok=True)

    file_count = 0
    skipped = 0

    with zipfile.ZipFile(zip_path, "w", compression=zipfile.ZIP_DEFLATED) as zf:
        for abs_path in sorted(ADDON_DIR.rglob("*")):
            if not abs_path.is_file():
                continue
            rel = abs_path.relative_to(ADDON_DIR)
            if _should_exclude(rel):
                skipped += 1
                continue
            # Archive path: PDFVectorImporter/<rel>
            arc_name = Path("PDFVectorImporter") / rel
            zf.write(abs_path, arc_name)
            file_count += 1

    print(f"Built: {zip_path}")
    print(f"  {file_count} files included, {skipped} excluded")
    return zip_path


def main() -> None:
    parser = argparse.ArgumentParser(description="Build PDFVectorImporter release zip")
    parser.add_argument(
        "--out", default=str(REPO_ROOT),
        help="Output directory (default: repo root)"
    )
    args = parser.parse_args()

    out_dir = Path(args.out).resolve()
    zip_path = build(out_dir)
    print(f"\nRelease ready: {zip_path}")


if __name__ == "__main__":
    main()
```

### build_windows_installer.py

- Path: `build_windows_installer.py`
- Size: `3.71 KB`
- Modified: `2026-03-31 16:09:42`

```python
#!/usr/bin/env python3
"""Build a Windows Setup.exe installer for PDFVectorImporter using Inno Setup."""

from __future__ import annotations

import argparse
import os
import re
import shutil
import subprocess
import sys
import zipfile
from pathlib import Path

import build_release


REPO_ROOT = Path(__file__).parent.resolve()
ADDON_DIR = REPO_ROOT / "PDFVectorImporter"
DIST_DIR = REPO_ROOT / "dist"
STAGE_DIR = DIST_DIR / "installer_stage"
INNO_SCRIPT = REPO_ROOT / "installer" / "PDFVectorImporter.iss"


def read_version() -> str:
    package_xml = ADDON_DIR / "package.xml"
    if not package_xml.exists():
        raise FileNotFoundError(f"Missing package metadata: {package_xml}")

    text = package_xml.read_text(encoding="utf-8")
    match = re.search(r"<version>(.*?)</version>", text)
    if not match:
        raise RuntimeError("Could not determine version from package.xml")
    return match.group(1).strip()


def find_iscc(explicit_path: str | None) -> Path:
    candidates: list[Path] = []

    if explicit_path:
        candidates.append(Path(explicit_path))

    for name in ("iscc", "ISCC.exe"):
        on_path = shutil.which(name)
        if on_path:
            candidates.append(Path(on_path))

    for env_var in ("ProgramFiles", "ProgramFiles(x86)"):
        root = os.environ.get(env_var)
        if not root:
            continue
        base = Path(root)
        candidates.append(base / "Inno Setup 6" / "ISCC.exe")
        candidates.append(base / "Inno Setup 5" / "ISCC.exe")

    for candidate in candidates:
        if candidate.exists():
            return candidate.resolve()

    raise FileNotFoundError(
        "Inno Setup compiler (ISCC.exe) was not found.\n"
        "Install Inno Setup 6 from https://jrsoftware.org/isinfo.php "
        "or pass --iscc C:\\path\\to\\ISCC.exe."
    )


def stage_release() -> tuple[str, Path, Path]:
    version = read_version()
    DIST_DIR.mkdir(parents=True, exist_ok=True)

    zip_path = build_release.build(DIST_DIR)

    if STAGE_DIR.exists():
        shutil.rmtree(STAGE_DIR)
    STAGE_DIR.mkdir(parents=True, exist_ok=True)

    with zipfile.ZipFile(zip_path, "r") as zf:
        zf.extractall(STAGE_DIR)

    source_dir = STAGE_DIR / "PDFVectorImporter"
    if not source_dir.is_dir():
        raise RuntimeError(f"Expected staged addon folder at {source_dir}")

    return version, source_dir, zip_path


def compile_installer(iscc: Path, version: str, source_dir: Path) -> Path:
    cmd = [
        str(iscc),
        str(INNO_SCRIPT),
        f"/DMyAppVersion={version}",
        f"/DSourceDir={source_dir}",
    ]
    print("Running:", " ".join(cmd))
    subprocess.run(cmd, check=True, cwd=REPO_ROOT)

    installer_exe = DIST_DIR / f"PDFVectorImporter_Setup_v{version}.exe"
    if not installer_exe.exists():
        raise RuntimeError(
            "Inno Setup completed but installer was not found at "
            f"{installer_exe}"
        )
    return installer_exe


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Build PDFVectorImporter Windows installer (.exe)"
    )
    parser.add_argument(
        "--iscc",
        default=None,
        help="Path to ISCC.exe (Inno Setup compiler). Optional if ISCC is on PATH.",
    )
    args = parser.parse_args()

    version, source_dir, zip_path = stage_release()
    iscc = find_iscc(args.iscc)
    installer_exe = compile_installer(iscc, version, source_dir)

    print("")
    print(f"Release zip: {zip_path}")
    print(f"Installer:   {installer_exe}")
    print(f"Stage dir:   {source_dir}")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:  # pragma: no cover - entrypoint safety
        print(f"ERROR: {exc}", file=sys.stderr)
        raise SystemExit(1)
```

## Source Files

Included files: `95`

### PDFVectorImporter/__init__.py

- Path: `PDFVectorImporter/__init__.py`
- Size: `566.00 B`
- Modified: `2026-04-03 19:03:00`

```python
# PDFVectorImporter — FreeCAD Workbench
# BlueCollar Systems — BUILT. NOT BOUGHT.
import os
import sys

try:
    _base = os.path.dirname(os.path.abspath(__file__))
except NameError:
    # __file__ not defined (shouldn't happen for __init__.py, but be safe)
    import FreeCAD
    _base = os.path.join(FreeCAD.getUserAppDataDir(), "Mod", "PDFVectorImporter")

_src = os.path.join(_base, "src")
_lib = os.path.join(_src, "lib")

for _p in (_base, _src, _lib):
    if os.path.isdir(_p) and _p not in sys.path:
        sys.path.insert(0, _p)



```

### PDFVectorImporter/adapters/blender_adapter.py

- Path: `PDFVectorImporter/adapters/blender_adapter.py`
- Size: `7.82 KB`
- Modified: `2026-04-03 18:40:49`

```python
#!/usr/bin/env python3
"""
Blender adapter for PDF Vector Importer QA.

Runs the standalone Blender PDF importer CLI and classifies the run as
PASS/FAIL/BLOCKED for the central QA workbook runner.
"""
from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
import tempfile
import time
from pathlib import Path
from typing import Optional


def load_json(path: Optional[str]) -> dict:
    if not path:
        return {}
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def normalize_path(value: Optional[str], base_dir: Optional[str] = None) -> Optional[str]:
    if value is None:
        return None
    raw = os.path.expandvars(str(value))
    # Allow command-style executables like "python" without forcing path resolution.
    if ("/" not in raw and "\\" not in raw and not Path(raw).is_absolute()):
        return raw
    p = Path(raw).expanduser()
    if not p.is_absolute() and base_dir:
        p = Path(base_dir) / p
    return str(p.resolve())


def run_blender_cli(
    python_exe: str,
    repo_dir: str,
    input_pdf: str,
    preset: str,
    page_range: str,
    summary_json: str,
    timeout_seconds: int,
    no_text: bool = False,
    no_images: bool = False,
    no_arcs: bool = False,
) -> subprocess.CompletedProcess:
    cmd = [
        python_exe,
        "-m",
        "blender_pdf_vector_importer.cli",
        input_pdf,
        "--preset",
        preset,
        "--pages",
        page_range,
        "--json",
        summary_json,
    ]
    if no_text:
        cmd.append("--no-text")
    if no_images:
        cmd.append("--no-images")
    if no_arcs:
        cmd.append("--no-arcs")

    return subprocess.run(
        cmd,
        cwd=repo_dir,
        capture_output=True,
        text=True,
        timeout=timeout_seconds,
        check=False,
    )


def classify_result(summary: dict, min_primitives: int, max_seconds: int, runtime_seconds: float) -> tuple[str, str]:
    primitive_count = int(summary.get("primitives", 0))
    page_count = int(summary.get("pages", 0))
    if page_count <= 0:
        return "FAIL", "Importer returned 0 pages."
    if primitive_count < min_primitives:
        return "FAIL", f"Primitive count {primitive_count} below required minimum {min_primitives}."
    if max_seconds > 0 and runtime_seconds > max_seconds:
        return "FAIL", f"Runtime {runtime_seconds:.2f}s exceeded cap {max_seconds}s."
    return "PASS", f"Imported {primitive_count} primitives across {page_count} page(s)."


def main() -> int:
    parser = argparse.ArgumentParser(description="Blender adapter for PDF importer QA.")
    parser.add_argument("--config", help="Path to qa_config.json", required=False)
    parser.add_argument("--test-id", required=True)
    parser.add_argument("--input", required=True, help="Input PDF path")
    parser.add_argument("--preset", default="technical")
    parser.add_argument("--page-range", default="1")
    parser.add_argument("--min-primitives", type=int, default=1)
    parser.add_argument("--runtime-cap-seconds", type=int, default=0)
    parser.add_argument("--no-text", action="store_true")
    parser.add_argument("--no-images", action="store_true")
    parser.add_argument("--no-arcs", action="store_true")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    cfg = load_json(args.config)
    config_dir = str(Path(args.config).expanduser().resolve().parent) if args.config else os.getcwd()
    blender_cfg = cfg.get("blender", {})

    repo_dir = normalize_path(blender_cfg.get("repo_dir"), config_dir)
    python_exe = normalize_path(blender_cfg.get("python_exe"), config_dir) or sys.executable
    input_pdf = normalize_path(args.input, config_dir)
    timeout_seconds = int(blender_cfg.get("timeout_seconds", 1800))

    if args.dry_run:
        print(
            json.dumps(
                {
                    "test_id": args.test_id,
                    "platform": "BL",
                    "status": "DRY_RUN",
                    "message": "Blender adapter config parsed successfully.",
                    "repo_dir": repo_dir,
                    "python_exe": python_exe,
                },
                indent=2,
            )
        )
        return 0

    if not repo_dir or not os.path.isdir(repo_dir):
        print(
            json.dumps(
                {
                    "test_id": args.test_id,
                    "platform": "BL",
                    "status": "ERROR",
                    "message": f"Blender repo_dir not found: {repo_dir}",
                },
                indent=2,
            )
        )
        return 2
    if not input_pdf or not os.path.isfile(input_pdf):
        print(
            json.dumps(
                {
                    "test_id": args.test_id,
                    "platform": "BL",
                    "status": "ERROR",
                    "message": f"Input PDF not found: {input_pdf}",
                },
                indent=2,
            )
        )
        return 2

    with tempfile.TemporaryDirectory(prefix="bc_pdf_bl_qa_") as td:
        summary_path = os.path.join(td, f"{args.test_id}_bl_summary.json")
        started = time.perf_counter()
        try:
            proc = run_blender_cli(
                python_exe=python_exe,
                repo_dir=repo_dir,
                input_pdf=input_pdf,
                preset=args.preset,
                page_range=args.page_range,
                summary_json=summary_path,
                timeout_seconds=timeout_seconds,
                no_text=args.no_text,
                no_images=args.no_images,
                no_arcs=args.no_arcs,
            )
        except subprocess.TimeoutExpired:
            print(
                json.dumps(
                    {
                        "test_id": args.test_id,
                        "platform": "BL",
                        "status": "FAIL",
                        "message": f"Timed out after {timeout_seconds}s.",
                    },
                    indent=2,
                )
            )
            return 1

        runtime_seconds = round(time.perf_counter() - started, 3)
        if proc.returncode != 0:
            print(
                json.dumps(
                    {
                        "test_id": args.test_id,
                        "platform": "BL",
                        "status": "FAIL",
                        "message": f"CLI exited {proc.returncode}",
                        "stdout": (proc.stdout or "")[-2000:],
                        "stderr": (proc.stderr or "")[-2000:],
                    },
                    indent=2,
                )
            )
            return proc.returncode

        if not os.path.isfile(summary_path):
            print(
                json.dumps(
                    {
                        "test_id": args.test_id,
                        "platform": "BL",
                        "status": "FAIL",
                        "message": "CLI did not produce summary JSON.",
                        "stdout": (proc.stdout or "")[-2000:],
                        "stderr": (proc.stderr or "")[-2000:],
                    },
                    indent=2,
                )
            )
            return 1

        with open(summary_path, "r", encoding="utf-8") as f:
            summary = json.load(f)

        status, message = classify_result(summary, args.min_primitives, args.runtime_cap_seconds, runtime_seconds)
        print(
            json.dumps(
                {
                    "test_id": args.test_id,
                    "platform": "BL",
                    "status": status,
                    "message": message,
                    "runtime_seconds": runtime_seconds,
                    "summary": summary,
                },
                indent=2,
            )
        )
        return 0 if status == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
```

### PDFVectorImporter/adapters/freecad_adapter.py

- Path: `PDFVectorImporter/adapters/freecad_adapter.py`
- Size: `6.77 KB`
- Modified: `2026-04-02 17:26:17`

```python
#!/usr/bin/env python3
"""
FreeCAD adapter for PDF Vector Importer QA.

Purpose:
- Provides a stable command-line interface for the external test runner.
- Can launch FreeCAD in GUI or console mode.
- Hands off a payload JSON to a Python harness script that performs the import
  and writes a result JSON file.

Typical use:
python adapters/freecad_adapter.py --config qa_config.json --test-id FC-GEO-001 --input "C:/tests/1071 - Rev 0.pdf" --preset "Shop Drawing" --dry-run
"""
from __future__ import annotations

from typing import Optional, Tuple

import argparse
import json
import os
import subprocess
import tempfile
import time
from pathlib import Path


def load_json(path: Optional[str]) -> dict:
    if not path:
        return {}
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def normalize_path(value: Optional[str], base_dir: Optional[str] = None) -> Optional[str]:
    if value is None:
        return None
    raw = os.path.expandvars(str(value))
    p = Path(raw).expanduser()
    if not p.is_absolute() and base_dir:
        p = Path(base_dir) / p
    return str(p.resolve())


def build_payload(args: argparse.Namespace, cfg: dict, result_path: str, config_dir: Optional[str]) -> dict:
    freecad_cfg = cfg.get("freecad", {})
    return {
        "adapter": "freecad",
        "timestamp_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "test_id": args.test_id,
        "platform": "FC",
        "input_pdf": normalize_path(args.input, config_dir),
        "preset": args.preset,
        "page_range": args.page_range,
        "output_dir": normalize_path(args.output_dir, config_dir) if args.output_dir else None,
        "result_json": result_path,
        "mod_dir": normalize_path(freecad_cfg.get("mod_dir"), config_dir),
        "python_harness": normalize_path(freecad_cfg.get("python_harness"), config_dir),
        "expected": {
            "layers_min_populated": args.layers_min_populated,
            "runtime_cap_seconds": args.runtime_cap_seconds,
        },
        "notes": args.notes or "",
    }


def launch_freecad_console(freecadcmd_exe: str, harness: str, payload_path: str,
                           timeout: int = 300) -> Tuple[int, str, str]:
    env = os.environ.copy()
    env["BC_PDF_QA_PAYLOAD"] = payload_path

    cmd = [freecadcmd_exe, harness]
    try:
        proc = subprocess.run(cmd, capture_output=True, text=True, env=env,
                              timeout=timeout)
    except subprocess.TimeoutExpired:
        return (
            1,
            "",
            f"FreeCAD process timed out after {timeout} seconds. "
            "Consider increasing the timeout or checking if the harness is stuck.",
        )
    stdout = proc.stdout or ""
    stderr = proc.stderr or ""
    return proc.returncode, stdout, stderr


def main() -> int:
    parser = argparse.ArgumentParser(description="FreeCAD adapter for PDF Vector Importer QA.")
    parser.add_argument("--config", help="Path to qa_config.json", required=False)
    parser.add_argument("--test-id", required=True, help="Test ID, e.g. FC-GEO-001")
    parser.add_argument("--input", required=True, help="Input PDF path")
    parser.add_argument("--preset", default="Shop Drawing", help="Import preset name")
    parser.add_argument("--page-range", default="1", help="Page range string")
    parser.add_argument("--output-dir", help="Optional output directory")
    parser.add_argument("--notes", help="Optional notes")
    parser.add_argument("--layers-min-populated", type=int, default=0)
    parser.add_argument("--runtime-cap-seconds", type=int, default=0)
    parser.add_argument("--dry-run", action="store_true", help="Do not launch FreeCAD; emit a starter result only.")
    args = parser.parse_args()

    cfg = load_json(args.config)
    config_dir = str(Path(args.config).expanduser().resolve().parent) if args.config else os.getcwd()
    freecad_cfg = cfg.get("freecad", {})

    with tempfile.TemporaryDirectory(prefix="bc_pdf_fc_qa_") as td:
        payload_path = os.path.join(td, f"{args.test_id}_payload.json")
        result_path = os.path.join(td, f"{args.test_id}_result.json")

        payload = build_payload(args, cfg, result_path, config_dir)
        with open(payload_path, "w", encoding="utf-8") as f:
            json.dump(payload, f, indent=2)

        if args.dry_run:
            result = {
                "test_id": args.test_id,
                "platform": "FC",
                "status": "DRY_RUN",
                "message": "FreeCAD adapter payload created successfully.",
                "payload_json": payload_path,
                "result_json_expected": result_path,
            }
            print(json.dumps(result, indent=2))
            return 0

        freecadcmd_exe = normalize_path(freecad_cfg.get("freecadcmd_exe"), config_dir)
        harness = normalize_path(freecad_cfg.get("python_harness"), config_dir)
        if not freecadcmd_exe or not os.path.isfile(freecadcmd_exe):
            print(json.dumps({
                "test_id": args.test_id,
                "platform": "FC",
                "status": "ERROR",
                "message": f"FreeCADCmd executable not found: {freecadcmd_exe}",
                "payload_json": payload_path,
            }, indent=2))
            return 2
        if not harness or not os.path.isfile(harness):
            print(json.dumps({
                "test_id": args.test_id,
                "platform": "FC",
                "status": "ERROR",
                "message": f"FreeCAD harness not found: {harness}",
                "payload_json": payload_path,
            }, indent=2))
            return 2

        timeout = args.runtime_cap_seconds if args.runtime_cap_seconds > 0 else 300
        returncode, stdout, stderr = launch_freecad_console(freecadcmd_exe, harness, payload_path, timeout=timeout)

        # Harness should write result JSON; if not, provide best-effort fallback.
        if os.path.isfile(result_path):
            try:
                with open(result_path, "r", encoding="utf-8") as f:
                    print(json.dumps(json.load(f), indent=2))
                    return 0 if returncode == 0 else returncode
            except (OSError, ValueError, TypeError, json.JSONDecodeError):
                pass

        print(json.dumps({
            "test_id": args.test_id,
            "platform": "FC",
            "status": "ERROR" if returncode else "UNKNOWN",
            "message": "Harness did not produce result JSON.",
            "payload_json": payload_path,
            "stdout": stdout[-4000:],
            "stderr": stderr[-4000:],
        }, indent=2))
        return returncode if returncode else 3


if __name__ == "__main__":
    raise SystemExit(main())
```

### PDFVectorImporter/adapters/freecad_harness.py

- Path: `PDFVectorImporter/adapters/freecad_harness.py`
- Size: `15.16 KB`
- Modified: `2026-04-03 16:34:22`

```python
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
```

### PDFVectorImporter/adapters/librecad_adapter.py

- Path: `PDFVectorImporter/adapters/librecad_adapter.py`
- Size: `8.00 KB`
- Modified: `2026-04-03 18:40:53`

```python
#!/usr/bin/env python3
"""
LibreCAD adapter for PDF Vector Importer QA.

Runs the standalone LibreCAD PDF importer CLI (PDF -> DXF pipeline) and
classifies the run as PASS/FAIL/BLOCKED for the central QA workbook runner.
"""
from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
import tempfile
import time
from pathlib import Path
from typing import Optional


def load_json(path: Optional[str]) -> dict:
    if not path:
        return {}
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def normalize_path(value: Optional[str], base_dir: Optional[str] = None) -> Optional[str]:
    if value is None:
        return None
    raw = os.path.expandvars(str(value))
    # Allow command-style executables like "python" without forcing path resolution.
    if ("/" not in raw and "\\" not in raw and not Path(raw).is_absolute()):
        return raw
    p = Path(raw).expanduser()
    if not p.is_absolute() and base_dir:
        p = Path(base_dir) / p
    return str(p.resolve())


def run_librecad_cli(
    python_exe: str,
    repo_dir: str,
    input_pdf: str,
    output_dxf: str,
    preset: str,
    page_range: str,
    summary_json: str,
    timeout_seconds: int,
    no_text: bool = False,
    no_images: bool = False,
    no_arcs: bool = False,
) -> subprocess.CompletedProcess:
    cmd = [
        python_exe,
        "-m",
        "librecad_pdf_importer.cli",
        input_pdf,
        "--out",
        output_dxf,
        "--preset",
        preset,
        "--pages",
        page_range,
        "--json",
        summary_json,
    ]
    if no_text:
        cmd.append("--no-text")
    if no_images:
        cmd.append("--no-images")
    if no_arcs:
        cmd.append("--no-arcs")

    return subprocess.run(
        cmd,
        cwd=repo_dir,
        capture_output=True,
        text=True,
        timeout=timeout_seconds,
        check=False,
    )


def classify_result(summary: dict, min_entities: int, max_seconds: int, runtime_seconds: float) -> tuple[str, str]:
    export = summary.get("export", {})
    entity_count = int(export.get("entity_count", 0))
    output_path = export.get("output_path")
    if not output_path:
        return "FAIL", "Exporter did not report an output path."
    if entity_count < min_entities:
        return "FAIL", f"Entity count {entity_count} below required minimum {min_entities}."
    if max_seconds > 0 and runtime_seconds > max_seconds:
        return "FAIL", f"Runtime {runtime_seconds:.2f}s exceeded cap {max_seconds}s."
    return "PASS", f"Exported {entity_count} entities."


def main() -> int:
    parser = argparse.ArgumentParser(description="LibreCAD adapter for PDF importer QA.")
    parser.add_argument("--config", help="Path to qa_config.json", required=False)
    parser.add_argument("--test-id", required=True)
    parser.add_argument("--input", required=True, help="Input PDF path")
    parser.add_argument("--preset", default="technical")
    parser.add_argument("--page-range", default="1")
    parser.add_argument("--min-entities", type=int, default=1)
    parser.add_argument("--runtime-cap-seconds", type=int, default=0)
    parser.add_argument("--no-text", action="store_true")
    parser.add_argument("--no-images", action="store_true")
    parser.add_argument("--no-arcs", action="store_true")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    cfg = load_json(args.config)
    config_dir = str(Path(args.config).expanduser().resolve().parent) if args.config else os.getcwd()
    librecad_cfg = cfg.get("librecad", {})

    repo_dir = normalize_path(librecad_cfg.get("repo_dir"), config_dir)
    python_exe = normalize_path(librecad_cfg.get("python_exe"), config_dir) or sys.executable
    input_pdf = normalize_path(args.input, config_dir)
    timeout_seconds = int(librecad_cfg.get("timeout_seconds", 1800))

    if args.dry_run:
        print(
            json.dumps(
                {
                    "test_id": args.test_id,
                    "platform": "LC",
                    "status": "DRY_RUN",
                    "message": "LibreCAD adapter config parsed successfully.",
                    "repo_dir": repo_dir,
                    "python_exe": python_exe,
                },
                indent=2,
            )
        )
        return 0

    if not repo_dir or not os.path.isdir(repo_dir):
        print(
            json.dumps(
                {
                    "test_id": args.test_id,
                    "platform": "LC",
                    "status": "ERROR",
                    "message": f"LibreCAD repo_dir not found: {repo_dir}",
                },
                indent=2,
            )
        )
        return 2
    if not input_pdf or not os.path.isfile(input_pdf):
        print(
            json.dumps(
                {
                    "test_id": args.test_id,
                    "platform": "LC",
                    "status": "ERROR",
                    "message": f"Input PDF not found: {input_pdf}",
                },
                indent=2,
            )
        )
        return 2

    with tempfile.TemporaryDirectory(prefix="bc_pdf_lc_qa_") as td:
        summary_path = os.path.join(td, f"{args.test_id}_lc_summary.json")
        output_dxf = os.path.join(td, f"{args.test_id}.dxf")

        started = time.perf_counter()
        try:
            proc = run_librecad_cli(
                python_exe=python_exe,
                repo_dir=repo_dir,
                input_pdf=input_pdf,
                output_dxf=output_dxf,
                preset=args.preset,
                page_range=args.page_range,
                summary_json=summary_path,
                timeout_seconds=timeout_seconds,
                no_text=args.no_text,
                no_images=args.no_images,
                no_arcs=args.no_arcs,
            )
        except subprocess.TimeoutExpired:
            print(
                json.dumps(
                    {
                        "test_id": args.test_id,
                        "platform": "LC",
                        "status": "FAIL",
                        "message": f"Timed out after {timeout_seconds}s.",
                    },
                    indent=2,
                )
            )
            return 1

        runtime_seconds = round(time.perf_counter() - started, 3)
        if proc.returncode != 0:
            print(
                json.dumps(
                    {
                        "test_id": args.test_id,
                        "platform": "LC",
                        "status": "FAIL",
                        "message": f"CLI exited {proc.returncode}",
                        "stdout": (proc.stdout or "")[-2000:],
                        "stderr": (proc.stderr or "")[-2000:],
                    },
                    indent=2,
                )
            )
            return proc.returncode

        if not os.path.isfile(summary_path):
            print(
                json.dumps(
                    {
                        "test_id": args.test_id,
                        "platform": "LC",
                        "status": "FAIL",
                        "message": "CLI did not produce summary JSON.",
                        "stdout": (proc.stdout or "")[-2000:],
                        "stderr": (proc.stderr or "")[-2000:],
                    },
                    indent=2,
                )
            )
            return 1

        with open(summary_path, "r", encoding="utf-8") as f:
            summary = json.load(f)

        status, message = classify_result(summary, args.min_entities, args.runtime_cap_seconds, runtime_seconds)
        print(
            json.dumps(
                {
                    "test_id": args.test_id,
                    "platform": "LC",
                    "status": status,
                    "message": message,
                    "runtime_seconds": runtime_seconds,
                    "summary": summary,
                },
                indent=2,
            )
        )
        return 0 if status == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
```

### PDFVectorImporter/adapters/sketchup_adapter.py

- Path: `PDFVectorImporter/adapters/sketchup_adapter.py`
- Size: `10.55 KB`
- Modified: `2026-04-02 17:26:28`

```python
#!/usr/bin/env python3
"""
SketchUp adapter for PDF Vector Importer QA.

Purpose:
- Provides a stable command-line interface for the external test runner.
- Prepares a JSON payload for a Ruby-side harness script.
- Optionally launches SketchUp with a test script.
- Supports dry-run mode for environments where SketchUp cannot be launched.

This adapter does NOT require changes to the main extension. It assumes you will
add a small Ruby harness that:
1) reads the payload file,
2) performs the import,
3) writes a result JSON file.

Typical use:
python adapters/sketchup_adapter.py --config qa_config.json --test-id SU-OCG-001 --input "C:/tests/1071 - Rev 0.pdf" --preset Full --dry-run
"""
from __future__ import annotations

from typing import Optional, Tuple

import argparse
import json
import os
import subprocess
import tempfile
import time
from datetime import datetime, timezone
from pathlib import Path


def load_json(path: Optional[str]) -> dict:
    if not path:
        return {}
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def normalize_path(value: Optional[str], base_dir: Optional[str] = None) -> Optional[str]:
    if value is None:
        return None
    raw = os.path.expandvars(str(value))
    p = Path(raw).expanduser()
    if not p.is_absolute() and base_dir:
        p = Path(base_dir) / p
    return str(p.resolve())


def build_payload(args: argparse.Namespace, cfg: dict, result_path: str, config_dir: Optional[str]) -> dict:
    sketchup_cfg = cfg.get("sketchup", {})
    return {
        "adapter": "sketchup",
        "timestamp_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "test_id": args.test_id,
        "platform": "SU",
        "input_pdf": normalize_path(args.input, config_dir),
        "preset": args.preset,
        "page_range": args.page_range,
        "output_dir": normalize_path(args.output_dir, config_dir) if args.output_dir else None,
        "result_json": result_path,
        "extension_root": normalize_path(sketchup_cfg.get("extension_root"), config_dir),
        "plugins_dir": normalize_path(sketchup_cfg.get("plugins_dir"), config_dir),
        "ruby_harness": normalize_path(sketchup_cfg.get("ruby_harness"), config_dir),
        "expected": {
            "layers_min_populated": args.layers_min_populated,
            "runtime_cap_seconds": args.runtime_cap_seconds,
        },
        "notes": args.notes or "",
    }


def write_bootstrap_plugin(plugins_dir: str, harness_path: str) -> str:
    ts = datetime.now(timezone.utc).strftime("%Y%m%d%H%M%S")
    bootstrap_path = os.path.join(plugins_dir, f"zz_bc_pdf_qa_bootstrap_{ts}.rb")
    ruby = """# Auto-generated by sketchup_adapter.py
begin
  payload = ENV["BC_PDF_QA_PAYLOAD"].to_s
  harness = ENV["BC_PDF_QA_HARNESS"].to_s
  if !payload.strip.empty? && !harness.strip.empty? && File.file?(harness)
    load harness
  end
rescue Exception => e
  begin
    require "json"
    msg = begin
      ("Bootstrap error: #{e.class}: #{e.message}").to_s
        .encode("UTF-8", "binary", invalid: :replace, undef: :replace, replace: "?")
    rescue Exception
      "Bootstrap error: #{e.class}"
    end
    payload_path = ENV["BC_PDF_QA_PAYLOAD"].to_s
    if !payload_path.strip.empty? && File.file?(payload_path)
      payload_data = JSON.parse(File.read(payload_path)) rescue {}
      result_path = payload_data["result_json"].to_s
      unless result_path.strip.empty?
        File.open(result_path, "w") do |f|
          f.write(JSON.pretty_generate({
            "platform" => "SU",
            "status" => "FAIL",
            "message" => msg
          }))
        end
      end
    end
  rescue Exception
  end
end
"""
    with open(bootstrap_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ruby)
    return bootstrap_path


def cleanup_bootstrap_plugin(path: Optional[str]) -> None:
    if not path:
        return
    try:
        if os.path.isfile(path):
            os.remove(path)
    except OSError:
        pass


def try_launch_sketchup(sketchup_exe: Optional[str], ruby_harness: Optional[str], payload_path: str,
                        config_dir: Optional[str], plugins_dir: Optional[str]) -> Tuple[bool, str, Optional[str]]:
    """
    Best-effort launcher.

    SketchUp does not provide a great official headless CLI for automated plugin
    testing, so this function is intentionally conservative:
    - If executable and harness are provided, launch SketchUp and pass the harness path.
    - The Ruby harness should know to read the payload JSON and write the result JSON.
    """
    if not sketchup_exe:
        return False, "No SketchUp executable configured.", None
    if not ruby_harness:
        return False, "No Ruby harness configured.", None

    exe = normalize_path(sketchup_exe, config_dir)
    harness = normalize_path(ruby_harness, config_dir)
    plugin_root = normalize_path(plugins_dir, config_dir) if plugins_dir else None
    if not os.path.isfile(exe):
        return False, f"SketchUp executable not found: {exe}", None
    if not os.path.isfile(harness):
        return False, f"Ruby harness not found: {harness}", None
    if not plugin_root or not os.path.isdir(plugin_root):
        return False, f"SketchUp plugins_dir not found: {plugin_root}", None

    env = os.environ.copy()
    env["BC_PDF_QA_PAYLOAD"] = payload_path
    env["BC_PDF_QA_HARNESS"] = harness

    bootstrap_path = None
    try:
        bootstrap_path = write_bootstrap_plugin(plugin_root, harness)
    except (OSError, ValueError, TypeError) as exc:
        return False, f"Failed to create bootstrap plugin: {exc}", None

    # Some SketchUp builds accept a Ruby startup script through a file association
    # or command-line file open flow; many do not. We therefore launch SketchUp and
    # let the Ruby harness/bootstrap in Plugins handle the payload.
    try:
        # SketchUp supports Ruby startup scripts on many builds. If unsupported,
        # SketchUp still launches and plugin-side bootstrap can read BC_PDF_QA_PAYLOAD.
        subprocess.Popen([exe, "-RubyStartup", harness], env=env)
        return True, "SketchUp launched. Waiting for Ruby harness to write result JSON.", bootstrap_path
    except (OSError, ValueError, TypeError) as exc:
        cleanup_bootstrap_plugin(bootstrap_path)
        return False, f"Launch failed: {exc}", None


def wait_for_result(result_path: str, timeout_seconds: int) -> Optional[dict]:
    deadline = time.time() + timeout_seconds
    while time.time() < deadline:
        if os.path.isfile(result_path):
            try:
                with open(result_path, "r", encoding="utf-8") as f:
                    return json.load(f)
            except (OSError, ValueError, TypeError, json.JSONDecodeError):
                pass
        time.sleep(1.0)
    return None


def main() -> int:
    parser = argparse.ArgumentParser(description="SketchUp adapter for PDF Vector Importer QA.")
    parser.add_argument("--config", help="Path to qa_config.json", required=False)
    parser.add_argument("--test-id", required=True, help="Test ID, e.g. SU-OCG-001")
    parser.add_argument("--input", required=True, help="Input PDF path")
    parser.add_argument("--preset", default="Full", help="Import preset name")
    parser.add_argument("--page-range", default="1", help="Page range string")
    parser.add_argument("--output-dir", help="Optional output directory")
    parser.add_argument("--notes", help="Optional notes")
    parser.add_argument("--layers-min-populated", type=int, default=0)
    parser.add_argument("--runtime-cap-seconds", type=int, default=0)
    parser.add_argument("--timeout-seconds", type=int, default=180)
    parser.add_argument("--dry-run", action="store_true", help="Do not launch SketchUp; emit a starter result only.")
    args = parser.parse_args()

    cfg = load_json(args.config)
    config_dir = str(Path(args.config).expanduser().resolve().parent) if args.config else os.getcwd()
    sketchup_cfg = cfg.get("sketchup", {})

    with tempfile.TemporaryDirectory(prefix="bc_pdf_su_qa_") as td:
        payload_path = os.path.join(td, f"{args.test_id}_payload.json")
        result_path = os.path.join(td, f"{args.test_id}_result.json")

        payload = build_payload(args, cfg, result_path, config_dir)
        with open(payload_path, "w", encoding="utf-8") as f:
            json.dump(payload, f, indent=2)

        if args.dry_run:
            result = {
                "test_id": args.test_id,
                "platform": "SU",
                "status": "DRY_RUN",
                "message": "SketchUp adapter payload created successfully.",
                "payload_json": payload_path,
                "result_json_expected": result_path,
            }
            print(json.dumps(result, indent=2))
            return 0

        if sketchup_cfg.get("automation_supported") is False:
            print(json.dumps({
                "test_id": args.test_id,
                "platform": "SU",
                "status": "BLOCKED",
                "message": "SketchUp automation disabled in config (automation_supported=false).",
                "payload_json": payload_path,
            }, indent=2))
            return 0

        bootstrap_path = None
        try:
            launched, message, bootstrap_path = try_launch_sketchup(
                sketchup_cfg.get("exe"),
                sketchup_cfg.get("ruby_harness"),
                payload_path,
                config_dir,
                sketchup_cfg.get("plugins_dir"),
            )
            if not launched:
                print(json.dumps({
                    "test_id": args.test_id,
                    "platform": "SU",
                    "status": "ERROR",
                    "message": message,
                    "payload_json": payload_path,
                }, indent=2))
                return 2

            result = wait_for_result(result_path, args.timeout_seconds)
            if result is None:
                print(json.dumps({
                    "test_id": args.test_id,
                    "platform": "SU",
                    "status": "TIMEOUT",
                    "message": message,
                    "payload_json": payload_path,
                    "result_json_expected": result_path,
                }, indent=2))
                return 3

            print(json.dumps(result, indent=2))
            return 0
        finally:
            cleanup_bootstrap_plugin(bootstrap_path)


if __name__ == "__main__":
    raise SystemExit(main())
```

### PDFVectorImporter/adapters/sketchup_harness.rb

- Path: `PDFVectorImporter/adapters/sketchup_harness.rb`
- Size: `6.20 KB`
- Modified: `2026-03-29 21:21:10`

```ruby
# frozen_string_literal: false
# BlueCollar Systems — BUILT. NOT BOUGHT.
#
# SketchUp QA harness for PDF Vector Importer.
#
# Runs inside SketchUp (for example via -RubyStartup) and:
# 1) reads payload from ENV["BC_PDF_QA_PAYLOAD"]
# 2) loads extension entry points
# 3) runs pipeline import with selected preset/pages
# 4) writes JSON result to payload["result_json"]

require "json"
require "time"

module BCPDFQA
  module SketchUpHarness
    module_function

    def run
      payload_path = ENV["BC_PDF_QA_PAYLOAD"].to_s
      raise "BC_PDF_QA_PAYLOAD not set" if payload_path.strip.empty?
      payload = JSON.parse(File.read(payload_path))
      result_path = payload["result_json"].to_s
      raise "result_json missing in payload" if result_path.strip.empty?

      start_time = Time.now
      result = {
        "test_id" => payload["test_id"],
        "platform" => "SU",
        "status" => "ERROR",
        "message" => "",
        "started_at" => start_time.utc.iso8601
      }

      begin
        loader = require_extension(payload)
        importer = BlueCollarSystems::PDFVectorImporter

        model = Sketchup.active_model
        raise "No active SketchUp model" unless model

        before = model_entity_counts(model)
        before_layers = safe_layer_count(model)

        opts = build_opts(payload, importer)
        stats = importer.run_pipeline(model, payload["input_pdf"], opts)
        raise "run_pipeline returned nil" if stats.nil?

        after = model_entity_counts(model)
        after_layers = safe_layer_count(model)

        result["status"] = "PASS"
        result["message"] = "Import completed."
        result["loader"] = loader
        result["input_pdf"] = payload["input_pdf"]
        result["preset"] = payload["preset"]
        result["page_range"] = payload["page_range"]
        result["pipeline_stats"] = stats
        result["model_counts_before"] = before
        result["model_counts_after"] = after
        result["model_delta"] = hash_delta(after, before)
        result["layers_before"] = before_layers
        result["layers_after"] = after_layers
        result["layers_delta"] = after_layers - before_layers
      rescue => e
        result["status"] = "FAIL"
        result["message"] = "#{e.class}: #{e.message}"
        result["backtrace"] = (e.backtrace || [])[0, 25]
      ensure
        finish = Time.now
        result["finished_at"] = finish.utc.iso8601
        result["runtime_seconds"] = (finish - start_time).round(3)
        safe_result = utf8_safe(result)
        File.open(result_path, "w") { |f| f.write(JSON.pretty_generate(safe_result)) }
      end
    end

    def utf8_safe(obj)
      case obj
      when String
        begin
          obj.encode("UTF-8", "binary", invalid: :replace, undef: :replace, replace: "?")
        rescue StandardError
          obj.to_s
        end
      when Array
        obj.map { |v| utf8_safe(v) }
      when Hash
        out = {}
        obj.each { |k, v| out[utf8_safe(k)] = utf8_safe(v) }
        out
      else
        obj
      end
    end

    def build_opts(payload, importer)
      presets = importer::ImportDialog::PRESETS
      preset_name = payload["preset"].to_s.strip
      preset_name = "Full" if preset_name.empty?
      preset = presets[preset_name] || presets["Full"] || {}

      raw = {}
      preset.each { |k, v| raw[k] = v }
      raw[:pages] = payload["page_range"].to_s.strip.empty? ? "1" : payload["page_range"].to_s
      raw[:scale] = "1.0" if raw[:scale].to_s.strip.empty?

      importer::ImportDialog.send(:build_opts, raw)
    end

    def require_extension(payload)
      candidates = []
      ext_root = resolve_path(payload["extension_root"])
      plugins_dir = resolve_path(payload["plugins_dir"])

      if ext_root && !ext_root.empty?
        candidates << File.join(ext_root, "main")
        candidates << File.join(ext_root, "main.rb")
        candidates << File.join(File.dirname(ext_root), "bc_pdf_vector_importer.rb")
      end
      if plugins_dir && !plugins_dir.empty?
        candidates << File.join(plugins_dir, "bc_pdf_vector_importer", "main")
        candidates << File.join(plugins_dir, "bc_pdf_vector_importer", "main.rb")
        candidates << File.join(plugins_dir, "bc_pdf_vector_importer.rb")
      end

      candidates.each do |path|
        begin
          require path
          return path
        rescue LoadError
          next
        rescue StandardError
          next
        end
      end

      if defined?(BlueCollarSystems::PDFVectorImporter) &&
         BlueCollarSystems::PDFVectorImporter.respond_to?(:run_pipeline)
        return "already_loaded"
      end

      raise "Could not load PDF Vector Importer from extension_root/plugins_dir."
    end

    def resolve_path(value)
      return nil if value.nil?
      s = value.to_s
      return nil if s.strip.empty?
      s = s.gsub(/%([^%]+)%/) { |m| ENV[$1] || m }
      File.expand_path(s)
    rescue
      value.to_s
    end

    def safe_layer_count(model)
      model.layers.length
    rescue
      0
    end

    def model_entity_counts(model)
      acc = {
        "edges" => 0,
        "faces" => 0,
        "groups" => 0,
        "component_instances" => 0,
        "texts" => 0,
        "images" => 0
      }
      count_entities(model.entities, acc, {})
      acc
    end

    def count_entities(entities, acc, seen_defs)
      entities.each do |e|
        if e.is_a?(Sketchup::Edge)
          acc["edges"] += 1
        elsif e.is_a?(Sketchup::Face)
          acc["faces"] += 1
        elsif defined?(Sketchup::Text) && e.is_a?(Sketchup::Text)
          acc["texts"] += 1
        elsif defined?(Sketchup::Image) && e.is_a?(Sketchup::Image)
          acc["images"] += 1
        elsif e.is_a?(Sketchup::Group)
          acc["groups"] += 1
          count_entities(e.entities, acc, seen_defs)
        elsif e.is_a?(Sketchup::ComponentInstance)
          acc["component_instances"] += 1
          d = e.definition
          next if d.nil?
          did = d.object_id
          next if seen_defs[did]
          seen_defs[did] = true
          count_entities(d.entities, acc, seen_defs)
        end
      end
    end

    def hash_delta(after, before)
      out = {}
      after.each do |k, v|
        out[k] = v.to_i - before[k].to_i
      end
      out
    end
  end
end

BCPDFQA::SketchUpHarness.run
```

### PDFVectorImporter/compare_feature_matrix.py

- Path: `PDFVectorImporter/compare_feature_matrix.py`
- Size: `8.38 KB`
- Modified: `2026-04-04 03:49:30`

```python
#!/usr/bin/env python3
"""
Cross-repository feature matrix generator.

Compares SketchUp, FreeCAD, Blender, LibreCAD importers plus the steel app,
then writes machine-readable JSON and a Markdown matrix.
"""
from __future__ import annotations

import argparse
import json
import re
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Dict, Iterable, List, Set


REPO_KEYS = ("SU", "FC", "BL", "LC", "APP")


@dataclass(frozen=True)
class Feature:
    key: str
    label: str
    pattern: str
    applies_to: Set[str]


FEATURES: List[Feature] = [
    Feature("vector_primitives", "Vector primitive extraction", r"\b(polyline|closed_loop|circle|arc|primitive)\b", {"SU", "FC", "BL", "LC"}),
    Feature("arc_rebuild", "Arc/circle reconstruction", r"\b(arc_fit|circle fit|kasa|rebuild arcs|arc_mode)\b", {"SU", "FC", "BL", "LC"}),
    Feature("dash_mapping", "Dash pattern preservation", r"\b(dash_pattern|map_dashes|linetype)\b", {"SU", "FC", "BL", "LC"}),
    Feature("text_labels", "Text as labels", r"\btext_mode\b.{0,40}\blabels\b|\blabels\b.{0,40}\btext_mode\b", {"SU", "FC", "BL", "LC"}),
    Feature("text_geometry", "Text as geometry", r"\btext_mode\b.{0,40}\bgeometry\b|\bgeometry\b.{0,40}\btext_mode\b", {"SU", "FC", "BL", "LC"}),
    Feature("strict_text", "Strict text fidelity mode", r"\bstrict_text_fidelity\b|strict glyph fidelity", {"SU", "FC", "BL", "LC"}),
    Feature("embedded_images", "Embedded image extraction", r"\b(get_images|insert_image|import_images|image extraction)\b", {"SU", "FC", "BL", "LC"}),
    Feature("raster_only", "Raster-only mode", r"\b(raster_only|Raster Only|import_mode.{0,30}raster)\b", {"SU", "FC", "BL", "LC"}),
    Feature("hybrid_mode", "Hybrid raster+vector mode", r"\b(hybrid|raster_vector|Raster \+ Vectors)\b", {"SU", "FC", "BL", "LC"}),
    Feature("hatch_modes", "Hatch handling modes", r"\b(hatch_mode|hatching)\b", {"SU", "FC", "BL", "LC"}),
    Feature("ocg_layers", "OCG/layer mapping", r"\b(OCG|optional content group|layer_name)\b", {"SU", "FC", "BL", "LC"}),
    Feature("grouping_modes", "Advanced grouping modes", r"\b(grouping_mode|Nested: page|nested_page_)\b", {"SU", "FC", "BL", "LC"}),
    Feature("lineweight_modes", "Lineweight handling modes", r"\b(lineweight_mode|lineweight)\b", {"SU", "FC", "BL", "LC"}),
    Feature("doc_profiling", "Document profiling/classification", r"\b(document_profiler|profile_page|primary_type)\b", {"SU", "FC", "BL", "LC"}),
    Feature("scale_reference", "Scale by reference tooling", r"\b(Scale by Reference|scale tool|reference_real_mm|PDFScaleTool)\b", {"SU", "FC", "BL", "LC"}),
    Feature("cli_surface", "CLI surface", r"\b(argparse|cli\.py|pdf2dxf\.py)\b", {"SU", "FC", "BL", "LC"}),
    Feature("gui_surface", "GUI surface", r"\b(HtmlDialog|QDialog|bpy\.types\.Operator|--gui|Tkinter)\b", {"SU", "FC", "BL", "LC"}),
    Feature("batch_import", "Batch import workflows", r"\b(Batch Import|batch import|BatchImportCommand)\b", {"SU", "FC", "BL", "LC"}),
    Feature("qa_automation", "Automated QA harness", r"\b(run_pdf_vector_importer_tests|qa_config|pytest|smoke_test|qa_smoke)\b", {"SU", "FC", "BL", "LC"}),
    Feature("all_pages_default", "Default imports all pages", r"spec is None:\s*return list\(range\(1,\s*page_count \+ 1\)\)", {"BL", "LC"}),
    Feature("app_aisc", "AISC dataset integration", r"\bAISC\b", {"APP"}),
    Feature("app_measurement_engine", "Measurement/unit parsing engine", r"\b(length_parser|1/16|unit conversions|fractional)\b", {"APP"}),
    Feature("app_svg_blueprints", "SVG blueprint rendering", r"\b(SVG|flutter_svg|shape_image_map)\b", {"APP"}),
]


def iter_files(root: Path) -> Iterable[Path]:
    if not root.exists():
        return []

    if root.name == "1SU-PDFimporter":
        globs = ["README.md", "test/*.rb", "extracted/sketchup_ext/**/*.rb"]
    elif root.name == "1FC-PDFimporter":
        globs = ["README.md", "PDFVectorImporter/**/*.py", "PDFVectorImporter/**/*.json", "PDFVectorImporter/**/*.rb", "tests/**/*.py"]
    elif root.name == "1BL-PDFimporter":
        globs = ["README.md", "blender_pdf_vector_importer/**/*.py", "pdf_vector_importer/**/*.py", "tests/**/*.py"]
    elif root.name == "1LC-PDFimporter":
        globs = ["README.md", "librecad_pdf_importer/**/*.py", "*.py", "tests/**/*.py"]
    else:
        globs = ["README.md", "lib/**/*.dart", "docs/**/*"]

    seen: Set[Path] = set()
    for pattern in globs:
        for p in root.glob(pattern):
            if p.is_file() and p not in seen:
                seen.add(p)
                yield p


def load_repo_text(root: Path, max_chars_per_file: int = 200_000) -> str:
    parts: List[str] = []
    for path in iter_files(root):
        try:
            text = path.read_text(encoding="utf-8", errors="ignore")
        except OSError:
            continue
        if len(text) > max_chars_per_file:
            text = text[:max_chars_per_file]
        parts.append(f"\n\n# FILE: {path}\n{text}")
    return "\n".join(parts)


def yes_no_na(value: str) -> str:
    if value == "yes":
        return "Yes"
    if value == "no":
        return "No"
    return "N/A"


def main() -> int:
    parser = argparse.ArgumentParser(description="Generate a cross-repo feature matrix report.")
    parser.add_argument("--su", required=True, help="SketchUp importer repo path")
    parser.add_argument("--fc", required=True, help="FreeCAD importer repo path")
    parser.add_argument("--bl", required=True, help="Blender importer repo path")
    parser.add_argument("--lc", required=True, help="LibreCAD importer repo path")
    parser.add_argument("--app", required=True, help="Structural steel app repo path")
    parser.add_argument("--outdir", required=True, help="Directory to write reports")
    args = parser.parse_args()

    roots: Dict[str, Path] = {
        "SU": Path(args.su).expanduser().resolve(),
        "FC": Path(args.fc).expanduser().resolve(),
        "BL": Path(args.bl).expanduser().resolve(),
        "LC": Path(args.lc).expanduser().resolve(),
        "APP": Path(args.app).expanduser().resolve(),
    }

    blobs = {key: load_repo_text(path) for key, path in roots.items()}

    rows = []
    summary = {k: {"applicable": 0, "yes": 0, "no": 0} for k in REPO_KEYS}
    for feature in FEATURES:
        row = {"key": feature.key, "label": feature.label, "status": {}}
        rx = re.compile(feature.pattern, flags=re.IGNORECASE | re.DOTALL)
        for repo in REPO_KEYS:
            if repo not in feature.applies_to:
                row["status"][repo] = "na"
                continue
            hit = bool(rx.search(blobs[repo]))
            row["status"][repo] = "yes" if hit else "no"
            summary[repo]["applicable"] += 1
            if hit:
                summary[repo]["yes"] += 1
            else:
                summary[repo]["no"] += 1
        rows.append(row)

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    outdir = Path(args.outdir).expanduser().resolve()
    outdir.mkdir(parents=True, exist_ok=True)

    json_payload = {
        "generated_at_local": timestamp,
        "repos": {k: str(v) for k, v in roots.items()},
        "summary": summary,
        "features": rows,
    }
    json_path = outdir / "feature_matrix.json"
    json_path.write_text(json.dumps(json_payload, indent=2), encoding="utf-8")

    md_lines = [
        "# Cross-Repo Feature Matrix",
        "",
        f"Generated: {timestamp}",
        "",
        "| Feature | SU | FC | BL | LC | App |",
        "|---|---|---|---|---|---|",
    ]
    for row in rows:
        s = row["status"]
        md_lines.append(
            f"| {row['label']} | {yes_no_na(s['SU'])} | {yes_no_na(s['FC'])} | {yes_no_na(s['BL'])} | {yes_no_na(s['LC'])} | {yes_no_na(s['APP'])} |"
        )

    md_lines.extend(
        [
            "",
            "## Coverage Summary",
            "",
            "| Repo | Applicable | Yes | No | Coverage |",
            "|---|---:|---:|---:|---:|",
        ]
    )
    for repo in REPO_KEYS:
        applicable = max(1, summary[repo]["applicable"])
        coverage = 100.0 * float(summary[repo]["yes"]) / float(applicable)
        md_lines.append(
            f"| {repo} | {summary[repo]['applicable']} | {summary[repo]['yes']} | {summary[repo]['no']} | {coverage:.1f}% |"
        )

    md_path = outdir / "feature_matrix.md"
    md_path.write_text("\n".join(md_lines), encoding="utf-8")

    print(json.dumps({"json": str(json_path), "markdown": str(md_path)}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
```

### PDFVectorImporter/fc_check_fitz.py

- Path: `PDFVectorImporter/fc_check_fitz.py`
- Size: `126.00 B`
- Modified: `2026-03-23 16:16:52`

```python
import importlib.util; import sys; m=importlib.util.find_spec('fitz'); print('FITZ_SPEC', bool(m)); print('PY', sys.version)
```

### PDFVectorImporter/fc_smoke_payload.json

- Path: `PDFVectorImporter/fc_smoke_payload.json`
- Size: `463.00 B`
- Modified: `2026-03-23 16:42:09`

```json
{
  "test_id": "FC-MANUAL-001",
  "platform": "FC",
  "input_pdf": "C:/Users/Rowdy Payton/Documents/Playground/tmp/master_bundle_20260317_2052/1071 - Rev 0.pdf",
  "preset": "Shop Drawing",
  "page_range": "1",
  "result_json": "C:/Users/Rowdy Payton/Documents/Playground/tmp/master_bundle_20260317_2052/fc_smoke_result.json",
  "mod_dir": "C:/Users/Rowdy Payton/Documents/Playground/tmp/master_bundle_20260317_2052/_inspect_fc_v350/PDFVectorImporter"
}
```

### PDFVectorImporter/Init.py

- Path: `PDFVectorImporter/Init.py`
- Size: `592.00 B`
- Modified: `2026-03-23 16:42:08`

```python
# -*- coding: utf-8 -*-
# Init.py — FreeCAD module initialization (runs at startup, before GUI)
# PDF Vector Importer — BlueCollar Systems — BUILT. NOT BOUGHT.
#
# This registers .pdf as an importable file format so that:
#   - Drag-and-drop a PDF onto FreeCAD → auto-imports
#   - File → Open → select a .pdf → auto-imports
#   - File → Import → select a .pdf → auto-imports
#
# Like InitGui.py, FreeCAD exec()s this file — NO __file__, NO top-level functions.
import FreeCAD

FreeCAD.addImportType("PDF vector drawings (*.pdf)", "PDFImportHandler")



```

### PDFVectorImporter/InitGui.py

- Path: `PDFVectorImporter/InitGui.py`
- Size: `9.10 KB`
- Modified: `2026-03-28 13:49:15`

```python
# -*- coding: utf-8 -*-
# InitGui.py — FreeCAD workbench registration
# PDF Vector Importer — BlueCollar Systems — BUILT. NOT BOUGHT.
#
# FreeCAD exec()s this file in a restricted namespace.
# ALL logic must be inside the class or fully inline.
# NO module-level helper functions — they vanish from scope.
import os
import sys

import FreeCAD
import FreeCADGui


class PDFVectorImporterWorkbench(FreeCADGui.Workbench):

    MenuText = "PDF Vector Importer"
    ToolTip  = ("Import vector PDF drawings with arc detection, text, "
                "images, and SketchUp-style reference scaling.")

    def __init__(self):
        # Find workbench root — inline, no helper function
        base = ""
        for root in (FreeCAD.getUserAppDataDir(), FreeCAD.getResourceDir()):
            d = os.path.join(root, "Mod", "PDFVectorImporter")
            if os.path.isdir(d):
                base = d
                break
        icon = os.path.join(base, "resources", "ImportPDFVector.svg") if base else ""
        self.__class__.Icon = icon if os.path.isfile(icon) else ""

    def _prioritize_paths(self, paths):
        """Ensure local workbench paths win over stale/duplicate installs."""
        for p in (x for x in reversed(paths) if x):
            try:
                while p in sys.path:
                    sys.path.remove(p)
            except (AttributeError, ValueError):
                pass
            sys.path.insert(0, p)

    def _evict_stale_modules(self, base):
        """Drop already-imported modules that came from another install path."""
        stale_names = (
            "PDFImporterCmd",
            "PDFScaleTool",
            "PDFTools",
            "PDFImporterCore",
            "PDFImportHandler",
            "PDFVectorImporter.src.PDFImporterCmd",
            "PDFVectorImporter.src.PDFScaleTool",
            "PDFVectorImporter.src.PDFImporterCore",
        )
        for name in stale_names:
            mod = sys.modules.get(name)
            mod_path = str(getattr(mod, "__file__", "") or "")
            if mod and mod_path and not mod_path.startswith(base):
                try:
                    del sys.modules[name]
                except KeyError:
                    pass

    def Initialize(self):
        # Find workbench root again (Initialize runs in a different context)
        base = ""
        for root in (FreeCAD.getUserAppDataDir(), FreeCAD.getResourceDir()):
            d = os.path.join(root, "Mod", "PDFVectorImporter")
            if os.path.isdir(d):
                base = d
                break

        if not base:
            FreeCAD.Console.PrintError("PDFVectorImporter: cannot find workbench folder\n")
            return

        src = os.path.join(base, "src")
        lib = os.path.join(src, "lib")

        # Ensure paths are importable
        self._prioritize_paths([os.path.dirname(base), base, src])
        if os.path.isdir(lib):
            self._prioritize_paths([lib])
        self._evict_stale_modules(base)

        # Register commands — each in its own try/except
        try:
            from PDFImporterCmd import ImportPDFVectorCommand
            FreeCADGui.addCommand("ImportPDFVector", ImportPDFVectorCommand())
        except (ImportError, AttributeError, RuntimeError, ValueError, SyntaxError) as e:
            FreeCAD.Console.PrintError("PDF Import cmd: " + str(e) + "\n")

        try:
            from PDFScaleTool import ScaleByReferenceCommand, QuickScaleCommand
            FreeCADGui.addCommand("PDF_ScaleByReference", ScaleByReferenceCommand())
            FreeCADGui.addCommand("PDF_QuickScale", QuickScaleCommand())
        except (ImportError, AttributeError, RuntimeError, ValueError, SyntaxError) as e:
            FreeCAD.Console.PrintError("PDF Scale cmds: " + str(e) + "\n")

        try:
            from PDFTools import (
                CheckEnvironmentCommand,
                ImportViaConsoleCommand,
                BatchImportCommand,
                InstallPyMuPDFCommand,
            )
            FreeCADGui.addCommand("PDF_CheckEnv", CheckEnvironmentCommand())
            FreeCADGui.addCommand("PDF_ImportViaConsole", ImportViaConsoleCommand())
            FreeCADGui.addCommand("PDF_BatchImport", BatchImportCommand())
            FreeCADGui.addCommand("PDF_InstallPyMuPDF", InstallPyMuPDFCommand())
        except (ImportError, AttributeError, RuntimeError, ValueError, SyntaxError) as e:
            FreeCAD.Console.PrintError("PDF Utility cmds: " + str(e) + "\n")

        # Toolbars & menus
        import_cmds = ["ImportPDFVector"]
        scale_cmds  = ["PDF_ScaleByReference", "PDF_QuickScale"]
        try:
            self.appendToolbar("PDF Import", import_cmds + scale_cmds)
        except (AttributeError, RuntimeError):
            pass
        try:
            self.appendMenu("PDF Vector Importer",
                            import_cmds + scale_cmds)
        except (AttributeError, RuntimeError):
            pass

        FreeCAD.Console.PrintMessage(
            "PDF Vector Importer ready — BlueCollar Systems\n")

    def Activated(self):
        # Ensure paths every time (in case this is the first activation)
        base = ""
        for root in (FreeCAD.getUserAppDataDir(), FreeCAD.getResourceDir()):
            d = os.path.join(root, "Mod", "PDFVectorImporter")
            if os.path.isdir(d):
                base = d
                break
        if base:
            src = os.path.join(base, "src")
            lib = os.path.join(src, "lib")
            self._prioritize_paths([os.path.dirname(base), base, src])
            if os.path.isdir(lib):
                self._prioritize_paths([lib])
            self._evict_stale_modules(base)

        # Check for PyMuPDF
        has_fitz = False
        try:
            import fitz  # noqa: F401
            has_fitz = True
        except ImportError:
            pass

        if not has_fitz:
            self._offer_install(base)

    def _offer_install(self, base):
        try:
            from PySide6 import QtWidgets
        except ImportError:
            from PySide2 import QtWidgets

        reply = QtWidgets.QMessageBox.question(
            None,
            "PDF Vector Importer — First-Time Setup",
            "PyMuPDF (the PDF reading engine) needs to be installed.\n\n"
            "Install it now?  (~30 MB download, no admin needed)\n\n"
            "This only happens once.",
            QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
            QtWidgets.QMessageBox.Yes,
        )
        if reply != QtWidgets.QMessageBox.Yes:
            return

        import subprocess

        target = os.path.join(base, "src", "lib") if base else ""
        if not target:
            return
        os.makedirs(target, exist_ok=True)

        # Find real python.exe (sys.executable may be freecad.exe)
        py = sys.executable
        bindir = os.path.dirname(py)
        for name in ("python.exe", "python3.exe", "python"):
            candidate = os.path.join(bindir, name)
            if os.path.isfile(candidate):
                py = candidate
                break

        kw = {}
        if sys.platform == "win32":
            kw["creationflags"] = 0x08000000  # CREATE_NO_WINDOW

        FreeCAD.Console.PrintMessage("Installing PyMuPDF to " + target + "...\n")
        try:
            try:
                subprocess.check_call(
                    [py, "-m", "ensurepip", "--upgrade"],
                    timeout=120, **kw)
            except (subprocess.CalledProcessError, subprocess.TimeoutExpired, OSError):
                pass

            subprocess.check_call(
                [py, "-m", "pip", "install", "--upgrade",
                 "--only-binary", ":all:", "--target", target, "PyMuPDF"],
                timeout=300, **kw)

            if target not in sys.path:
                sys.path.insert(0, target)

            # Test if it loaded
            try:
                import fitz  # noqa: F401
                QtWidgets.QMessageBox.information(
                    None, "Ready to Go!",
                    "PyMuPDF installed!\n\nYou can now import PDFs.")
                FreeCAD.Console.PrintMessage("PyMuPDF installed and loaded.\n")
            except ImportError:
                QtWidgets.QMessageBox.information(
                    None, "Almost There",
                    "PyMuPDF installed to:\n" + target + "\n\n"
                    "Please restart FreeCAD to activate it.")

        except subprocess.CalledProcessError as e:
            FreeCAD.Console.PrintError("pip failed: " + str(e) + "\n")
            QtWidgets.QMessageBox.critical(
                None, "Install Failed",
                "Automatic install failed.\n\n"
                "Try manually in a terminal:\n"
                '  "' + py + '" -m pip install --target "' + target + '" PyMuPDF')
        except (subprocess.SubprocessError, OSError, RuntimeError, ValueError) as e:
            FreeCAD.Console.PrintError("Install error: " + str(e) + "\n")

    def GetClassName(self):
        return "Gui::PythonWorkbench"


FreeCADGui.addWorkbench(PDFVectorImporterWorkbench())

```

### PDFVectorImporter/package.xml

- Path: `PDFVectorImporter/package.xml`
- Size: `1.52 KB`
- Modified: `2026-04-04 04:18:12`

```xml
<?xml version="1.0" encoding="UTF-8" standalone="no" ?>
<package format="1" xmlns="https://wiki.freecad.org/Package_Metadata">
  <name>PDFVectorImporter</name>
  <description>Import PDF vector drawings as editable FreeCAD geometry with arc reconstruction, text, scaling, and steel feature detection.</description>
  <version>4.0.2</version>
  <date>2026-04-04</date>
  <maintainer email="support@bluecollar-systems.com">BlueCollar Systems</maintainer>
  <!-- AI Contributors: Claude & Claude Code (Anthropic), ChatGPT & Codex (OpenAI),
       Gemini (Google), Microsoft Copilot — collaborative AI development partners. -->
  <license file="LICENSE">MIT</license>
  <url type="repository" branch="main">https://github.com/BlueCollar-Systems/FC-PDFimporter</url>
  <url type="readme">https://github.com/BlueCollar-Systems/FC-PDFimporter/blob/main/README.md</url>
  <icon>resources/ImportPDFVector.svg</icon>

  <content>
    <workbench>
      <classname>PDFVectorImporterWorkbench</classname>
      <subdirectory>./</subdirectory>
      <file>InitGui.py</file>

      <!-- Python dependencies — Addon Manager will attempt pip install -->
      <depend>PyMuPDF</depend>

      <!-- FreeCAD version support -->
      <freecadmin>0.21</freecadmin>
      <freecadmax>1.99</freecadmax>
    </workbench>
  </content>

  <tag>PDF</tag>
  <tag>import</tag>
  <tag>vector</tag>
  <tag>CAD</tag>
  <tag>fabrication</tag>
  <tag>steel</tag>
  <tag>drawing</tag>
  <tag>arc reconstruction</tag>
  <tag>scale</tag>
</package>
```

### PDFVectorImporter/pdfcadcore/__init__.py

- Path: `PDFVectorImporter/pdfcadcore/__init__.py`
- Size: `936.00 B`
- Modified: `2026-04-04 04:22:17`

```python
# -*- coding: utf-8 -*-
# pdfcadcore — Shared PDF vector import core
# BlueCollar Systems — BUILT. NOT BOUGHT.
"""
Host-neutral PDF vector extraction, recognition, and cleanup.
Used by FreeCAD, Blender, and LibreCAD importers.
"""
__version__ = "1.0.0"

from .primitives import (
    Primitive as Primitive,
    NormalizedText as NormalizedText,
    PageData as PageData,
    ParsedDimension as ParsedDimension,
    Region as Region,
    PageProfile as PageProfile,
    RecognitionConfig as RecognitionConfig,
    next_id as next_id,
    reset_ids as reset_ids,
)
from .import_config import ImportConfig as ImportConfig, CLEANUP_PRESETS as CLEANUP_PRESETS
from .primitive_extractor import extract_page as extract_page
from .auto_mode import classify_page_content as classify_page_content
from .hatch_detector import tag_hatch_primitives as tag_hatch_primitives
from .geometry_cleanup import cleanup_primitives as cleanup_primitives
```

### PDFVectorImporter/pdfcadcore/auto_mode.py

- Path: `PDFVectorImporter/pdfcadcore/auto_mode.py`
- Size: `7.21 KB`
- Modified: `2026-04-04 03:41:49`

~~~python
# -*- coding: utf-8 -*-
# auto_mode.py -- Auto-mode detection heuristics for PDF content classification
# BlueCollar Systems -- BUILT. NOT BOUGHT.
"""
Classifies PDF page content to prevent garbage output on certain PDF types:
- Glyph floods (OCR-like PDFs with thousands of tiny vector glyphs)
- Fill-art floods (decorative/map PDFs with mostly fills)

Heuristics ported from the FreeCAD importer's _looks_like_vector_glyph_flood()
and _looks_like_fill_art_flood() functions.
"""
from __future__ import annotations

from typing import Any, Dict, List

# ── Glyph-flood thresholds ──────────────────────────────────────────
AUTO_GLYPH_DRAWING_THRESHOLD = 1500
AUTO_GLYPH_FILL_RATIO = 0.75
AUTO_GLYPH_TINY_RECT_RATIO = 0.45
AUTO_GLYPH_TEXT_BLOCK_THRESHOLD = 50
AUTO_GLYPH_WORD_THRESHOLD = 400
AUTO_GLYPH_STROKE_SPARSE_RATIO = 0.05

# ── Fill-art flood thresholds ───────────────────────────────────────
AUTO_FILL_DRAWING_THRESHOLD = 400
AUTO_FILL_HEAVY_RATIO = 0.60
AUTO_FILL_STROKE_MAX = 0.22
AUTO_FILL_PURE_RATIO = 0.95
AUTO_FILL_PURE_STROKE_MAX = 0.02
AUTO_FILL_PURE_MIN_GROUPS = 12
AUTO_FILL_PURE_MIN_ITEMS = 24
AUTO_FILL_PURE_LARGE_RECT_RATIO = 0.03


def classify_page_content(
    drawings: List[Dict[str, Any]],
    text_blocks_count: int = 0,
    text_words_count: int = 0,
) -> Dict[str, Any]:
    """Classify page content type from raw PyMuPDF drawings.

    Call this on the result of ``fitz_page.get_drawings()`` *before*
    primitive extraction to decide whether a page should be imported
    as vectors, skipped, or converted to raster.

    Parameters
    ----------
    drawings:
        Raw PyMuPDF drawing groups from ``page.get_drawings()``.
    text_blocks_count:
        Number of text blocks on the page (from ``page.get_text("blocks")``).
    text_words_count:
        Number of words on the page (from ``page.get_text("words")``).

    Returns
    -------
    dict
        ``type``  -- ``'vectors'`` | ``'glyph_flood'`` | ``'fill_art'``
                     | ``'raster_candidate'``
        ``reason`` -- human-readable explanation
        ``drawing_count`` -- total drawing groups
        ``stats`` -- detailed numeric statistics
    """
    if not drawings:
        return {
            "type": "raster_candidate",
            "reason": "No vector content",
            "drawing_count": 0,
            "stats": {},
        }

    total = len(drawings)

    # ── Compute per-drawing statistics ──────────────────────────────
    has_fill = 0
    has_stroke = 0
    fill_only = 0
    tiny_rects = 0

    for d in drawings:
        items = d.get("items", [])
        f = d.get("fill")
        s = d.get("color") or d.get("stroke")

        if f is not None:
            has_fill += 1
        if s is not None:
            has_stroke += 1
        if f is not None and s is None:
            fill_only += 1

        # Tiny rect detection: single 're' item with small bounds
        if len(items) == 1 and items[0][0] == "re":
            rect = d.get("rect")
            if rect is not None:
                # rect is a fitz.Rect or tuple (x0, y0, x1, y1)
                try:
                    if hasattr(rect, "width"):
                        w, h = rect.width, rect.height
                    else:
                        w = abs(rect[2] - rect[0])
                        h = abs(rect[3] - rect[1])
                    if w < 2.0 and h < 2.0:
                        tiny_rects += 1
                except (TypeError, IndexError):
                    tiny_rects += 1
            else:
                tiny_rects += 1

    fill_ratio = has_fill / total if total > 0 else 0
    stroke_ratio = has_stroke / total if total > 0 else 0
    fill_only_ratio = fill_only / total if total > 0 else 0
    tiny_rect_ratio = tiny_rects / total if total > 0 else 0

    stats = {
        "total": total,
        "has_fill": has_fill,
        "has_stroke": has_stroke,
        "fill_only": fill_only,
        "tiny_rects": tiny_rects,
        "fill_ratio": fill_ratio,
        "stroke_ratio": stroke_ratio,
        "fill_only_ratio": fill_only_ratio,
        "tiny_rect_ratio": tiny_rect_ratio,
    }

    # ── Glyph flood detection ──────────────────────────────────────
    if (
        total >= AUTO_GLYPH_DRAWING_THRESHOLD
        and fill_ratio >= AUTO_GLYPH_FILL_RATIO
        and tiny_rect_ratio >= AUTO_GLYPH_TINY_RECT_RATIO
        and stroke_ratio <= AUTO_GLYPH_STROKE_SPARSE_RATIO
    ):
        return {
            "type": "glyph_flood",
            "reason": (
                f"{total} drawings, {fill_ratio:.0%} fills, "
                f"{tiny_rect_ratio:.0%} tiny rects"
            ),
            "drawing_count": total,
            "stats": stats,
        }

    # Text-density variant of glyph flood — requires BOTH high text density
    # AND glyph-like drawing characteristics (sparse strokes, high fills).
    # Without the fill/stroke check, normal shop drawings with many
    # dimension labels get falsely flagged.
    if (
        total >= AUTO_GLYPH_DRAWING_THRESHOLD
        and (
            text_blocks_count >= AUTO_GLYPH_TEXT_BLOCK_THRESHOLD
            or text_words_count >= AUTO_GLYPH_WORD_THRESHOLD
        )
        and stroke_ratio <= AUTO_GLYPH_STROKE_SPARSE_RATIO
        and fill_ratio >= AUTO_GLYPH_FILL_RATIO
    ):
        return {
            "type": "glyph_flood",
            "reason": (
                f"High text density ({text_blocks_count} blocks, "
                f"{text_words_count} words) with glyph-like draws "
                f"({fill_ratio:.0%} fills, {stroke_ratio:.0%} strokes)"
            ),
            "drawing_count": total,
            "stats": stats,
        }

    # ── Fill-art flood detection ───────────────────────────────────
    if total >= AUTO_FILL_DRAWING_THRESHOLD:
        if (
            fill_only_ratio >= AUTO_FILL_HEAVY_RATIO
            and stroke_ratio <= AUTO_FILL_STROKE_MAX
        ):
            return {
                "type": "fill_art",
                "reason": (
                    f"{fill_only_ratio:.0%} fill-only, "
                    f"{stroke_ratio:.0%} strokes in {total} drawings"
                ),
                "drawing_count": total,
                "stats": stats,
            }
        if (
            fill_only_ratio >= AUTO_FILL_PURE_RATIO
            and stroke_ratio <= AUTO_FILL_PURE_STROKE_MAX
            and total >= AUTO_FILL_PURE_MIN_GROUPS
        ):
            return {
                "type": "fill_art",
                "reason": (
                    f"Pure fill art ({fill_only_ratio:.0%} fill-only) "
                    f"in {total} drawings"
                ),
                "drawing_count": total,
                "stats": stats,
            }

    # ── Normal vector content ──────────────────────────────────────
    return {
        "type": "vectors",
        "reason": "Normal vector content",
        "drawing_count": total,
        "stats": stats,
    }
~~~

### PDFVectorImporter/pdfcadcore/dimension_parser.py

- Path: `PDFVectorImporter/pdfcadcore/dimension_parser.py`
- Size: `3.88 KB`
- Modified: `2026-04-03 19:02:39`

```python
# -*- coding: utf-8 -*-
# dimension_parser.py — Structured dimension parsing
# BlueCollar Systems — BUILT. NOT BOUGHT.
from __future__ import annotations
import re
from .primitives import ParsedDimension

MM_PER_INCH = 25.4


def parse(text: str) -> ParsedDimension:
    raw = text
    s = _normalize(raw)
    result = ParsedDimension(raw_text=raw, normalized_text=s)

    qty = _extract_qty(s)
    if qty:
        result.quantity = qty

    # Slot
    m = re.search(r'(\d+(?:\.\d+)?(?:\s*/\s*\d+)?)\s*"?\s*[xX\u00D7]\s*(\d+(?:\.\d+)?(?:\s+\d+\s*/\s*\d+)?(?:\s*/\s*\d+)?)\s*"?\s*(?:SLOT|SSL|LSL)', s, re.I)
    if m:
        w, l = _parse_token(m.group(1)), _parse_token(m.group(2))
        if w and l:
            result.kind, result.value = "slot", {"width": w*MM_PER_INCH, "length": l*MM_PER_INCH}
            result.units, result.confidence = "mm", 0.95
            return result

    # Diameter
    if re.search(r'\u00D8|DIA\b|HOLE', s, re.I):
        clean = re.sub(r'\u00D8|DIA\b|HOLE\b|\(\d+\)|\d+\s*[-xX]\s*', ' ', s, flags=re.I).strip()
        v = _parse_token(clean)
        if v is not None:
            result.kind, result.value = "diameter", v * MM_PER_INCH
            result.units, result.confidence = "mm", 0.95
            return result

    # Feet-inches
    m = re.match(r"(\d+(?:\.\d+)?)\s*['\u2032]\s*[-\u2013]?\s*(\d+(?:\.\d+)?)?\s*(?:(\d+)\s*/\s*(\d+))?\s*[\"\u2033]?\s*$", s)
    if m:
        ft = float(m.group(1))
        inc = float(m.group(2)) if m.group(2) else 0
        if m.group(3) and m.group(4) and int(m.group(4)) != 0:
            inc += float(m.group(3)) / float(m.group(4))
        result.kind, result.value = "linear", (ft * 12 + inc) * MM_PER_INCH
        result.units, result.confidence = "mm", 0.95
        return result

    # Metric explicit
    m = re.search(r'(\d+(?:\.\d+)?)\s*(MM|CM|M)\b', s, re.I)
    if m:
        v = float(m.group(1))
        u = m.group(2).upper()
        if u == "CM": v *= 10
        elif u == "M": v *= 1000
        result.kind, result.value = "linear", v
        result.units, result.confidence = "mm", 0.90
        return result

    # Imperial fraction/decimal with inch mark
    v = _parse_imperial(s)
    if v is not None:
        result.kind, result.value = "linear", v * MM_PER_INCH
        result.units, result.confidence = "mm", 0.85
        return result

    # Scale
    m = re.search(r'(\d+)\s*:\s*(\d+)', s)
    if m:
        result.kind, result.value = "scale", {"ratio": [float(m.group(1)), float(m.group(2))]}
        result.confidence = 0.80
        return result

    result.confidence = 0.1
    result.warnings.append("Could not parse")
    return result


def _normalize(t):
    t = t.replace('\u2018',"'").replace('\u2019',"'").replace('\u201C','"').replace('\u201D','"')
    t = t.replace('\u2013','-').replace('\u2014','-').replace('\u2044','/')
    t = re.sub(r'DIA\.?', 'DIA', t, flags=re.I)
    return re.sub(r'\s+', ' ', t).strip()


def _extract_qty(s):
    m = re.match(r'\s*\((\d+)\)', s) or re.match(r'\s*(\d+)\s*[-xX]\s*(?:\u00D8|\d)', s)
    return int(m.group(1)) if m else None


def _parse_token(s):
    if not s: return None
    s = s.strip().rstrip('"\'')
    m = re.match(r'(\d+)\s+(\d+)\s*/\s*(\d+)$', s)
    if m and int(m.group(3)) != 0: return float(m.group(1)) + float(m.group(2))/float(m.group(3))
    m = re.match(r'(\d+)\s*/\s*(\d+)$', s)
    if m and int(m.group(2)) != 0: return float(m.group(1))/float(m.group(2))
    m = re.match(r'(\d+(?:\.\d+)?)$', s)
    if m: return float(m.group(1))
    return None


def _parse_imperial(s):
    m = re.match(r'\s*(\d+)\s+(\d+)\s*/\s*(\d+)\s*["\u2033]?', s)
    if m and int(m.group(3)) != 0: return float(m.group(1)) + float(m.group(2))/float(m.group(3))
    m = re.match(r'\s*(\d+)\s*/\s*(\d+)\s*["\u2033]?\s*$', s)
    if m and int(m.group(2)) != 0: return float(m.group(1))/float(m.group(2))
    m = re.match(r'\s*(\d+(?:\.\d+)?)\s*["\u2033]', s)
    if m: return float(m.group(1))
    return None
```

### PDFVectorImporter/pdfcadcore/document_profiler.py

- Path: `PDFVectorImporter/pdfcadcore/document_profiler.py`
- Size: `2.85 KB`
- Modified: `2026-04-03 19:02:39`

```python
# -*- coding: utf-8 -*-
# document_profiler.py — Auto page-type detection
# BlueCollar Systems — BUILT. NOT BOUGHT.
from __future__ import annotations
from .primitives import PageData, PageProfile
from .geometry_cleanup import circle_fit


def profile(page_data: PageData) -> PageProfile:
    """Score page type. Returns PageProfile."""
    prims = page_data.primitives
    texts = page_data.text_items

    lines = sum(1 for p in prims if p.type == "line")
    closed = sum(1 for p in prims if p.type == "closed_loop")
    polylines = sum(1 for p in prims if p.type == "polyline")
    total_geom = len(prims)

    dim_texts = sum(1 for t in texts if "dimension_like" in t.generic_tags)
    scale_texts = sum(1 for t in texts if "scale_like" in t.generic_tags)
    tb_texts = sum(1 for t in texts if "titleblock_like" in t.generic_tags)
    callout_texts = sum(1 for t in texts if "callout_like" in t.generic_tags)
    total_text = len(texts)
    has_layers = bool(page_data.layers)

    circles = 0
    for p in prims:
        if p.type == "closed_loop" and p.points and len(p.points) >= 8:
            fit = circle_fit(p.points)
            if fit and fit[3] < 0.5:
                circles += 1

    scores = {}

    s = 0.20 * (circles > 3) + 0.15 * (callout_texts > 2) + 0.15 * (dim_texts > 5)
    s += 0.10 * (closed > 10) + 0.10 * (tb_texts > 2) + 0.10 * (scale_texts > 0)
    scores["fabrication"] = min(s, 1.0)

    s = 0.20 * (lines > 50) + 0.15 * (dim_texts > 3) + 0.15 * has_layers
    s += 0.10 * (closed > 5) + 0.10 * (scale_texts > 0) + 0.10 * (tb_texts > 0)
    scores["cad_drawing"] = min(s, 1.0)

    s = 0.20 * (lines > 100) + 0.15 * has_layers + 0.15 * (dim_texts > 10)
    s += 0.10 * (total_text > 30) - 0.15 * (circles > 10)
    scores["architectural"] = min(max(s, 0), 1.0)

    s = 0.30 * (total_geom > 20 and dim_texts == 0) + 0.20 * (polylines > lines)
    s += 0.10 * (total_text < 5) - 0.20 * has_layers - 0.20 * (dim_texts > 2)
    scores["vector_art"] = min(max(s, 0), 1.0)

    s = 0.90 if total_geom == 0 and total_text == 0 else 0.0
    scores["raster_only"] = s

    primary = max(scores, key=scores.get) if scores else "unknown"
    if max(scores.values(), default=0) < 0.25:
        primary = "cad_drawing" if total_geom > 0 else "unknown"

    return PageProfile(
        page_number=page_data.page_number, primary_type=primary,
        scores=scores, has_layers=has_layers, has_text=total_text > 0,
        has_dimensions=dim_texts > 0, circle_count=circles,
        closed_loop_count=closed, line_count=lines, text_count=total_text,
        titleblock_likely=tb_texts > 2
    )


def suggest_mode(profile_result: PageProfile) -> str:
    t = profile_result.primary_type
    if t == "fabrication":
        return "technical"
    elif t == "architectural":
        return "architectural"
    elif t in ("vector_art", "raster_only"):
        return "none"
    return "generic"
```

### PDFVectorImporter/pdfcadcore/generic_classifier.py

- Path: `PDFVectorImporter/pdfcadcore/generic_classifier.py`
- Size: `3.23 KB`
- Modified: `2026-04-03 19:02:39`

```python
# -*- coding: utf-8 -*-
# generic_classifier.py — Domain-neutral classification
# BlueCollar Systems — BUILT. NOT BOUGHT.
"""Classifies text and primitives generically. Domain-neutral."""
from __future__ import annotations
import re
from .primitives import PageData


def classify_text(page_data: PageData):
    """Add generic tags to text items (in place)."""
    for txt in page_data.text_items:
        tags = list(txt.generic_tags)
        tu = txt.normalized
        if re.search(r"\b(NOTE|NOTES|N\.?T\.?S\.?|SEE\s+DWG)\b", tu):
            tags.append("note_indicator")
        if re.search(r"\b(QTY|EA|EACH|PCS)\b", tu):
            tags.append("quantity_indicator")
        if re.search(r"\bREV[.\s]?[A-Z0-9]?\b", tu):
            tags.append("revision_like")
        if re.search(r"\b(DETAIL|SECTION|VIEW|ELEVATION)\s+[A-Z]", tu):
            tags.append("detail_reference")
        txt.generic_tags = tags


def classify_primitives(page_data: PageData):
    """Add generic tags to primitives (in place)."""
    page_area = page_data.width * page_data.height
    for p in page_data.primitives:
        tags = list(p.generic_tags)
        if p.type == "closed_loop" and p.area and p.area > page_area * 0.7:
            if p.points and len(p.points) <= 5:
                tags.append("page_border")
        if p.type == "closed_loop" and p.area and p.area < 50.0:
            if p.points and len(p.points) <= 5:
                tags.append("possible_table_cell")
        if p.dash_pattern:
            tags.append("dashed_line")
        if p.line_width is not None and p.line_width < 0.3:
            tags.append("thin_line")
        p.generic_tags = tags


def detect_title_block(page_data: PageData):
    """Returns bbox (x0,y0,x1,y1) of likely title block or None."""
    tb = [t for t in page_data.text_items if "titleblock_like" in t.generic_tags]
    if len(tb) < 2:
        return None
    xs = [t.insertion[0] for t in tb]
    ys = [t.insertion[1] for t in tb]
    bbox = (min(xs) - 1, min(ys) - 1, max(xs) + 1, max(ys) + 1)
    if bbox[3] < page_data.height * 0.4:
        return bbox
    return None


def detect_tables(page_data: PageData):
    """Find clusters of small rectangles -> table regions."""
    cells = [p for p in page_data.primitives
             if "possible_table_cell" in p.generic_tags]
    if len(cells) < 4:
        return []
    tables = []
    used = set()
    for i, c in enumerate(cells):
        if i in used:
            continue
        cluster = [c]
        used.add(i)
        for j, o in enumerate(cells):
            if j in used:
                continue
            if c.bbox and o.bbox and _bboxes_adjacent(c.bbox, o.bbox, 12.0):
                cluster.append(o)
                used.add(j)
        if len(cluster) >= 4:
            all_x = [v for c2 in cluster for v in (c2.bbox[0], c2.bbox[2]) if c2.bbox]
            all_y = [v for c2 in cluster for v in (c2.bbox[1], c2.bbox[3]) if c2.bbox]
            tables.append({"bbox": (min(all_x), min(all_y), max(all_x), max(all_y)),
                           "cell_count": len(cluster)})
    return tables


def _bboxes_adjacent(b1, b2, threshold):
    gap_x = max(b1[0] - b2[2], b2[0] - b1[2], 0)
    gap_y = max(b1[1] - b2[3], b2[1] - b1[3], 0)
    return gap_x < threshold and gap_y < threshold
```

### PDFVectorImporter/pdfcadcore/generic_recognizer.py

- Path: `PDFVectorImporter/pdfcadcore/generic_recognizer.py`
- Size: `2.92 KB`
- Modified: `2026-04-03 19:02:39`

```python
# -*- coding: utf-8 -*-
# generic_recognizer.py — Domain-neutral recognition
# BlueCollar Systems — BUILT. NOT BOUGHT.
from __future__ import annotations
from dataclasses import dataclass, field
from .primitives import PageData, RecognitionConfig
from .geometry_cleanup import circle_fit
from . import generic_classifier as gc
from . import document_profiler as dp
from . import dimension_parser as dim_parser
import math


@dataclass
class GenericResults:
    circles: list = field(default_factory=list)
    closed_boundaries: list = field(default_factory=list)
    repeated_patterns: list = field(default_factory=list)
    tables: list = field(default_factory=list)
    title_block_bbox: object = None
    dimension_assocs: list = field(default_factory=list)
    page_profile: object = None


def analyze(page_data: PageData, config: RecognitionConfig = None) -> GenericResults:
    if config is None:
        config = RecognitionConfig()
    gc.classify_text(page_data)
    gc.classify_primitives(page_data)
    profile = dp.profile(page_data)

    circles = []
    for p in page_data.primitives:
        if p.type == "closed_loop" and p.closed and p.points and len(p.points) >= 6:
            fit = circle_fit(p.points)
            if fit and fit[3] < config.circle_fit_tol:
                circles.append({"center":(fit[0],fit[1]),"radius":fit[2],"prim_id":p.id,"rms":fit[3]})

    boundaries = [{"prim_id":p.id,"area":p.area,"bbox":p.bbox}
                  for p in page_data.primitives
                  if p.type=="closed_loop" and p.closed and p.area and p.area>=config.closed_loop_min_area]
    boundaries.sort(key=lambda b: -(b["area"] or 0))

    groups = {}
    for p in page_data.primitives:
        if p.type=="closed_loop" and p.area and p.area > 1.0:
            k = f"{round(p.area)}_{len(p.points or [])}"
            groups.setdefault(k,[]).append(p)
    patterns = [{"prim_ids":[q.id for q in g],"count":len(g)} for g in groups.values() if len(g)>=3]

    tables = gc.detect_tables(page_data)
    tb_bbox = gc.detect_title_block(page_data)

    dim_assocs = []
    for txt in page_data.text_items:
        if "dimension_like" not in txt.generic_tags: continue
        pd = dim_parser.parse(txt.text)
        if pd.value is None or pd.confidence < 0.3: continue
        nearest, nd = None, config.dimension_assoc_radius
        for p in page_data.primitives:
            if not p.bbox: continue
            pcx = (p.bbox[0]+p.bbox[2])/2; pcy = (p.bbox[1]+p.bbox[3])/2
            d = math.hypot(txt.insertion[0]-pcx, txt.insertion[1]-pcy)
            if d < nd: nearest, nd = p, d
        dim_assocs.append({"text_id":txt.id,"text":txt.text,"value":pd.value,
                          "kind":pd.kind,"nearest_prim_id":nearest.id if nearest else None})

    return GenericResults(circles=circles, closed_boundaries=boundaries,
        repeated_patterns=patterns, tables=tables, title_block_bbox=tb_bbox,
        dimension_assocs=dim_assocs, page_profile=profile)
```

### PDFVectorImporter/pdfcadcore/geometry_cleanup.py

- Path: `PDFVectorImporter/pdfcadcore/geometry_cleanup.py`
- Size: `2.47 KB`
- Modified: `2026-04-03 19:02:39`

```python
# -*- coding: utf-8 -*-
# geometry_cleanup.py — Geometry cleanup on primitives
# BlueCollar Systems — BUILT. NOT BOUGHT.
from __future__ import annotations
import math
from typing import List, Tuple


def circle_fit(points: List[Tuple[float, float]]):
    """Kasa algebraic circle fit -> (cx, cy, radius, rms) or None."""
    n = len(points)
    if n < 3:
        return None
    sx = sum(p[0] for p in points)
    sy = sum(p[1] for p in points)
    sx2 = sum(p[0]**2 for p in points)
    sy2 = sum(p[1]**2 for p in points)
    sxy = sum(p[0]*p[1] for p in points)
    sz = sum(p[0]**2 + p[1]**2 for p in points)
    sxz = sum(p[0]*(p[0]**2 + p[1]**2) for p in points)
    syz = sum(p[1]*(p[0]**2 + p[1]**2) for p in points)
    A = [[sx, sy, n], [sx2, sxy, sx], [sxy, sy2, sy]]
    B = [sz, sxz, syz]
    D = _det3(A)
    if abs(D) < 1e-12:
        return None
    A1 = [[B[0],A[0][1],A[0][2]],[B[1],A[1][1],A[1][2]],[B[2],A[2][1],A[2][2]]]
    A2 = [[A[0][0],B[0],A[0][2]],[A[1][0],B[1],A[1][2]],[A[2][0],B[2],A[2][2]]]
    A3 = [[A[0][0],A[0][1],B[0]],[A[1][0],A[1][1],B[1]],[A[2][0],A[2][1],B[2]]]
    a = _det3(A1)/D; b = _det3(A2)/D; c = _det3(A3)/D
    cx, cy = 0.5*a, 0.5*b
    r = math.sqrt(max(0, c + cx*cx + cy*cy))
    rms = math.sqrt(sum((math.hypot(p[0]-cx, p[1]-cy) - r)**2 for p in points) / n)
    return (cx, cy, r, rms)


def _det3(m):
    return (m[0][0]*(m[1][1]*m[2][2]-m[1][2]*m[2][1])
           -m[0][1]*(m[1][0]*m[2][2]-m[1][2]*m[2][0])
           +m[0][2]*(m[1][0]*m[2][1]-m[1][1]*m[2][0]))


def cleanup_primitives(primitives, config=None, cleanup_level=None):
    """Run cleanup on primitive list. Returns stats dict."""
    from .primitives import RecognitionConfig
    if config is None:
        config = RecognitionConfig()

    min_seg = config.min_segment_len
    if cleanup_level:
        from .import_config import CLEANUP_PRESETS
        preset = CLEANUP_PRESETS.get(cleanup_level.lower(),
                                     CLEANUP_PRESETS.get("balanced", {}))
        if "min_seg" in preset:
            min_seg = preset["min_seg"]

    stats = {"merged": 0, "removed_micro": 0, "removed_dupes": 0}
    before = len(primitives)
    primitives[:] = [p for p in primitives
                     if not (p.type == "line" and p.points and len(p.points) == 2
                             and math.hypot(p.points[1][0]-p.points[0][0],
                                            p.points[1][1]-p.points[0][1]) < min_seg)]
    stats["removed_micro"] = before - len(primitives)
    return stats
```

### PDFVectorImporter/pdfcadcore/hatch_detector.py

- Path: `PDFVectorImporter/pdfcadcore/hatch_detector.py`
- Size: `7.29 KB`
- Modified: `2026-04-04 03:33:46`

~~~python
# -*- coding: utf-8 -*-
# hatch_detector.py — Detect hatching patterns in PyMuPDF drawing groups
# BlueCollar Systems — BUILT. NOT BOUGHT.
"""
Hatching = dense clusters of parallel lines at regular spacing.
Modes: "import" (default), "skip" (remove), "group" (separate hidden group)
"""
from __future__ import annotations

import math
from typing import List, Optional, Set, Tuple

MIN_HATCH_LINES = 6
ANGLE_TOL_DEG = 3.0
SPACING_REGULARITY = 0.35
LENGTH_CV_MAX = 0.50


def _parse_line_segment(item_data) -> Optional[Tuple[float, float, float, float]]:
    if len(item_data) >= 2:
        p0, p1 = item_data[0], item_data[1]
        if hasattr(p0, 'x') and hasattr(p1, 'x'):
            return (p0.x, p0.y, p1.x, p1.y)
    return None


def _angle_diff(a: float, b: float) -> float:
    d = abs(a - b)
    if d > 90.0:
        d = 180.0 - d
    return d


def detect(drawings: List[dict]) -> Set[int]:
    """Detect hatch patterns. Returns set of drawing-group indices."""
    if not drawings or len(drawings) < MIN_HATCH_LINES:
        return set()

    lines: List[dict] = []
    for idx, pg in enumerate(drawings):
        items = pg.get("items", [])
        if len(items) < 1:
            continue
        segs = []
        cur = None
        for item in items:
            kind = item[0]
            data = item[1:]
            if kind == "m":
                pt = data[0] if data else None
                if pt and hasattr(pt, 'x'):
                    cur = (pt.x, pt.y)
            elif kind == "l" and cur is not None:
                parsed = _parse_line_segment(data)
                if parsed:
                    segs.append(parsed)
                else:
                    pt = data[0] if data else None
                    if pt and hasattr(pt, 'x'):
                        segs.append((cur[0], cur[1], pt.x, pt.y))
                        cur = (pt.x, pt.y)
            elif kind == "c":
                break
        if len(segs) == 1:
            x0, y0, x1, y1 = segs[0]
            dx, dy = x1 - x0, y1 - y0
            length = math.hypot(dx, dy)
            if length < 0.5:
                continue
            angle = math.degrees(math.atan2(dy, dx))
            if angle < 0:
                angle += 180.0
            mx, my = (x0 + x1) / 2.0, (y0 + y1) / 2.0
            lines.append({"idx": idx, "angle": angle, "len": length, "mx": mx, "my": my})

    if len(lines) < MIN_HATCH_LINES:
        return set()

    hatch_indices: Set[int] = set()
    used = [False] * len(lines)

    for i, line in enumerate(lines):
        if used[i]:
            continue
        group = [line]
        used[i] = True
        for j, other in enumerate(lines):
            if j <= i or used[j]:
                continue
            if _angle_diff(line["angle"], other["angle"]) < ANGLE_TOL_DEG:
                group.append(other)
                used[j] = True
        if len(group) < MIN_HATCH_LINES:
            continue

        ref_rad = math.radians(group[0]["angle"])
        perp_x = -math.sin(ref_rad)
        perp_y = math.cos(ref_rad)
        projections = sorted(
            [{"proj": l["mx"] * perp_x + l["my"] * perp_y, "line": l} for l in group],
            key=lambda p: p["proj"]
        )
        spacings = []
        for k in range(1, len(projections)):
            spacings.append(abs(projections[k]["proj"] - projections[k-1]["proj"]))
        if not spacings:
            continue
        mean_sp = sum(spacings) / len(spacings)
        if mean_sp < 0.3:
            continue
        variance = sum((s - mean_sp) ** 2 for s in spacings) / len(spacings)
        std_dev = math.sqrt(variance)
        if mean_sp > 0 and (std_dev / mean_sp) < SPACING_REGULARITY:
            lengths = [l["len"] for l in group]
            mean_len = sum(lengths) / len(lengths)
            len_var = sum((v - mean_len) ** 2 for v in lengths) / len(lengths)
            len_cv = math.sqrt(len_var) / mean_len if mean_len > 0 else 1.0
            if len_cv < LENGTH_CV_MAX:
                for l in group:
                    hatch_indices.add(l["idx"])

    return hatch_indices


# ── Post-extraction hatch detection on Primitive objects ────────────

def tag_hatch_primitives(primitives) -> Set[int]:
    """Detect hatch patterns among extracted Primitive objects.

    Works on the already-extracted primitives (post-extraction) rather
    than raw PyMuPDF drawings.  Uses the same algorithm as :func:`detect`
    but operates on :class:`Primitive` ``points`` instead of raw path items.

    Parameters
    ----------
    primitives:
        List of :class:`Primitive` objects from a :class:`PageData`.

    Returns
    -------
    set[int]
        Set of Primitive ``.id`` values that form hatch patterns.
    """
    if not primitives or len(primitives) < MIN_HATCH_LINES:
        return set()

    # Step 1: filter to simple line primitives (type=="line", exactly 2 points)
    lines = []
    for p in primitives:
        if p.type != "line" or not p.points or len(p.points) != 2:
            continue
        x0, y0 = p.points[0]
        x1, y1 = p.points[1]
        dx, dy = x1 - x0, y1 - y0
        length = math.hypot(dx, dy)
        if length < 0.5:
            continue
        angle = math.degrees(math.atan2(dy, dx))
        if angle < 0:
            angle += 180.0
        mx = (x0 + x1) / 2.0
        my = (y0 + y1) / 2.0
        lines.append({
            "pid": p.id,
            "angle": angle,
            "len": length,
            "mx": mx,
            "my": my,
        })

    if len(lines) < MIN_HATCH_LINES:
        return set()

    # Step 2: group by angle (within tolerance)
    hatch_ids: Set[int] = set()
    used = [False] * len(lines)

    for i, line in enumerate(lines):
        if used[i]:
            continue
        group = [line]
        used[i] = True
        for j, other in enumerate(lines):
            if j <= i or used[j]:
                continue
            if _angle_diff(line["angle"], other["angle"]) < ANGLE_TOL_DEG:
                group.append(other)
                used[j] = True
        if len(group) < MIN_HATCH_LINES:
            continue

        # Step 3: check spacing regularity along perpendicular axis
        ref_rad = math.radians(group[0]["angle"])
        perp_x = -math.sin(ref_rad)
        perp_y = math.cos(ref_rad)
        projections = sorted(
            [{"proj": l["mx"] * perp_x + l["my"] * perp_y, "line": l}
             for l in group],
            key=lambda p: p["proj"],
        )
        spacings = []
        for k in range(1, len(projections)):
            spacings.append(
                abs(projections[k]["proj"] - projections[k - 1]["proj"])
            )
        if not spacings:
            continue
        mean_sp = sum(spacings) / len(spacings)
        if mean_sp < 0.3:
            continue
        variance = sum((s - mean_sp) ** 2 for s in spacings) / len(spacings)
        std_dev = math.sqrt(variance)
        if mean_sp > 0 and (std_dev / mean_sp) < SPACING_REGULARITY:
            # Step 4: check length consistency
            lengths = [l["len"] for l in group]
            mean_len = sum(lengths) / len(lengths)
            len_var = sum((v - mean_len) ** 2 for v in lengths) / len(lengths)
            len_cv = math.sqrt(len_var) / mean_len if mean_len > 0 else 1.0
            if len_cv < LENGTH_CV_MAX:
                for l in group:
                    hatch_ids.add(l["pid"])

    return hatch_ids
~~~

### PDFVectorImporter/pdfcadcore/import_config.py

- Path: `PDFVectorImporter/pdfcadcore/import_config.py`
- Size: `6.89 KB`
- Modified: `2026-04-03 19:02:39`

```python
# -*- coding: utf-8 -*-
# import_config.py — Versioned import configuration
# BlueCollar Systems — BUILT. NOT BOUGHT.
"""
Centralised, versioned import configuration for PDF Vector Importers.
Shared across FreeCAD, Blender, and LibreCAD hosts.
"""
from __future__ import annotations

from dataclasses import dataclass, asdict, fields
from typing import Any, Dict, List, Optional


# ──────────────────────────────────────────────────────────────────────
# Cleanup presets  (tolerance values in mm)
# ──────────────────────────────────────────────────────────────────────
CLEANUP_PRESETS: Dict[str, Dict[str, float]] = {
    "conservative": {
        "merge_tol": 0.5,
        "collinear_tol": 0.25,
        "min_seg": 0.25,
    },
    "balanced": {
        "merge_tol": 0.1,
        "collinear_tol": 0.05,
        "min_seg": 0.05,
    },
    "aggressive": {
        "merge_tol": 0.01,
        "collinear_tol": 0.005,
        "min_seg": 0.01,
    },
}


@dataclass
class ImportConfig:
    """Versioned import configuration for PDF Vector Importers."""

    VERSION: str = "2.0"

    # ── Core geometry options ────────────────────────────────────────
    pages: Optional[List[int]] = None
    scale_to_mm: bool = True
    user_scale: float = 1.0
    flip_y: bool = True
    join_tol: float = 0.1
    min_seg_len: float = 0.0
    curve_step_mm: float = 0.5
    make_faces: bool = True
    import_text: bool = True
    text_mode: str = "labels"               # "labels" | "geometry" | "none"
    strict_text_fidelity: bool = True
    group_by_color: bool = True
    assign_lineweight: bool = True
    map_dashes: bool = True
    verbose: bool = True
    create_top_group: bool = True
    hatch_to_faces: bool = True
    hatch_mode: str = "import"              # "import" | "skip" | "group"
    ignore_images: bool = False
    raster_fallback: bool = True
    raster_dpi: int = 200
    import_mode: str = "auto"               # "auto" | "vectors" | "raster" | "hybrid"
    max_bezier_segments: int = 128

    # ── Arc reconstruction ───────────────────────────────────────────
    detect_arcs: bool = True
    arc_fit_tol_mm: float = 0.08
    min_arc_angle_deg: float = 5.0
    arc_sampling_pts: int = 7

    # ── Layering ─────────────────────────────────────────────────────
    layer_mode: str = "auto"                # "auto" | "ocg" | "color" | "none"

    # ── Object-count management ──────────────────────────────────────
    compound_batch_size: int = 200
    heavy_page_threshold: int = 3000

    # ── Phase 2 options ──────────────────────────────────────────────
    arc_mode: str = "auto"
    cleanup_level: str = "balanced"
    lineweight_mode: str = "ignore"
    grouping_mode: str = "per_page"

    # ─────────────────────────────────────────────────────────────────
    def to_dict(self) -> Dict[str, Any]:
        d = asdict(self)
        d.pop("VERSION", None)
        return d

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> "ImportConfig":
        valid_keys = {f.name for f in fields(cls)}
        filtered = {k: v for k, v in d.items() if k in valid_keys}
        return cls(**filtered)

    def get_cleanup_tolerances(self) -> Dict[str, float]:
        return dict(CLEANUP_PRESETS.get(self.cleanup_level,
                                        CLEANUP_PRESETS["balanced"]))

    # ── Named constructors (presets) ─────────────────────────────────
    @classmethod
    def fast(cls) -> "ImportConfig":
        """Fast Preview — speed over fidelity."""
        return cls(
            curve_step_mm=2.0, join_tol=0.5, detect_arcs=False,
            map_dashes=False, make_faces=False, import_text=False,
            text_mode="none", strict_text_fidelity=False,
            hatch_mode="skip", import_mode="auto",
            cleanup_level="conservative", arc_mode="polyline",
            lineweight_mode="ignore", grouping_mode="single",
        )

    @classmethod
    def general_vector(cls) -> "ImportConfig":
        """General Vector — good for most PDFs."""
        return cls(
            curve_step_mm=1.0, join_tol=0.2, detect_arcs=True,
            map_dashes=False, make_faces=False, import_text=True,
            text_mode="labels", strict_text_fidelity=False,
            hatch_mode="skip", import_mode="auto",
            cleanup_level="conservative", arc_mode="auto",
            lineweight_mode="ignore", grouping_mode="per_page",
        )

    @classmethod
    def technical_drawing(cls) -> "ImportConfig":
        """Technical Drawing — engineering drawings."""
        return cls(
            curve_step_mm=0.5, join_tol=0.1, detect_arcs=True,
            map_dashes=True, make_faces=True, import_text=True,
            text_mode="geometry", strict_text_fidelity=True,
            hatch_mode="group", import_mode="auto",
            cleanup_level="balanced", arc_mode="auto",
            lineweight_mode="preserve", grouping_mode="per_page",
        )

    @classmethod
    def shop_drawing(cls) -> "ImportConfig":
        """Shop Drawing — fabrication drawings (default)."""
        return cls(
            curve_step_mm=0.5, join_tol=0.1, detect_arcs=True,
            map_dashes=True, make_faces=True, import_text=True,
            text_mode="geometry", strict_text_fidelity=True,
            hatch_mode="group", import_mode="auto",
            cleanup_level="balanced", arc_mode="auto",
            lineweight_mode="preserve", grouping_mode="per_page",
        )

    @classmethod
    def full(cls) -> "ImportConfig":
        """Full / Shop Drawing preset — balanced quality."""
        return cls.shop_drawing()

    @classmethod
    def max_fidelity(cls) -> "ImportConfig":
        """Max Fidelity — highest accuracy, slower."""
        return cls(
            curve_step_mm=0.2, join_tol=0.05, detect_arcs=True,
            map_dashes=True, make_faces=True, import_text=True,
            text_mode="geometry", strict_text_fidelity=True,
            hatch_mode="import", import_mode="auto",
            cleanup_level="aggressive", arc_mode="rebuild",
            lineweight_mode="preserve", grouping_mode="nested_page_layer",
        )
```

### PDFVectorImporter/pdfcadcore/primitive_extractor.py

- Path: `PDFVectorImporter/pdfcadcore/primitive_extractor.py`
- Size: `12.19 KB`
- Modified: `2026-04-04 02:46:03`

~~~python
# -*- coding: utf-8 -*-
# primitive_extractor.py — PyMuPDF -> normalized Primitives
# BlueCollar Systems — BUILT. NOT BOUGHT.
"""
THE SEAM: converts PyMuPDF page data into host-neutral Primitives.
Rule 1: Parser modules must not know about domain-specific logic.
"""
from __future__ import annotations
import math
import re
from typing import List, Tuple

from .primitives import (
    Primitive, NormalizedText, PageData, next_id
)

MM_PER_PT = 25.4 / 72.0


def _xy(obj) -> Tuple[float, float]:
    if hasattr(obj, "x") and hasattr(obj, "y"):
        return float(obj.x), float(obj.y)
    if isinstance(obj, (tuple, list)) and len(obj) >= 2:
        return float(obj[0]), float(obj[1])
    return 0.0, 0.0


def _norm_color(col) -> Tuple[float, float, float]:
    if col is None:
        return (0.0, 0.0, 0.0)
    try:
        if isinstance(col, (int, float)):
            g = max(0.0, min(1.0, float(col)))
            return (g, g, g)
        vals = [max(0.0, min(1.0, float(c))) for c in col]
        if len(vals) >= 4:
            c, m, y, k = vals[0], vals[1], vals[2], vals[3]
            r = (1.0 - c) * (1.0 - k)
            g = (1.0 - m) * (1.0 - k)
            b = (1.0 - y) * (1.0 - k)
            return (
                max(0.0, min(1.0, r)),
                max(0.0, min(1.0, g)),
                max(0.0, min(1.0, b)),
            )
        while len(vals) < 3:
            vals.append(vals[-1] if vals else 0.0)
        return (vals[0], vals[1], vals[2])
    except (TypeError, ValueError, AttributeError):
        return (0.0, 0.0, 0.0)


def _parse_dashes(raw) -> list | None:
    """Parse PyMuPDF dash patterns into a numeric list.

    PyMuPDF returns dashes as strings like ``'[ 6 6 ] 0'`` (array + phase)
    or as actual lists/tuples.  Returns ``None`` for solid lines.
    """
    if raw is None:
        return None
    if isinstance(raw, str):
        s = raw.strip()
        if not s or s.startswith("[]") or s == "() 0":
            return None
        # Extract numbers between brackets: "[ 6 6 ] 0" -> [6.0, 6.0]
        bracket = s.find("[")
        bracket_end = s.find("]")
        if bracket >= 0 and bracket_end > bracket:
            inner = s[bracket + 1:bracket_end].strip()
            if not inner:
                return None
            try:
                nums = [float(x) for x in inner.split()]
                return nums if nums else None
            except ValueError:
                return None
        return None
    if isinstance(raw, (list, tuple)):
        if not raw:
            return None
        # Could be ([6,6], 0) tuple or flat [6,6]
        if len(raw) == 2 and isinstance(raw[0], (list, tuple)):
            return list(raw[0]) if raw[0] else None
        try:
            nums = [float(x) for x in raw]
            return nums if nums else None
        except (TypeError, ValueError):
            return None
    return None


def extract_page(page, page_num: int, scale: float = 1.0,
                 flip_y: bool = True) -> PageData:
    """Extract normalized primitives from a PyMuPDF page."""
    page_h = page.rect.height
    page_w_mm = page.rect.width * MM_PER_PT * scale
    page_h_mm = page.rect.height * MM_PER_PT * scale

    primitives = []
    drawings = page.get_drawings()

    for path_group in drawings:
        items = path_group.get("items", [])
        if not items:
            continue

        stroke = _norm_color(path_group.get("color") or path_group.get("stroke"))
        fill = _norm_color(path_group.get("fill"))
        width = path_group.get("width")
        dashes = _parse_dashes(path_group.get("dashes"))
        close_path = path_group.get("closePath", False)
        layer_name = path_group.get("oc") or path_group.get("layer")

        current_pts: List[Tuple[float, float]] = []
        sub_paths: List[Tuple[List[Tuple[float, float]], bool]] = []

        def flush(closed: bool, _sub_paths=sub_paths):
            nonlocal current_pts
            if len(current_pts) >= 2:
                _sub_paths.append((current_pts[:], closed))
            current_pts = []

        for item in items:
            kind = item[0]
            data = item[1:]

            if kind == "m":
                flush(False)
                x, y = _parse_point(data)
                px, py = _to_mm(x, y, page_h, flip_y, scale)
                current_pts = [(px, py)]

            elif kind == "l":
                if len(data) >= 2 and hasattr(data[0], "x") and hasattr(data[1], "x"):
                    x0, y0 = _xy(data[0])
                    x1, y1 = _xy(data[1])
                    p0 = _to_mm(x0, y0, page_h, flip_y, scale)
                    p1 = _to_mm(x1, y1, page_h, flip_y, scale)
                    if not current_pts:
                        current_pts.append(p0)
                    current_pts.append(p1)
                else:
                    x, y = _parse_point(data)
                    current_pts.append(_to_mm(x, y, page_h, flip_y, scale))

            elif kind == "c":
                if len(data) == 4 and all(hasattr(d, "x") for d in data):
                    pts = [_xy(d) for d in data]
                else:
                    pts = _parse_cubic(data)
                p0 = _to_mm(pts[0][0], pts[0][1], page_h, flip_y, scale)
                p1 = _to_mm(pts[1][0], pts[1][1], page_h, flip_y, scale)
                p2 = _to_mm(pts[2][0], pts[2][1], page_h, flip_y, scale)
                p3 = _to_mm(pts[3][0] if len(pts) > 3 else pts[2][0],
                            pts[3][1] if len(pts) > 3 else pts[2][1],
                            page_h, flip_y, scale)
                if not current_pts:
                    current_pts.append(p0)
                N = max(4, min(32, int(math.ceil(_dist(p0, p3) / 0.5))))
                for i in range(1, N + 1):
                    t = i / float(N)
                    q = _bezier_pt(p0, p1, p2, p3, t)
                    current_pts.append(q)

            elif kind == "re":
                flush(False)
                x, y, w, h = _parse_rect(data)
                c1 = _to_mm(x, y, page_h, flip_y, scale)
                c2 = _to_mm(x + w, y, page_h, flip_y, scale)
                c3 = _to_mm(x + w, y + h, page_h, flip_y, scale)
                c4 = _to_mm(x, y + h, page_h, flip_y, scale)
                sub_paths.append(([c1, c2, c3, c4, c1], True))

            elif kind == "h":
                flush(True)

            elif kind == "v":
                if len(data) >= 2:
                    cx, cy = _xy(data[0])
                    ex, ey = _xy(data[1])
                    ctrl = _to_mm(cx, cy, page_h, flip_y, scale)
                    end = _to_mm(ex, ey, page_h, flip_y, scale)
                    if current_pts:
                        p0 = current_pts[-1]
                        cp1 = (p0[0] + 2/3*(ctrl[0]-p0[0]), p0[1] + 2/3*(ctrl[1]-p0[1]))
                        cp2 = (end[0] + 2/3*(ctrl[0]-end[0]), end[1] + 2/3*(ctrl[1]-end[1]))
                        N = 8
                        for i in range(1, N + 1):
                            t = i / float(N)
                            current_pts.append(_bezier_pt(p0, cp1, cp2, end, t))

        flush(close_path)

        for pts, is_closed in sub_paths:
            if len(pts) < 2:
                continue
            cleaned = [pts[0]]
            for p in pts[1:]:
                if _dist(p, cleaned[-1]) > 0.01:
                    cleaned.append(p)
            if len(cleaned) < 2:
                continue

            xs = [p[0] for p in cleaned]
            ys = [p[1] for p in cleaned]
            bbox = (min(xs), min(ys), max(xs), max(ys))

            area = None
            if is_closed and len(cleaned) >= 3:
                area = _polygon_area(cleaned)

            ptype = "line" if len(cleaned) == 2 else ("closed_loop" if is_closed else "polyline")

            primitives.append(Primitive(
                id=next_id(), type=ptype, points=cleaned,
                bbox=bbox, stroke_color=stroke, fill_color=fill,
                dash_pattern=dashes, line_width=width,
                layer_name=layer_name, closed=is_closed,
                area=area, page_number=page_num
            ))

    text_items = _extract_text(page, page_h, page_num, flip_y, scale)

    return PageData(
        page_number=page_num,
        width=page_w_mm, height=page_h_mm,
        primitives=primitives, text_items=text_items,
        layers=[], xobject_names=[]
    )


def _extract_text(page, page_h, page_num, flip_y, scale) -> List[NormalizedText]:
    items = []
    try:
        tdict = page.get_text("dict")
    except (RuntimeError, TypeError, ValueError):
        return items

    for block in tdict.get("blocks", []):
        if block.get("type") != 0:
            continue
        for line in block.get("lines", []):
            spans = line.get("spans", [])
            if not spans:
                continue
            text = "".join(s.get("text", "") for s in spans).strip()
            if not text:
                continue

            origin = spans[0].get("origin")
            if origin:
                x, y = float(origin[0]), float(origin[1])
            else:
                bb = line.get("bbox", (0, 0, 0, 0))
                x, y = float(bb[0]), float(bb[1])

            px, py = _to_mm(x, y, page_h, flip_y, scale)
            size = max(float(spans[0].get("size", 3)), 1.0) * MM_PER_PT * scale
            font = str(spans[0].get("font", ""))

            text_dir = line.get("dir", (1.0, 0.0))
            dx = float(text_dir[0]) if text_dir else 1.0
            dy = float(text_dir[1]) if text_dir else 0.0
            angle = -math.degrees(math.atan2(dy, dx))

            normalized = text.upper().replace("  ", " ").strip()
            generic_tags = _classify_generic(text)

            items.append(NormalizedText(
                id=next_id(), text=text, normalized=normalized,
                insertion=(px, py), font_size=size,
                rotation=angle, font_name=font,
                page_number=page_num, generic_tags=generic_tags
            ))
    return items


def _classify_generic(text: str) -> list:
    tags = []
    t = text.strip()
    tu = t.upper()
    if re.search(r"\d+['']\s*[-\u2013]?\s*\d", t) or re.search(r"\d+\s*/\s*\d+", t):
        tags.append("dimension_like")
    if re.search(r'\d+\.?\d*\s*(?:"|mm|cm|in|ft)', t, re.I):
        tags.append("dimension_like")
    if re.search(r"SCALE[:\s]*\d", tu) or re.search(r"\d+\s*:\s*\d+", t):
        tags.append("scale_like")
    if re.search(r"\b(DRAWN|CHECKED|DATE|SCALE|REV|SHEET|PROJECT|DWG|TITLE)\b", tu):
        tags.append("titleblock_like")
    if re.search(r"\u00D8|\bDIA\b|\bRAD\b|\bR\d", t, re.I):
        tags.append("callout_like")
    if re.search(r"\b(DETAIL|SECTION|SEC|VIEW|ELEVATION)\s+[A-Z]", tu):
        tags.append("detail_reference")
    if len(t) > 1 and len(t) < 60 and re.search(r"[A-Z]{2,}", tu):
        tags.append("label_like")
    return tags


# ── Coordinate helpers ──

def _to_mm(x, y, page_h, flip_y, scale):
    if flip_y:
        y = page_h - y
    return x * MM_PER_PT * scale, y * MM_PER_PT * scale


def _parse_point(data):
    if len(data) >= 1 and hasattr(data[0], "x"):
        return _xy(data[0])
    if len(data) >= 2:
        return float(data[0]), float(data[1])
    return 0.0, 0.0


def _parse_cubic(data):
    if len(data) == 3 and all(hasattr(d, "x") for d in data):
        return [_xy(d) for d in data]
    if len(data) >= 6:
        return [(float(data[0]), float(data[1])),
                (float(data[2]), float(data[3])),
                (float(data[4]), float(data[5]))]
    if len(data) == 4:
        return [_xy(d) for d in data]
    return [(0, 0), (0, 0), (0, 0)]


def _parse_rect(data):
    if len(data) >= 1 and hasattr(data[0], "x0"):
        r = data[0]
        return float(r.x0), float(r.y0), float(r.x1) - float(r.x0), float(r.y1) - float(r.y0)
    if len(data) >= 4:
        return float(data[0]), float(data[1]), float(data[2]), float(data[3])
    return 0.0, 0.0, 0.0, 0.0


def _bezier_pt(p0, p1, p2, p3, t):
    u = 1.0 - t
    return (u**3*p0[0] + 3*u**2*t*p1[0] + 3*u*t**2*p2[0] + t**3*p3[0],
            u**3*p0[1] + 3*u**2*t*p1[1] + 3*u*t**2*p2[1] + t**3*p3[1])


def _dist(a, b):
    return math.hypot(a[0] - b[0], a[1] - b[1])


def _polygon_area(pts):
    n = len(pts)
    a = 0.0
    for i in range(n):
        j = (i + 1) % n
        a += pts[i][0] * pts[j][1] - pts[j][0] * pts[i][1]
    return abs(a) / 2.0
~~~

### PDFVectorImporter/pdfcadcore/primitives.py

- Path: `PDFVectorImporter/pdfcadcore/primitives.py`
- Size: `3.72 KB`
- Modified: `2026-04-03 19:02:39`

```python
# -*- coding: utf-8 -*-
# primitives.py — Host-neutral intermediate data model
# BlueCollar Systems — BUILT. NOT BOUGHT.
"""
All recognition modules operate on these structures, NOT on host objects.
Rule 2: Recognizers must operate on normalized primitives, not host entities.
"""
from __future__ import annotations
from dataclasses import dataclass, field
from typing import Dict, List, Optional, Tuple

_next_id = 0
def next_id() -> int:
    global _next_id
    _next_id += 1
    return _next_id

def reset_ids():
    global _next_id
    _next_id = 0


@dataclass
class RecognitionConfig:
    vertex_merge_tol: float = 0.1        # mm
    min_segment_len: float = 0.05        # mm
    loop_close_tol: float = 0.5          # mm
    region_padding: float = 25.0         # mm
    text_assoc_radius: float = 50.0      # mm
    dimension_assoc_radius: float = 75.0 # mm
    circle_min_diameter: float = 5.0     # mm
    circle_max_diameter: float = 100.0   # mm
    circle_fit_tol: float = 0.25         # mm RMS
    closed_loop_min_aspect: float = 1.5
    closed_loop_min_area: float = 100.0  # sq mm
    confidence_threshold: float = 0.60


@dataclass
class Primitive:
    id: int
    type: str              # "line", "arc", "circle", "polyline", "closed_loop", "rect"
    points: List[Tuple[float, float]]
    center: Optional[Tuple[float, float]] = None
    radius: Optional[float] = None
    start_angle: Optional[float] = None
    end_angle: Optional[float] = None
    bbox: Optional[Tuple[float, float, float, float]] = None
    stroke_color: Optional[Tuple[float, float, float]] = None
    fill_color: Optional[Tuple[float, float, float]] = None
    dash_pattern: Optional[list] = None
    line_width: Optional[float] = None
    layer_name: Optional[str] = None
    closed: bool = False
    area: Optional[float] = None
    page_number: int = 0
    generic_tags: List[str] = field(default_factory=list)


@dataclass
class NormalizedText:
    id: int
    text: str
    normalized: str        # uppercased, cleaned
    insertion: Tuple[float, float] = (0.0, 0.0)
    bbox: Optional[Tuple[float, float, float, float]] = None
    font_size: float = 3.0 # mm
    rotation: float = 0.0  # degrees
    font_name: str = ""
    page_number: int = 0
    generic_tags: List[str] = field(default_factory=list)
    domain_tags: List[dict] = field(default_factory=list)


@dataclass
class PageData:
    page_number: int
    width: float           # mm
    height: float          # mm
    primitives: List[Primitive] = field(default_factory=list)
    text_items: List[NormalizedText] = field(default_factory=list)
    layers: List[str] = field(default_factory=list)
    xobject_names: List[str] = field(default_factory=list)


@dataclass
class ParsedDimension:
    raw_text: str
    kind: str = "unknown"  # linear, diameter, radius, slot, scale, unknown
    value: object = None   # float or dict
    units: Optional[str] = None
    quantity: Optional[int] = None
    normalized_text: str = ""
    confidence: float = 0.0
    warnings: List[str] = field(default_factory=list)


@dataclass
class Region:
    id: int = 0
    page_number: int = 0
    bbox: Optional[Tuple[float, float, float, float]] = None
    primitive_ids: List[int] = field(default_factory=list)
    text_ids: List[int] = field(default_factory=list)
    region_type: str = "unknown"
    label: str = ""
    is_titleblock: bool = False
    confidence: float = 0.0


@dataclass
class PageProfile:
    page_number: int = 0
    primary_type: str = "unknown"
    scores: Dict[str, float] = field(default_factory=dict)
    has_layers: bool = False
    has_text: bool = False
    has_dimensions: bool = False
    circle_count: int = 0
    closed_loop_count: int = 0
    line_count: int = 0
    text_count: int = 0
    titleblock_likely: bool = False
```

### PDFVectorImporter/pdfcadcore/recognition.py

- Path: `PDFVectorImporter/pdfcadcore/recognition.py`
- Size: `959.00 B`
- Modified: `2026-04-03 19:02:39`

```python
# -*- coding: utf-8 -*-
# recognition.py — Pipeline orchestrator
# BlueCollar Systems — BUILT. NOT BOUGHT.
"""
Modes: none, generic, auto
Generic recognition runs document profiling, circle/boundary detection,
table/title block detection, and dimension association.
"""
from __future__ import annotations
from .primitives import PageData, RecognitionConfig
from . import generic_recognizer as generic_rec
from . import document_profiler as profiler


def run(page_data: PageData, mode: str = "auto", config: RecognitionConfig = None):
    if config is None:
        config = RecognitionConfig()
    if mode == "none":
        return {"generic": None, "mode_used": "none"}

    generic = generic_rec.analyze(page_data, config)

    if mode == "auto":
        profile = profiler.profile(page_data)
        effective = profile.primary_type if profile else "generic"
    else:
        effective = mode

    return {"generic": generic, "mode_used": effective}
```

### PDFVectorImporter/pdfcadcore/regions.py

- Path: `PDFVectorImporter/pdfcadcore/regions.py`
- Size: `2.27 KB`
- Modified: `2026-04-03 19:02:39`

```python
# -*- coding: utf-8 -*-
# regions.py — Region segmentation
# BlueCollar Systems — BUILT. NOT BOUGHT.
from __future__ import annotations
from .primitives import Region, PageData, next_id


def segment(page_data: PageData, config=None) -> list:
    """Split page into logical detail regions using spatial clustering."""
    prims = page_data.primitives
    if not prims:
        return []

    gap = 50.0  # mm
    cell = gap * 3

    cells = {}
    for p in prims:
        if not p.bbox: continue
        cx = (p.bbox[0]+p.bbox[2])/2
        cy = (p.bbox[1]+p.bbox[3])/2
        key = (int(cx/cell), int(cy/cell))
        cells.setdefault(key, []).append(p)

    parent = {k:k for k in cells}
    def find(x):
        while parent[x] != x: parent[x] = parent[parent[x]]; x = parent[x]
        return x
    def unite(a,b):
        ra,rb = find(a),find(b)
        if ra!=rb: parent[ra]=rb

    for key in cells:
        gx,gy = key
        for dx in range(-1,2):
            for dy in range(-1,2):
                nb = (gx+dx,gy+dy)
                if nb in cells: unite(key,nb)

    groups = {}
    for key, ps in cells.items():
        root = find(key)
        groups.setdefault(root,[]).extend(ps)

    regions = []
    for cluster in groups.values():
        if len(cluster) < 3: continue
        xs = [v for p in cluster for v in (p.bbox[0],p.bbox[2]) if p.bbox]
        ys = [v for p in cluster for v in (p.bbox[1],p.bbox[3]) if p.bbox]
        if not xs: continue
        bbox = (min(xs),min(ys),max(xs),max(ys))
        r = Region(id=next_id(), page_number=page_data.page_number,
            bbox=bbox, primitive_ids=[p.id for p in cluster],
            region_type="unknown", label=f"Region_{len(regions)}")
        regions.append(r)

    _classify(regions, page_data)
    return regions


def _classify(regions, page_data):
    ph = page_data.height
    for r in regions:
        if not r.bbox: continue
        if r.bbox[1] < ph * 0.15 and r.bbox[3] < ph * 0.3:
            r.is_titleblock = True
            r.region_type = "title_block"
            r.label = "TitleBlock"
            r.confidence = 0.80
        elif len(r.primitive_ids) > 50:
            r.region_type = "assembly"
            r.label = "Assembly"
        else:
            r.region_type = "detail"
            r.label = f"Detail_{r.id}"
```

### PDFVectorImporter/pdfcadcore/validation.py

- Path: `PDFVectorImporter/pdfcadcore/validation.py`
- Size: `1.27 KB`
- Modified: `2026-04-03 19:02:39`

```python
# -*- coding: utf-8 -*-
# validation.py — Confidence and validation layer
# BlueCollar Systems — BUILT. NOT BOUGHT.
from __future__ import annotations


def validate_recognition(recognition_result: dict) -> dict:
    """Post-process recognition results with final validation pass."""
    if not recognition_result or not recognition_result.get("domain"):
        return recognition_result

    domain = recognition_result["domain"]
    plates = domain.get("plates", [])
    holes = domain.get("holes", [])

    for plate in plates:
        if plate.thickness_note and plate.width_geom and plate.height_geom:
            plate.evidence.append(
                f"Dimensions: {plate.width_geom:.1f} x {plate.height_geom:.1f}mm, "
                f"thickness={plate.thickness_note}")

    for hole in holes:
        if hole.inside_plate_id is None and hole.confidence > 0.5:
            hole.warnings.append("Hole not inside any detected plate")

    return recognition_result


CONFIDENCE_THRESHOLDS = {
    "trusted":    0.85,
    "build_warn": 0.75,
    "candidate":  0.60,
    "report_only": 0.0,
}

def action_for_confidence(score: float) -> str:
    if score >= 0.85: return "trusted"
    if score >= 0.75: return "build_warn"
    if score >= 0.60: return "candidate"
    return "report_only"
```

### PDFVectorImporter/PDFImportHandler.py

- Path: `PDFVectorImporter/PDFImportHandler.py`
- Size: `6.04 KB`
- Modified: `2026-04-03 19:07:19`

```python
# -*- coding: utf-8 -*-
# PDFImportHandler.py — FreeCAD file import handler for .pdf
# BlueCollar Systems — BUILT. NOT BOUGHT.
#
# FreeCAD calls open() when a .pdf is opened (drag-drop, File→Open)
# and insert() when File→Import is used into an existing document.
#
# Both paths can either:
#   - Show the full options dialog (if GUI is up)
#   - Import silently with defaults (headless / batch mode)
import os
import sys

import FreeCAD

# Ensure our src and lib directories are importable
_candidates = []
for root in (FreeCAD.getUserAppDataDir(), FreeCAD.getResourceDir()):
    d = os.path.join(root, "Mod", "PDFVectorImporter")
    if os.path.isdir(d):
        _candidates.append(d)
        break

for _base in _candidates:
    _src = os.path.join(_base, "src")
    _lib = os.path.join(_src, "lib")
    for _p in (os.path.dirname(_base), _base, _src):
        if not _p:
            continue
        try:
            while _p in sys.path:
                sys.path.remove(_p)
        except (AttributeError, ValueError):
            pass
        sys.path.insert(0, _p)
    if os.path.isdir(_lib):
        try:
            while _lib in sys.path:
                sys.path.remove(_lib)
        except (AttributeError, ValueError):
            pass
        sys.path.insert(0, _lib)


def open(filename, docname=None):
    """Called by FreeCAD when a PDF is opened (drag-drop, File→Open).
    Creates a new document and imports into it."""
    if not _check_fitz():
        return

    # Create a new document named after the PDF
    basename = os.path.splitext(os.path.basename(filename))[0]
    doc = FreeCAD.newDocument(docname or basename)
    FreeCAD.setActiveDocument(doc.Name)

    _do_import(filename)


def insert(filename, docname):
    """Called by FreeCAD when a PDF is imported into an existing document."""
    if not _check_fitz():
        return

    try:
        doc = FreeCAD.getDocument(docname)
    except (RuntimeError, TypeError, ValueError):
        doc = None

    if doc is None:
        doc = FreeCAD.newDocument(docname or "PDF_Import")
    FreeCAD.setActiveDocument(doc.Name)

    _do_import(filename)


def _check_fitz():
    """Verify PyMuPDF is available; show install prompt if not."""
    try:
        import fitz  # noqa: F401
        return True
    except ImportError:
        pass

    FreeCAD.Console.PrintError(
        "PyMuPDF is not installed. Switch to the PDF Vector Importer "
        "workbench to install it automatically.\n")

    if FreeCAD.GuiUp:
        try:
            from PySide6 import QtWidgets
        except ImportError:
            from PySide2 import QtWidgets
        QtWidgets.QMessageBox.warning(
            None, "PyMuPDF Required",
            "PyMuPDF is not installed yet.\n\n"
            "Switch to the PDF Vector Importer workbench\n"
            "and it will install automatically.")
    return False


def _do_import(filename):
    """Run the import — show dialog if GUI is up, otherwise use defaults."""
    if FreeCAD.GuiUp:
        _import_with_dialog(filename)
    else:
        _import_headless(filename)


def _import_with_dialog(filename):
    """Show the options dialog pre-filled with the dropped file."""
    try:
        from PDFImporterCmd import ImportPDFDialog
        import PDFVectorImporter.src.PDFImporterCore as core
    except ImportError:
        # Fallback: try direct import
        try:
            import PDFImporterCore as core
            from PDFImporterCmd import ImportPDFDialog
        except ImportError as e:
            FreeCAD.Console.PrintError(f"Cannot load importer: {e}\n")
            return

    dlg = ImportPDFDialog()
    dlg.file_edit.setText(filename)

    # Pre-populate page count
    try:
        import fitz
        with fitz.open(filename) as doc:
            page_count = doc.page_count
        dlg._page_count = page_count
        dlg.page_edit.setPlaceholderText(
            f"1-{page_count}  (PDF has {page_count} pages)")
    except (ImportError, OSError, RuntimeError, ValueError):
        pass

    try:
        from PySide6 import QtWidgets
    except ImportError:
        from PySide2 import QtWidgets

    exec_fn = getattr(dlg, "exec", None) or getattr(dlg, "exec_", None)
    if exec_fn is None or exec_fn() != QtWidgets.QDialog.Accepted:
        return

    opts = dlg.build_options()
    try:
        core.import_pdf(filename, opts)
        FreeCAD.Console.PrintMessage("PDF import complete.\n")

        # Fit view
        try:
            import FreeCADGui
            if FreeCADGui.ActiveDocument and FreeCADGui.ActiveDocument.ActiveView:
                FreeCADGui.ActiveDocument.ActiveView.fitAll()
        except (ImportError, AttributeError, RuntimeError):
            pass
    except (RuntimeError, ValueError, TypeError, OSError, AttributeError, ImportError) as e:
        import traceback
        FreeCAD.Console.PrintError(f"Import failed: {e}\n{traceback.format_exc()}")
        try:
            from PySide6 import QtWidgets
        except ImportError:
            from PySide2 import QtWidgets

        # Provide targeted error messages for common failure modes
        msg = str(e)
        if "encrypt" in msg.lower():
            title = "Encrypted PDF"
        elif "fitz" in msg.lower() or "pymupdf" in msg.lower():
            title = "PyMuPDF Error"
        else:
            title = "Import Failed"
        QtWidgets.QMessageBox.critical(None, title, msg)


def _import_headless(filename):
    """Import with default options (no GUI)."""
    try:
        import PDFVectorImporter.src.PDFImporterCore as core
    except ImportError:
        import PDFImporterCore as core

    opts = core.ImportOptions()
    try:
        core.import_pdf(filename, opts)
        FreeCAD.Console.PrintMessage("PDF import complete.\n")
    except (RuntimeError, ValueError, TypeError, OSError, AttributeError, ImportError) as e:
        import traceback
        FreeCAD.Console.PrintError(f"Import failed: {e}\n{traceback.format_exc()}")


```

### PDFVectorImporter/PDFTools.py

- Path: `PDFVectorImporter/PDFTools.py`
- Size: `12.66 KB`
- Modified: `2026-03-27 16:20:42`

```python
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
            ver_str = ".".join(str(v) for v in ver) if isinstance(ver, (tuple, list)) else str(ver)
            _msg(f"  PyMuPDF:  version={ver_str}  file={getattr(fitz, '__file__', '?')}")
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
            _warn(f"  Page spec '{part}' is not a valid page number — skipped.")
            continue
    if not out:
        _warn(f"  Page spec '{spec}' produced no valid pages — defaulting to page 1.")
        return [1]
    return out
```

### PDFVectorImporter/qa_config_example.json

- Path: `PDFVectorImporter/qa_config_example.json`
- Size: `1.45 KB`
- Modified: `2026-04-03 18:32:56`

```json
{
  "workspace": ".",
  "adapters": {
    "sketchup": {
      "command": "python adapters/sketchup_adapter.py --config qa_config.json --test-id {test_id} --input \"{input}\"",
      "timeout_seconds": 300
    },
    "freecad": {
      "command": "python adapters/freecad_adapter.py --config qa_config.json --test-id {test_id} --input \"{input}\"",
      "timeout_seconds": 300
    },
    "blender": {
      "command": "python adapters/blender_adapter.py --config qa_config.json --test-id {test_id} --input \"{input}\"",
      "timeout_seconds": 600
    },
    "librecad": {
      "command": "python adapters/librecad_adapter.py --config qa_config.json --test-id {test_id} --input \"{input}\"",
      "timeout_seconds": 600
    }
  },
  "sketchup": {
    "exe": "C:/Program Files/SketchUp/SketchUp 2017/SketchUp.exe",
    "plugins_dir": "%APPDATA%/SketchUp/SketchUp 2017/SketchUp/Plugins",
    "extension_root": "%APPDATA%/SketchUp/SketchUp 2017/SketchUp/Plugins/bc_pdf_vector_importer",
    "ruby_harness": "adapters/sketchup_harness.rb"
  },
  "freecad": {
    "freecadcmd_exe": "C:/Program Files/FreeCAD 1.0/bin/FreeCADCmd.exe",
    "mod_dir": "%APPDATA%/FreeCAD/Mod/PDFVectorImporter",
    "python_harness": "adapters/freecad_harness.py"
  },
  "blender": {
    "repo_dir": "C:/1BL-PDFimporter",
    "python_exe": "python",
    "timeout_seconds": 600
  },
  "librecad": {
    "repo_dir": "C:/1LC-PDFimporter",
    "python_exe": "python",
    "timeout_seconds": 600
  }
}
```

### PDFVectorImporter/qa_config_local_live.json

- Path: `PDFVectorImporter/qa_config_local_live.json`
- Size: `1.02 KB`
- Modified: `2026-03-29 20:42:53`

```json
{
  "workspace": "C:/1FC-PDFimporter/PDFVectorImporter",
  "adapters": {
    "sketchup": {
      "command": "python adapters/sketchup_adapter.py --config qa_config_local_live.json --test-id {test_id} --input \"{input}\" --preset \"{test_name}\"",
      "timeout_seconds": 420
    },
    "freecad": {
      "command": "python adapters/freecad_adapter.py --config qa_config_local_live.json --test-id {test_id} --input \"{input}\" --preset \"{test_name}\"",
      "timeout_seconds": 1800
    }
  },
  "sketchup": {
    "automation_supported": true,
    "exe": "C:/Program Files/SketchUp/SketchUp 2017/SketchUp.exe",
    "plugins_dir": "%APPDATA%/SketchUp/SketchUp 2017/SketchUp/Plugins",
    "extension_root": "%APPDATA%/SketchUp/SketchUp 2017/SketchUp/Plugins/bc_pdf_vector_importer",
    "ruby_harness": "adapters/sketchup_harness.rb"
  },
  "freecad": {
    "freecadcmd_exe": "C:/Program Files/FreeCAD 1.1/bin/FreeCADCmd.exe",
    "mod_dir": "%APPDATA%/FreeCAD/Mod/PDFVectorImporter",
    "python_harness": "adapters/freecad_harness.py"
  }
}
```

### PDFVectorImporter/qa_config_template.json

- Path: `PDFVectorImporter/qa_config_template.json`
- Size: `1.55 KB`
- Modified: `2026-04-03 18:32:48`

```json
{
  "workspace": "<YOUR_WORKSPACE_DIR>",
  "adapters": {
    "sketchup": {
      "command": "python adapters/sketchup_adapter.py --config qa_config_local_full.json --test-id {test_id} --input \"{input}\"",
      "timeout_seconds": 420
    },
    "freecad": {
      "command": "python adapters/freecad_adapter.py --config qa_config_local_full.json --test-id {test_id} --input \"{input}\"",
      "timeout_seconds": 1800
    },
    "blender": {
      "command": "python adapters/blender_adapter.py --config qa_config_local_full.json --test-id {test_id} --input \"{input}\"",
      "timeout_seconds": 1800
    },
    "librecad": {
      "command": "python adapters/librecad_adapter.py --config qa_config_local_full.json --test-id {test_id} --input \"{input}\"",
      "timeout_seconds": 1800
    }
  },
  "sketchup": {
    "automation_supported": false,
    "exe": "<PATH_TO_SKETCHUP_EXE>",
    "plugins_dir": "%APPDATA%/SketchUp/SketchUp 2017/SketchUp/Plugins",
    "extension_root": "%APPDATA%/SketchUp/SketchUp 2017/SketchUp/Plugins/bc_pdf_vector_importer",
    "ruby_harness": "adapters/sketchup_harness.rb"
  },
  "freecad": {
    "freecadcmd_exe": "<PATH_TO_FREECADCMD_EXE>",
    "mod_dir": "<PATH_TO_FREECAD_MOD_DIR>/PDFVectorImporter",
    "python_harness": "adapters/freecad_harness.py"
  },
  "blender": {
    "repo_dir": "C:/1BL-PDFimporter",
    "python_exe": "<PATH_TO_PYTHON_EXE_OPTIONAL>",
    "timeout_seconds": 1800
  },
  "librecad": {
    "repo_dir": "C:/1LC-PDFimporter",
    "python_exe": "<PATH_TO_PYTHON_EXE_OPTIONAL>",
    "timeout_seconds": 1800
  }
}
```

### PDFVectorImporter/qa_results.json

- Path: `PDFVectorImporter/qa_results.json`
- Size: `356.00 B`
- Modified: `2026-04-04 03:50:14`

```json
{
  "total": 1,
  "passed": 1,
  "failed": 0,
  "blocked": 0,
  "p0_failed": 0,
  "results": [
    {
      "test_id": "LC-SMOKE-001",
      "platform": "LC",
      "priority": "P0",
      "automation": "AUTO",
      "result": "Pass",
      "runtime_seconds": 1.074,
      "notes": "Exported 293 entities. | adapter_status=PASS"
    }
  ]
}
```

### PDFVectorImporter/qa_runs/20260329_205803/fc_verify_map.json

- Path: `PDFVectorImporter/qa_runs/20260329_205803/fc_verify_map.json`
- Size: `1.90 KB`
- Modified: `2026-03-29 20:58:14`

```json
{
  "test_id": "FC-VERIFY-MAP",
  "platform": "FC",
  "status": "PASS",
  "message": "Import completed.",
  "started_at": "2026-03-30T01:58:05Z",
  "mod_dir": "C:\\Users\\Rowdy Payton\\AppData\\Roaming\\FreeCAD\\Mod\\PDFVectorImporter",
  "sys_path_head": [
    "C:\\Users\\Rowdy Payton\\AppData\\Roaming\\FreeCAD\\Mod\\PDFVectorImporter\\src",
    "C:\\Users\\Rowdy Payton\\AppData\\Roaming\\FreeCAD\\Mod\\PDFVectorImporter",
    "C:\\Users\\Rowdy Payton\\AppData\\Roaming\\FreeCAD\\Mod",
    "C:\\Users\\Rowdy Payton\\AppData\\Roaming\\FreeCAD\\v1-1\\Mod\\PDFVectorImporter\\.\\",
    "C:\\Users\\Rowdy Payton\\AppData\\Roaming\\FreeCAD\\v1-1\\Mod\\PDFVectorImporter",
    "C:\\Users\\Rowdy Payton\\AppData\\Roaming\\FreeCAD\\v1-1\\Mod\\CombineFiles_SingleText_Clear.ps1",
    "C:\\Users\\Rowdy Payton\\AppData\\Roaming\\FreeCAD\\v1-1\\Mod\\CombineFiles_SingleText_Clear.bat",
    "C:\\Program Files\\FreeCAD 1.1\\Mod\\Web",
    "C:\\Program Files\\FreeCAD 1.1\\Mod\\Tux",
    "C:\\Program Files\\FreeCAD 1.1\\Mod\\Test",
    "C:\\Program Files\\FreeCAD 1.1\\Mod\\TechDraw",
    "C:\\Program Files\\FreeCAD 1.1\\Mod\\Surface"
  ],
  "pymupdf": {
    "status": "available_from_lib_dir",
    "installed_now": false,
    "lib_dir": "C:\\Users\\Rowdy Payton\\AppData\\Roaming\\FreeCAD\\Mod\\PDFVectorImporter\\src\\lib"
  },
  "input_pdf": "C:\\Users\\Rowdy Payton\\Downloads\\TX_Alvord_20220525_TM_geo.pdf",
  "preset": "Shop Drawing",
  "page_range": "1",
  "pages": [
    1
  ],
  "counts_before": {
    "objects_total": 0,
    "groups": 0,
    "wires": 0,
    "faces": 0,
    "texts": 0
  },
  "counts_after": {
    "objects_total": 2,
    "groups": 1,
    "wires": 0,
    "faces": 0,
    "texts": 0
  },
  "counts_delta": {
    "objects_total": 2,
    "groups": 1,
    "wires": 0,
    "faces": 0,
    "texts": 0
  },
  "finished_at": "2026-03-30T01:58:14Z",
  "runtime_seconds": 8.456
}
```

### PDFVectorImporter/qa_runs/20260329_205803/fc_verify_plant.json

- Path: `PDFVectorImporter/qa_runs/20260329_205803/fc_verify_plant.json`
- Size: `1.92 KB`
- Modified: `2026-03-29 20:58:16`

```json
{
  "test_id": "FC-VERIFY-PLANT",
  "platform": "FC",
  "status": "PASS",
  "message": "Import completed.",
  "started_at": "2026-03-30T01:58:14Z",
  "mod_dir": "C:\\Users\\Rowdy Payton\\AppData\\Roaming\\FreeCAD\\Mod\\PDFVectorImporter",
  "sys_path_head": [
    "C:\\Users\\Rowdy Payton\\AppData\\Roaming\\FreeCAD\\Mod\\PDFVectorImporter\\src",
    "C:\\Users\\Rowdy Payton\\AppData\\Roaming\\FreeCAD\\Mod\\PDFVectorImporter",
    "C:\\Users\\Rowdy Payton\\AppData\\Roaming\\FreeCAD\\Mod",
    "C:\\Users\\Rowdy Payton\\AppData\\Roaming\\FreeCAD\\v1-1\\Mod\\PDFVectorImporter\\.\\",
    "C:\\Users\\Rowdy Payton\\AppData\\Roaming\\FreeCAD\\v1-1\\Mod\\PDFVectorImporter",
    "C:\\Users\\Rowdy Payton\\AppData\\Roaming\\FreeCAD\\v1-1\\Mod\\CombineFiles_SingleText_Clear.ps1",
    "C:\\Users\\Rowdy Payton\\AppData\\Roaming\\FreeCAD\\v1-1\\Mod\\CombineFiles_SingleText_Clear.bat",
    "C:\\Program Files\\FreeCAD 1.1\\Mod\\Web",
    "C:\\Program Files\\FreeCAD 1.1\\Mod\\Tux",
    "C:\\Program Files\\FreeCAD 1.1\\Mod\\Test",
    "C:\\Program Files\\FreeCAD 1.1\\Mod\\TechDraw",
    "C:\\Program Files\\FreeCAD 1.1\\Mod\\Surface"
  ],
  "pymupdf": {
    "status": "available_from_lib_dir",
    "installed_now": false,
    "lib_dir": "C:\\Users\\Rowdy Payton\\AppData\\Roaming\\FreeCAD\\Mod\\PDFVectorImporter\\src\\lib"
  },
  "input_pdf": "C:\\Users\\Rowdy Payton\\Downloads\\alvord_plant_list.pdf",
  "preset": "Shop Drawing",
  "page_range": "all",
  "pages": [
    1,
    2
  ],
  "counts_before": {
    "objects_total": 0,
    "groups": 0,
    "wires": 0,
    "faces": 0,
    "texts": 0
  },
  "counts_after": {
    "objects_total": 309,
    "groups": 10,
    "wires": 123,
    "faces": 87,
    "texts": 0
  },
  "counts_delta": {
    "objects_total": 309,
    "groups": 10,
    "wires": 123,
    "faces": 87,
    "texts": 0
  },
  "finished_at": "2026-03-30T01:58:16Z",
  "runtime_seconds": 1.385
}
```

### PDFVectorImporter/qa_runs/20260329_205803/fc_verify_weld.json

- Path: `PDFVectorImporter/qa_runs/20260329_205803/fc_verify_weld.json`
- Size: `1.91 KB`
- Modified: `2026-03-29 20:58:05`

```json
{
  "test_id": "FC-VERIFY-WELD",
  "platform": "FC",
  "status": "PASS",
  "message": "Import completed.",
  "started_at": "2026-03-30T01:58:03Z",
  "mod_dir": "C:\\Users\\Rowdy Payton\\AppData\\Roaming\\FreeCAD\\Mod\\PDFVectorImporter",
  "sys_path_head": [
    "C:\\Users\\Rowdy Payton\\AppData\\Roaming\\FreeCAD\\Mod\\PDFVectorImporter\\src",
    "C:\\Users\\Rowdy Payton\\AppData\\Roaming\\FreeCAD\\Mod\\PDFVectorImporter",
    "C:\\Users\\Rowdy Payton\\AppData\\Roaming\\FreeCAD\\Mod",
    "C:\\Users\\Rowdy Payton\\AppData\\Roaming\\FreeCAD\\v1-1\\Mod\\PDFVectorImporter\\.\\",
    "C:\\Users\\Rowdy Payton\\AppData\\Roaming\\FreeCAD\\v1-1\\Mod\\PDFVectorImporter",
    "C:\\Users\\Rowdy Payton\\AppData\\Roaming\\FreeCAD\\v1-1\\Mod\\CombineFiles_SingleText_Clear.ps1",
    "C:\\Users\\Rowdy Payton\\AppData\\Roaming\\FreeCAD\\v1-1\\Mod\\CombineFiles_SingleText_Clear.bat",
    "C:\\Program Files\\FreeCAD 1.1\\Mod\\Web",
    "C:\\Program Files\\FreeCAD 1.1\\Mod\\Tux",
    "C:\\Program Files\\FreeCAD 1.1\\Mod\\Test",
    "C:\\Program Files\\FreeCAD 1.1\\Mod\\TechDraw",
    "C:\\Program Files\\FreeCAD 1.1\\Mod\\Surface"
  ],
  "pymupdf": {
    "status": "available_from_lib_dir",
    "installed_now": false,
    "lib_dir": "C:\\Users\\Rowdy Payton\\AppData\\Roaming\\FreeCAD\\Mod\\PDFVectorImporter\\src\\lib"
  },
  "input_pdf": "C:\\Users\\Rowdy Payton\\Downloads\\Welding-Symbol-Chart OCR.pdf",
  "preset": "Shop Drawing",
  "page_range": "1",
  "pages": [
    1
  ],
  "counts_before": {
    "objects_total": 0,
    "groups": 0,
    "wires": 0,
    "faces": 0,
    "texts": 0
  },
  "counts_after": {
    "objects_total": 543,
    "groups": 12,
    "wires": 631,
    "faces": 127,
    "texts": 0
  },
  "counts_delta": {
    "objects_total": 543,
    "groups": 12,
    "wires": 631,
    "faces": 127,
    "texts": 0
  },
  "finished_at": "2026-03-30T01:58:05Z",
  "runtime_seconds": 1.784
}
```

### PDFVectorImporter/qa_runs/20260329_205803/su_manual_probe/autoload_probe_marker.txt

- Path: `PDFVectorImporter/qa_runs/20260329_205803/su_manual_probe/autoload_probe_marker.txt`
- Size: `21.00 B`
- Modified: `2026-03-29 21:10:27`

```text
PLUGIN_AUTOLOAD_RAN
```

### PDFVectorImporter/qa_runs/20260329_205803/su_manual_probe/env_probe_marker.txt

- Path: `PDFVectorImporter/qa_runs/20260329_205803/su_manual_probe/env_probe_marker.txt`
- Size: `158.00 B`
- Modified: `2026-03-29 21:10:27`

```text
C:\1FC-PDFimporter\PDFVectorImporter\qa_runs\20260329_205803\su_manual_probe\payload.json
C:\1FC-PDFimporter\PDFVectorImporter\adapters\sketchup_harness.rb
```

### PDFVectorImporter/qa_runs/20260329_205803/su_manual_probe/harness_debug_log.txt

- Path: `PDFVectorImporter/qa_runs/20260329_205803/su_manual_probe/harness_debug_log.txt`
- Size: `846.00 B`
- Modified: `2026-03-29 21:10:27`

~~~text
START
payload=C:\1FC-PDFimporter\PDFVectorImporter\qa_runs\20260329_205803\su_manual_probe\payload.json
harness=C:\1FC-PDFimporter\PDFVectorImporter\adapters\sketchup_harness.rb
payload_exists=true
harness_exists=true
LOAD_ERROR: SyntaxError: C:/1FC-PDFimporter/PDFVectorImporter/adapters/sketchup_harness.rb:110: syntax error, unexpected keyword_rescue, expecting keyword_end
      rescue LoadError
            ^
C:/1FC-PDFimporter/PDFVectorImporter/adapters/sketchup_harness.rb:112: syntax error, unexpected keyword_rescue, expecting keyword_end
      rescue StandardError
            ^
C:/Users/Rowdy Payton/AppData/Roaming/SketchUp/SketchUp 2017/SketchUp/Plugins/zz_probe_harness_debug.rb:9:in `load'
C:/Users/Rowdy Payton/AppData/Roaming/SketchUp/SketchUp 2017/SketchUp/Plugins/zz_probe_harness_debug.rb:9:in `<top (required)>'
~~~

### PDFVectorImporter/qa_runs/20260329_205803/su_manual_probe/harness_debug_map_log.txt

- Path: `PDFVectorImporter/qa_runs/20260329_205803/su_manual_probe/harness_debug_map_log.txt`
- Size: `1.14 KB`
- Modified: `2026-03-29 21:20:02`

~~~text
START
payload=C:\1FC-PDFimporter\PDFVectorImporter\qa_runs\20260329_205803\su_manual_probe\payload_map.json
harness=C:\1FC-PDFimporter\PDFVectorImporter\adapters\sketchup_harness.rb
payload_exists=true
harness_exists=true
LOAD_ERROR: Encoding::UndefinedConversionError: "\xFE" from ASCII-8BIT to UTF-8
C:/Program Files/SketchUp/SketchUp 2017/Tools/RubyStdLib/json/common.rb:285:in `encode'
C:/Program Files/SketchUp/SketchUp 2017/Tools/RubyStdLib/json/common.rb:285:in `generate'
C:/Program Files/SketchUp/SketchUp 2017/Tools/RubyStdLib/json/common.rb:285:in `pretty_generate'
C:/1FC-PDFimporter/PDFVectorImporter/adapters/sketchup_harness.rb:73:in `block in run'
C:/1FC-PDFimporter/PDFVectorImporter/adapters/sketchup_harness.rb:73:in `open'
C:/1FC-PDFimporter/PDFVectorImporter/adapters/sketchup_harness.rb:73:in `run'
C:/1FC-PDFimporter/PDFVectorImporter/adapters/sketchup_harness.rb:190:in `<top (required)>'
C:/Users/Rowdy Payton/AppData/Roaming/SketchUp/SketchUp 2017/SketchUp/Plugins/zz_probe_harness_debug.rb:9:in `load'
C:/Users/Rowdy Payton/AppData/Roaming/SketchUp/SketchUp 2017/SketchUp/Plugins/zz_probe_harness_debug.rb:9:in `<top (required)>'
~~~

### PDFVectorImporter/qa_runs/20260329_205803/su_manual_probe/json_probe_marker.txt

- Path: `PDFVectorImporter/qa_runs/20260329_205803/su_manual_probe/json_probe_marker.txt`
- Size: `9.00 B`
- Modified: `2026-03-29 21:10:27`

```text
JSON_OK
```

### PDFVectorImporter/qa_runs/20260329_205803/su_manual_probe/payload.json

- Path: `PDFVectorImporter/qa_runs/20260329_205803/su_manual_probe/payload.json`
- Size: `832.00 B`
- Modified: `2026-03-29 21:10:17`

```json
{
  "page_range": "1",
  "preset": "Full",
  "test_id": "SU-DEBUG-HARNESS",
  "input_pdf": "C:/Users/Rowdy Payton/Downloads/Welding-Symbol-Chart OCR.pdf",
  "result_json": "C:\\1FC-PDFimporter\\PDFVectorImporter\\qa_runs\\20260329_205803\\su_manual_probe\\result.json",
  "platform": "SU",
  "adapter": "sketchup",
  "expected": {
    "layers_min_populated": 0,
    "runtime_cap_seconds": 120
  },
  "timestamp_utc": "2026-03-30T02:10:17Z",
  "plugins_dir": "C:\\Users\\Rowdy Payton\\AppData\\Roaming/SketchUp/SketchUp 2017/SketchUp/Plugins",
  "notes": "harness debug",
  "output_dir": null,
  "extension_root": "C:\\Users\\Rowdy Payton\\AppData\\Roaming/SketchUp/SketchUp 2017/SketchUp/Plugins/bc_pdf_vector_importer",
  "ruby_harness": "C:\\1FC-PDFimporter\\PDFVectorImporter\\adapters\\sketchup_harness.rb"
}
```

### PDFVectorImporter/qa_runs/20260329_205803/su_manual_probe/payload_map.json

- Path: `PDFVectorImporter/qa_runs/20260329_205803/su_manual_probe/payload_map.json`
- Size: `837.00 B`
- Modified: `2026-03-29 21:19:35`

```json
{
  "page_range": "1",
  "output_dir": null,
  "extension_root": "C:\\Users\\Rowdy Payton\\AppData\\Roaming/SketchUp/SketchUp 2017/SketchUp/Plugins/bc_pdf_vector_importer",
  "timestamp_utc": "2026-03-30T02:19:35Z",
  "ruby_harness": "C:\\1FC-PDFimporter\\PDFVectorImporter\\adapters\\sketchup_harness.rb",
  "platform": "SU",
  "input_pdf": "C:/Users/Rowdy Payton/Downloads/TX_Alvord_20220525_TM_geo.pdf",
  "test_id": "SU-DEBUG-MAP",
  "plugins_dir": "C:\\Users\\Rowdy Payton\\AppData\\Roaming/SketchUp/SketchUp 2017/SketchUp/Plugins",
  "expected": {
    "runtime_cap_seconds": 300,
    "layers_min_populated": 0
  },
  "result_json": "C:\\1FC-PDFimporter\\PDFVectorImporter\\qa_runs\\20260329_205803\\su_manual_probe\\result_map.json",
  "preset": "Full",
  "notes": "harness debug map",
  "adapter": "sketchup"
}
```

### PDFVectorImporter/qa_runs/20260329_205803/su_manual_probe/result.json

- Path: `PDFVectorImporter/qa_runs/20260329_205803/su_manual_probe/result.json`
- Size: `443.00 B`
- Modified: `2026-03-29 21:10:27`

```json
{
  "platform": "SU",
  "status": "FAIL",
  "message": "Bootstrap error: SyntaxError: C:/1FC-PDFimporter/PDFVectorImporter/adapters/sketchup_harness.rb:110: syntax error, unexpected keyword_rescue, expecting keyword_end\n      rescue LoadError\n            ^\nC:/1FC-PDFimporter/PDFVectorImporter/adapters/sketchup_harness.rb:112: syntax error, unexpected keyword_rescue, expecting keyword_end\n      rescue StandardError\n            ^"
}
```

### PDFVectorImporter/qa_runs/20260329_205803/su_manual_probe/result_map.json

- Path: `PDFVectorImporter/qa_runs/20260329_205803/su_manual_probe/result_map.json`
- Size: `0.00 B`
- Modified: `2026-03-29 21:20:02`

```json

```

### PDFVectorImporter/qa_runs/20260329_205803/su_manual_probe/startup_probe.rb

- Path: `PDFVectorImporter/qa_runs/20260329_205803/su_manual_probe/startup_probe.rb`
- Size: `153.00 B`
- Modified: `2026-03-29 21:06:00`

```ruby
File.open('C:/1FC-PDFimporter/PDFVectorImporter/qa_runs/20260329_205803/su_manual_probe/startup_probe_marker.txt','w'){|f| f.puts('RUBY_STARTUP_RAN') }
```

### PDFVectorImporter/qa_runs/20260329_205803/su_smoke_test.txt

- Path: `PDFVectorImporter/qa_runs/20260329_205803/su_smoke_test.txt`
- Size: `913.00 B`
- Modified: `2026-03-29 20:58:18`

```text
============================================================
PDF Vector Importer -- Smoke Tests
============================================================

--- Check 1: Ruby syntax on all .rb files ---
  33/33 files passed syntax check

--- Check 2: Main entry point loadability ---
  PASS: extracted/sketchup_ext/bc_pdf_vector_importer.rb parses without error
  PASS: extracted/sketchup_ext/bc_pdf_vector_importer/main.rb parses without error
  PASS: logger.rb loads and executes standalone

--- Check 3: .rbz package validity ---
  PASS: bc_pdf_vector_importer_v3.5.0.rbz is a valid zip archive (33 entries)

--- Check 4: no bare/silent rescue patterns in core extension ---
  PASS: no 'rescue nil' / bare 'rescue => e' patterns found

============================================================
ALL CHECKS PASSED (38 checks)
============================================================
```

### PDFVectorImporter/qa_runs/20260329_205803/su_verify_map.json

- Path: `PDFVectorImporter/qa_runs/20260329_205803/su_verify_map.json`
- Size: `2.04 KB`
- Modified: `2026-03-29 21:25:16`

```json
{
  "test_id": "SU-VERIFY-MAP",
  "platform": "SU",
  "status": "PASS",
  "message": "Import completed.",
  "started_at": "2026-03-30T02:24:59Z",
  "loader": "C:/Users/Rowdy Payton/AppData/Roaming/SketchUp/SketchUp 2017/SketchUp/Plugins/bc_pdf_vector_importer/main",
  "input_pdf": "C:\\Users\\Rowdy Payton\\Downloads\\TX_Alvord_20220525_TM_geo.pdf",
  "preset": "Full",
  "page_range": "1",
  "pipeline_stats": {
    "pages": 1,
    "primitives": 0,
    "edges": 0,
    "faces": 0,
    "arcs": 0,
    "text": 0,
    "components": 0,
    "layers": [
      "??\u0000L\u0000a\u0000b\u0000e\u0000l\u0000s",
      "Map Collar",
      "Map Elements",
      "Map Frame",
      "Boundaries",
      "Federal Administrated Lands",
      "Forest Service",
      "Jurisdictional Boundaries",
      "County or Equivalent",
      "State or Territory",
      "Woodland",
      "Terrain",
      "Shaded Relief",
      "Contours",
      "Hydrography",
      "Wetlands",
      "Transportation",
      "Airports",
      "Railroads",
      "Road Features",
      "Road Names and Shields",
      "Structures",
      "Geographic Names",
      "Projection and Grids",
      "Images",
      "Orthoimage",
      "Barcode"
    ],
    "cleanup": {},
    "generic": null,
    "mode_used": null,
    "xobjects": 0,
    "text_mode": "geometry",
    "raster_fallback_used": true,
    "elapsed_seconds": 17.2,
    "log_path": "C:/TMP/bc_pdf_importer/last_import.log"
  },
  "model_counts_before": {
    "edges": 0,
    "faces": 0,
    "groups": 0,
    "component_instances": 0,
    "texts": 0,
    "images": 0
  },
  "model_counts_after": {
    "edges": 0,
    "faces": 0,
    "groups": 0,
    "component_instances": 0,
    "texts": 0,
    "images": 1
  },
  "model_delta": {
    "edges": 0,
    "faces": 0,
    "groups": 0,
    "component_instances": 0,
    "texts": 0,
    "images": 1
  },
  "layers_before": 1,
  "layers_after": 29,
  "layers_delta": 28,
  "finished_at": "2026-03-30T02:25:16Z",
  "runtime_seconds": 17.217
}
```

### PDFVectorImporter/qa_runs/20260329_205803/su_verify_plant.json

- Path: `PDFVectorImporter/qa_runs/20260329_205803/su_verify_plant.json`
- Size: `1.49 KB`
- Modified: `2026-03-29 21:25:29`

```json
{
  "test_id": "SU-VERIFY-PLANT",
  "platform": "SU",
  "status": "PASS",
  "message": "Import completed.",
  "started_at": "2026-03-30T02:25:27Z",
  "loader": "C:/Users/Rowdy Payton/AppData/Roaming/SketchUp/SketchUp 2017/SketchUp/Plugins/bc_pdf_vector_importer/main",
  "input_pdf": "C:\\Users\\Rowdy Payton\\Downloads\\alvord_plant_list.pdf",
  "preset": "Full",
  "page_range": "all",
  "pipeline_stats": {
    "pages": 2,
    "primitives": 125,
    "edges": 11018,
    "faces": 87,
    "arcs": 0,
    "text": 2767,
    "components": 0,
    "layers": [],
    "cleanup": {
      "merged_verts": 0,
      "removed_dupes": 0,
      "removed_micro": 0,
      "joined_collinear": 0,
      "closed_gaps": 0
    },
    "generic": null,
    "mode_used": null,
    "xobjects": 0,
    "text_mode": "geometry",
    "elapsed_seconds": 1.4,
    "log_path": "C:/TMP/bc_pdf_importer/last_import.log"
  },
  "model_counts_before": {
    "edges": 0,
    "faces": 0,
    "groups": 0,
    "component_instances": 0,
    "texts": 0,
    "images": 0
  },
  "model_counts_after": {
    "edges": 10946,
    "faces": 87,
    "groups": 8,
    "component_instances": 2767,
    "texts": 0,
    "images": 0
  },
  "model_delta": {
    "edges": 10946,
    "faces": 87,
    "groups": 8,
    "component_instances": 2767,
    "texts": 0,
    "images": 0
  },
  "layers_before": 1,
  "layers_after": 4,
  "layers_delta": 3,
  "finished_at": "2026-03-30T02:25:28Z",
  "runtime_seconds": 1.442
}
```

### PDFVectorImporter/qa_runs/20260329_205803/su_verify_weld.json

- Path: `PDFVectorImporter/qa_runs/20260329_205803/su_verify_weld.json`
- Size: `1.67 KB`
- Modified: `2026-03-29 21:24:49`

```json
{
  "test_id": "SU-VERIFY-WELD",
  "platform": "SU",
  "status": "PASS",
  "message": "Import completed.",
  "started_at": "2026-03-30T02:24:41Z",
  "loader": "C:/Users/Rowdy Payton/AppData/Roaming/SketchUp/SketchUp 2017/SketchUp/Plugins/bc_pdf_vector_importer/main",
  "input_pdf": "C:\\Users\\Rowdy Payton\\Downloads\\Welding-Symbol-Chart OCR.pdf",
  "preset": "Full",
  "page_range": "1",
  "pipeline_stats": {
    "pages": 1,
    "primitives": 642,
    "edges": 1973,
    "faces": 125,
    "arcs": 51,
    "text": 361,
    "components": 0,
    "layers": [
      "Layer 1",
      "Layer 3",
      "Layer 4",
      "Layer 5",
      "Layer 6",
      "Layer 7",
      "Layer 8",
      "Layer 2",
      "Layer 9",
      "Layer 10"
    ],
    "cleanup": {
      "merged_verts": 0,
      "removed_dupes": 0,
      "removed_micro": 0,
      "joined_collinear": 0,
      "closed_gaps": 0
    },
    "generic": null,
    "mode_used": null,
    "xobjects": 1,
    "text_mode": "text3d",
    "elapsed_seconds": 7.6,
    "log_path": "C:/TMP/bc_pdf_importer/last_import.log"
  },
  "model_counts_before": {
    "edges": 0,
    "faces": 0,
    "groups": 0,
    "component_instances": 0,
    "texts": 0,
    "images": 0
  },
  "model_counts_after": {
    "edges": 70396,
    "faces": 4037,
    "groups": 3,
    "component_instances": 0,
    "texts": 0,
    "images": 0
  },
  "model_delta": {
    "edges": 70396,
    "faces": 4037,
    "groups": 3,
    "component_instances": 0,
    "texts": 0,
    "images": 0
  },
  "layers_before": 1,
  "layers_after": 13,
  "layers_delta": 12,
  "finished_at": "2026-03-30T02:24:48Z",
  "runtime_seconds": 7.67
}
```

### PDFVectorImporter/qa_runs/20260329_213208/consolidated_alvord_report.json

- Path: `PDFVectorImporter/qa_runs/20260329_213208/consolidated_alvord_report.json`
- Size: `21.70 KB`
- Modified: `2026-03-29 21:37:47`

```json
{
  "run_id": "20260329_213208",
  "outdir": "C:\\1FC-PDFimporter\\PDFVectorImporter\\qa_runs\\20260329_213208",
  "config": "C:\\1FC-PDFimporter\\PDFVectorImporter\\qa_config_local_live.json",
  "freecad": [
    {
      "test_id": "FC-ALV-01",
      "platform": "FC",
      "status": "PASS",
      "message": "Import completed.",
      "started_at": "2026-03-30T02:32:08Z",
      "mod_dir": "C:\\Users\\Rowdy Payton\\AppData\\Roaming\\FreeCAD\\Mod\\PDFVectorImporter",
      "sys_path_head": [
        "C:\\Users\\Rowdy Payton\\AppData\\Roaming\\FreeCAD\\Mod\\PDFVectorImporter\\src",
        "C:\\Users\\Rowdy Payton\\AppData\\Roaming\\FreeCAD\\Mod\\PDFVectorImporter",
        "C:\\Users\\Rowdy Payton\\AppData\\Roaming\\FreeCAD\\Mod",
        "C:\\Users\\Rowdy Payton\\AppData\\Roaming\\FreeCAD\\v1-1\\Mod\\PDFVectorImporter\\.\\",
        "C:\\Users\\Rowdy Payton\\AppData\\Roaming\\FreeCAD\\v1-1\\Mod\\PDFVectorImporter",
        "C:\\Users\\Rowdy Payton\\AppData\\Roaming\\FreeCAD\\v1-1\\Mod\\CombineFiles_SingleText_Clear.ps1",
        "C:\\Users\\Rowdy Payton\\AppData\\Roaming\\FreeCAD\\v1-1\\Mod\\CombineFiles_SingleText_Clear.bat",
        "C:\\Program Files\\FreeCAD 1.1\\Mod\\Web",
        "C:\\Program Files\\FreeCAD 1.1\\Mod\\Tux",
        "C:\\Program Files\\FreeCAD 1.1\\Mod\\Test",
        "C:\\Program Files\\FreeCAD 1.1\\Mod\\TechDraw",
        "C:\\Program Files\\FreeCAD 1.1\\Mod\\Surface"
      ],
      "pymupdf": {
        "status": "available_from_lib_dir",
        "installed_now": false,
        "lib_dir": "C:\\Users\\Rowdy Payton\\AppData\\Roaming\\FreeCAD\\Mod\\PDFVectorImporter\\src\\lib"
      },
      "input_pdf": "C:\\Users\\Rowdy Payton\\Downloads\\TX_Alvord_20220525_TM_geo.pdf",
      "preset": "Shop Drawing",
      "page_range": "all",
      "pages": [
        1
      ],
      "counts_before": {
        "objects_total": 0,
        "groups": 0,
        "wires": 0,
        "faces": 0,
        "texts": 0
      },
      "counts_after": {
        "objects_total": 2,
        "groups": 1,
        "wires": 0,
        "faces": 0,
        "texts": 0
      },
      "counts_delta": {
        "objects_total": 2,
        "groups": 1,
        "wires": 0,
        "faces": 0,
        "texts": 0
      },
      "finished_at": "2026-03-30T02:32:17Z",
      "runtime_seconds": 8.857,
      "_returncode": 0,
      "_wall_seconds": 9.518,
      "_input_pdf": "C:\\Users\\Rowdy Payton\\Downloads\\TX_Alvord_20220525_TM_geo.pdf"
    },
    {
      "test_id": "FC-ALV-02",
      "platform": "FC",
      "status": "PASS",
      "message": "Import completed.",
      "started_at": "2026-03-30T02:32:18Z",
      "mod_dir": "C:\\Users\\Rowdy Payton\\AppData\\Roaming\\FreeCAD\\Mod\\PDFVectorImporter",
      "sys_path_head": [
        "C:\\Users\\Rowdy Payton\\AppData\\Roaming\\FreeCAD\\Mod\\PDFVectorImporter\\src",
        "C:\\Users\\Rowdy Payton\\AppData\\Roaming\\FreeCAD\\Mod\\PDFVectorImporter",
        "C:\\Users\\Rowdy Payton\\AppData\\Roaming\\FreeCAD\\Mod",
        "C:\\Users\\Rowdy Payton\\AppData\\Roaming\\FreeCAD\\v1-1\\Mod\\PDFVectorImporter\\.\\",
        "C:\\Users\\Rowdy Payton\\AppData\\Roaming\\FreeCAD\\v1-1\\Mod\\PDFVectorImporter",
        "C:\\Users\\Rowdy Payton\\AppData\\Roaming\\FreeCAD\\v1-1\\Mod\\CombineFiles_SingleText_Clear.ps1",
        "C:\\Users\\Rowdy Payton\\AppData\\Roaming\\FreeCAD\\v1-1\\Mod\\CombineFiles_SingleText_Clear.bat",
        "C:\\Program Files\\FreeCAD 1.1\\Mod\\Web",
        "C:\\Program Files\\FreeCAD 1.1\\Mod\\Tux",
        "C:\\Program Files\\FreeCAD 1.1\\Mod\\Test",
        "C:\\Program Files\\FreeCAD 1.1\\Mod\\TechDraw",
        "C:\\Program Files\\FreeCAD 1.1\\Mod\\Surface"
      ],
      "pymupdf": {
        "status": "available_from_lib_dir",
        "installed_now": false,
        "lib_dir": "C:\\Users\\Rowdy Payton\\AppData\\Roaming\\FreeCAD\\Mod\\PDFVectorImporter\\src\\lib"
      },
      "input_pdf": "C:\\Users\\Rowdy Payton\\Downloads\\alvord_plant_list.pdf",
      "preset": "Shop Drawing",
      "page_range": "all",
      "pages": [
        1,
        2
      ],
      "counts_before": {
        "objects_total": 0,
        "groups": 0,
        "wires": 0,
        "faces": 0,
        "texts": 0
      },
      "counts_after": {
        "objects_total": 309,
        "groups": 10,
        "wires": 123,
        "faces": 87,
        "texts": 0
      },
      "counts_delta": {
        "objects_total": 309,
        "groups": 10,
        "wires": 123,
        "faces": 87,
        "texts": 0
      },
      "finished_at": "2026-03-30T02:32:19Z",
      "runtime_seconds": 1.525,
      "_returncode": 0,
      "_wall_seconds": 1.935,
      "_input_pdf": "C:\\Users\\Rowdy Payton\\Downloads\\alvord_plant_list.pdf"
    },
    {
      "test_id": "FC-ALV-03",
      "platform": "FC",
      "status": "PASS",
      "message": "Import completed.",
      "started_at": "2026-03-30T02:32:19Z",
      "mod_dir": "C:\\Users\\Rowdy Payton\\AppData\\Roaming\\FreeCAD\\Mod\\PDFVectorImporter",
      "sys_path_head": [
        "C:\\Users\\Rowdy Payton\\AppData\\Roaming\\FreeCAD\\Mod\\PDFVectorImporter\\src",
        "C:\\Users\\Rowdy Payton\\AppData\\Roaming\\FreeCAD\\Mod\\PDFVectorImporter",
        "C:\\Users\\Rowdy Payton\\AppData\\Roaming\\FreeCAD\\Mod",
        "C:\\Users\\Rowdy Payton\\AppData\\Roaming\\FreeCAD\\v1-1\\Mod\\PDFVectorImporter\\.\\",
        "C:\\Users\\Rowdy Payton\\AppData\\Roaming\\FreeCAD\\v1-1\\Mod\\PDFVectorImporter",
        "C:\\Users\\Rowdy Payton\\AppData\\Roaming\\FreeCAD\\v1-1\\Mod\\CombineFiles_SingleText_Clear.ps1",
        "C:\\Users\\Rowdy Payton\\AppData\\Roaming\\FreeCAD\\v1-1\\Mod\\CombineFiles_SingleText_Clear.bat",
        "C:\\Program Files\\FreeCAD 1.1\\Mod\\Web",
        "C:\\Program Files\\FreeCAD 1.1\\Mod\\Tux",
        "C:\\Program Files\\FreeCAD 1.1\\Mod\\Test",
        "C:\\Program Files\\FreeCAD 1.1\\Mod\\TechDraw",
        "C:\\Program Files\\FreeCAD 1.1\\Mod\\Surface"
      ],
      "pymupdf": {
        "status": "available_from_lib_dir",
        "installed_now": false,
        "lib_dir": "C:\\Users\\Rowdy Payton\\AppData\\Roaming\\FreeCAD\\Mod\\PDFVectorImporter\\src\\lib"
      },
      "input_pdf": "C:\\Users\\Rowdy Payton\\Downloads\\alvord_garden_map_PRINT.pdf",
      "preset": "Shop Drawing",
      "page_range": "all",
      "pages": [
        1,
        2,
        3,
        4
      ],
      "counts_before": {
        "objects_total": 0,
        "groups": 0,
        "wires": 0,
        "faces": 0,
        "texts": 0
      },
      "counts_after": {
        "objects_total": 3024,
        "groups": 38,
        "wires": 1181,
        "faces": 1118,
        "texts": 0
      },
      "counts_delta": {
        "objects_total": 3024,
        "groups": 38,
        "wires": 1181,
        "faces": 1118,
        "texts": 0
      },
      "finished_at": "2026-03-30T02:32:23Z",
      "runtime_seconds": 3.136,
      "_returncode": 0,
      "_wall_seconds": 3.589,
      "_input_pdf": "C:\\Users\\Rowdy Payton\\Downloads\\alvord_garden_map_PRINT.pdf"
    },
    {
      "test_id": "FC-ALV-04",
      "platform": "FC",
      "status": "PASS",
      "message": "Import completed.",
      "started_at": "2026-03-30T02:32:23Z",
      "mod_dir": "C:\\Users\\Rowdy Payton\\AppData\\Roaming\\FreeCAD\\Mod\\PDFVectorImporter",
      "sys_path_head": [
        "C:\\Users\\Rowdy Payton\\AppData\\Roaming\\FreeCAD\\Mod\\PDFVectorImporter\\src",
        "C:\\Users\\Rowdy Payton\\AppData\\Roaming\\FreeCAD\\Mod\\PDFVectorImporter",
        "C:\\Users\\Rowdy Payton\\AppData\\Roaming\\FreeCAD\\Mod",
        "C:\\Users\\Rowdy Payton\\AppData\\Roaming\\FreeCAD\\v1-1\\Mod\\PDFVectorImporter\\.\\",
        "C:\\Users\\Rowdy Payton\\AppData\\Roaming\\FreeCAD\\v1-1\\Mod\\PDFVectorImporter",
        "C:\\Users\\Rowdy Payton\\AppData\\Roaming\\FreeCAD\\v1-1\\Mod\\CombineFiles_SingleText_Clear.ps1",
        "C:\\Users\\Rowdy Payton\\AppData\\Roaming\\FreeCAD\\v1-1\\Mod\\CombineFiles_SingleText_Clear.bat",
        "C:\\Program Files\\FreeCAD 1.1\\Mod\\Web",
        "C:\\Program Files\\FreeCAD 1.1\\Mod\\Tux",
        "C:\\Program Files\\FreeCAD 1.1\\Mod\\Test",
        "C:\\Program Files\\FreeCAD 1.1\\Mod\\TechDraw",
        "C:\\Program Files\\FreeCAD 1.1\\Mod\\Surface"
      ],
      "pymupdf": {
        "status": "available_from_lib_dir",
        "installed_now": false,
        "lib_dir": "C:\\Users\\Rowdy Payton\\AppData\\Roaming\\FreeCAD\\Mod\\PDFVectorImporter\\src\\lib"
      },
      "input_pdf": "C:\\Users\\Rowdy Payton\\Downloads\\Alvord TX \u2014 Garden Map \u00b7 Final.pdf",
      "preset": "Shop Drawing",
      "page_range": "all",
      "pages": [
        1
      ],
      "counts_before": {
        "objects_total": 0,
        "groups": 0,
        "wires": 0,
        "faces": 0,
        "texts": 0
      },
      "counts_after": {
        "objects_total": 2,
        "groups": 1,
        "wires": 0,
        "faces": 0,
        "texts": 0
      },
      "counts_delta": {
        "objects_total": 2,
        "groups": 1,
        "wires": 0,
        "faces": 0,
        "texts": 0
      },
      "finished_at": "2026-03-30T02:32:24Z",
      "runtime_seconds": 1.153,
      "_returncode": 0,
      "_wall_seconds": 1.535,
      "_input_pdf": "C:\\Users\\Rowdy Payton\\Downloads\\Alvord TX \u2014 Garden Map \u00b7 Final.pdf"
    },
    {
      "test_id": "FC-ALV-05",
      "platform": "FC",
      "status": "PASS",
      "message": "Import completed.",
      "started_at": "2026-03-30T02:32:25Z",
      "mod_dir": "C:\\Users\\Rowdy Payton\\AppData\\Roaming\\FreeCAD\\Mod\\PDFVectorImporter",
      "sys_path_head": [
        "C:\\Users\\Rowdy Payton\\AppData\\Roaming\\FreeCAD\\Mod\\PDFVectorImporter\\src",
        "C:\\Users\\Rowdy Payton\\AppData\\Roaming\\FreeCAD\\Mod\\PDFVectorImporter",
        "C:\\Users\\Rowdy Payton\\AppData\\Roaming\\FreeCAD\\Mod",
        "C:\\Users\\Rowdy Payton\\AppData\\Roaming\\FreeCAD\\v1-1\\Mod\\PDFVectorImporter\\.\\",
        "C:\\Users\\Rowdy Payton\\AppData\\Roaming\\FreeCAD\\v1-1\\Mod\\PDFVectorImporter",
        "C:\\Users\\Rowdy Payton\\AppData\\Roaming\\FreeCAD\\v1-1\\Mod\\CombineFiles_SingleText_Clear.ps1",
        "C:\\Users\\Rowdy Payton\\AppData\\Roaming\\FreeCAD\\v1-1\\Mod\\CombineFiles_SingleText_Clear.bat",
        "C:\\Program Files\\FreeCAD 1.1\\Mod\\Web",
        "C:\\Program Files\\FreeCAD 1.1\\Mod\\Tux",
        "C:\\Program Files\\FreeCAD 1.1\\Mod\\Test",
        "C:\\Program Files\\FreeCAD 1.1\\Mod\\TechDraw",
        "C:\\Program Files\\FreeCAD 1.1\\Mod\\Surface"
      ],
      "pymupdf": {
        "status": "available_from_lib_dir",
        "installed_now": false,
        "lib_dir": "C:\\Users\\Rowdy Payton\\AppData\\Roaming\\FreeCAD\\Mod\\PDFVectorImporter\\src\\lib"
      },
      "input_pdf": "C:\\Users\\Rowdy Payton\\Downloads\\Alvord TX \u2014 Garden Plan \u00b7 Final.pdf",
      "preset": "Shop Drawing",
      "page_range": "all",
      "pages": [
        1,
        2,
        3,
        4,
        5,
        6,
        7
      ],
      "counts_before": {
        "objects_total": 0,
        "groups": 0,
        "wires": 0,
        "faces": 0,
        "texts": 0
      },
      "counts_after": {
        "objects_total": 14,
        "groups": 7,
        "wires": 0,
        "faces": 0,
        "texts": 0
      },
      "counts_delta": {
        "objects_total": 14,
        "groups": 7,
        "wires": 0,
        "faces": 0,
        "texts": 0
      },
      "finished_at": "2026-03-30T02:32:26Z",
      "runtime_seconds": 1.472,
      "_returncode": 0,
      "_wall_seconds": 1.865,
      "_input_pdf": "C:\\Users\\Rowdy Payton\\Downloads\\Alvord TX \u2014 Garden Plan \u00b7 Final.pdf"
    }
  ],
  "sketchup": [
    {
      "test_id": "SU-ALV-01",
      "platform": "SU",
      "status": "PASS",
      "message": "Import completed.",
      "started_at": "2026-03-30T02:36:33Z",
      "loader": "C:/Users/Rowdy Payton/AppData/Roaming/SketchUp/SketchUp 2017/SketchUp/Plugins/bc_pdf_vector_importer/main",
      "input_pdf": "C:\\Users\\Rowdy Payton\\Downloads\\TX_Alvord_20220525_TM_geo.pdf",
      "preset": "Full",
      "page_range": "all",
      "pipeline_stats": {
        "pages": 1,
        "primitives": 0,
        "edges": 0,
        "faces": 0,
        "arcs": 0,
        "text": 0,
        "components": 0,
        "layers": [
          "??\u0000L\u0000a\u0000b\u0000e\u0000l\u0000s",
          "Map Collar",
          "Map Elements",
          "Map Frame",
          "Boundaries",
          "Federal Administrated Lands",
          "Forest Service",
          "Jurisdictional Boundaries",
          "County or Equivalent",
          "State or Territory",
          "Woodland",
          "Terrain",
          "Shaded Relief",
          "Contours",
          "Hydrography",
          "Wetlands",
          "Transportation",
          "Airports",
          "Railroads",
          "Road Features",
          "Road Names and Shields",
          "Structures",
          "Geographic Names",
          "Projection and Grids",
          "Images",
          "Orthoimage",
          "Barcode"
        ],
        "cleanup": {},
        "generic": null,
        "mode_used": null,
        "xobjects": 0,
        "text_mode": "geometry",
        "raster_fallback_used": true,
        "elapsed_seconds": 16.6,
        "log_path": "C:/TMP/bc_pdf_importer/last_import.log"
      },
      "model_counts_before": {
        "edges": 0,
        "faces": 0,
        "groups": 0,
        "component_instances": 0,
        "texts": 0,
        "images": 0
      },
      "model_counts_after": {
        "edges": 0,
        "faces": 0,
        "groups": 0,
        "component_instances": 0,
        "texts": 0,
        "images": 1
      },
      "model_delta": {
        "edges": 0,
        "faces": 0,
        "groups": 0,
        "component_instances": 0,
        "texts": 0,
        "images": 1
      },
      "layers_before": 1,
      "layers_after": 29,
      "layers_delta": 28,
      "finished_at": "2026-03-30T02:36:49Z",
      "runtime_seconds": 16.61,
      "_returncode": 0,
      "_wall_seconds": 263.182,
      "_input_pdf": "C:\\Users\\Rowdy Payton\\Downloads\\TX_Alvord_20220525_TM_geo.pdf"
    },
    {
      "test_id": "SU-ALV-02",
      "platform": "SU",
      "status": "PASS",
      "message": "Import completed.",
      "started_at": "2026-03-30T02:37:01Z",
      "loader": "C:/Users/Rowdy Payton/AppData/Roaming/SketchUp/SketchUp 2017/SketchUp/Plugins/bc_pdf_vector_importer/main",
      "input_pdf": "C:\\Users\\Rowdy Payton\\Downloads\\alvord_plant_list.pdf",
      "preset": "Full",
      "page_range": "all",
      "pipeline_stats": {
        "pages": 2,
        "primitives": 125,
        "edges": 11018,
        "faces": 87,
        "arcs": 0,
        "text": 2767,
        "components": 0,
        "layers": [],
        "cleanup": {
          "merged_verts": 0,
          "removed_dupes": 0,
          "removed_micro": 0,
          "joined_collinear": 0,
          "closed_gaps": 0
        },
        "generic": null,
        "mode_used": null,
        "xobjects": 0,
        "text_mode": "geometry",
        "elapsed_seconds": 1.4,
        "log_path": "C:/TMP/bc_pdf_importer/last_import.log"
      },
      "model_counts_before": {
        "edges": 0,
        "faces": 0,
        "groups": 0,
        "component_instances": 0,
        "texts": 0,
        "images": 0
      },
      "model_counts_after": {
        "edges": 10946,
        "faces": 87,
        "groups": 8,
        "component_instances": 2767,
        "texts": 0,
        "images": 0
      },
      "model_delta": {
        "edges": 10946,
        "faces": 87,
        "groups": 8,
        "component_instances": 2767,
        "texts": 0,
        "images": 0
      },
      "layers_before": 1,
      "layers_after": 4,
      "layers_delta": 3,
      "finished_at": "2026-03-30T02:37:03Z",
      "runtime_seconds": 1.423,
      "_returncode": 0,
      "_wall_seconds": 12.105,
      "_input_pdf": "C:\\Users\\Rowdy Payton\\Downloads\\alvord_plant_list.pdf"
    },
    {
      "test_id": "SU-ALV-03",
      "platform": "SU",
      "status": "PASS",
      "message": "Import completed.",
      "started_at": "2026-03-30T02:37:10Z",
      "loader": "C:/Users/Rowdy Payton/AppData/Roaming/SketchUp/SketchUp 2017/SketchUp/Plugins/bc_pdf_vector_importer/main",
      "input_pdf": "C:\\Users\\Rowdy Payton\\Downloads\\alvord_garden_map_PRINT.pdf",
      "preset": "Full",
      "page_range": "all",
      "pipeline_stats": {
        "pages": 4,
        "primitives": 1769,
        "edges": 47432,
        "faces": 1082,
        "arcs": 0,
        "text": 7224,
        "components": 0,
        "layers": [],
        "cleanup": {
          "merged_verts": 0,
          "removed_dupes": 0,
          "removed_micro": 0,
          "joined_collinear": 0,
          "closed_gaps": 0
        },
        "generic": null,
        "mode_used": null,
        "xobjects": 0,
        "text_mode": "geometry",
        "elapsed_seconds": 4.7,
        "log_path": "C:/TMP/bc_pdf_importer/last_import.log"
      },
      "model_counts_before": {
        "edges": 0,
        "faces": 0,
        "groups": 0,
        "component_instances": 0,
        "texts": 0,
        "images": 0
      },
      "model_counts_after": {
        "edges": 54638,
        "faces": 1082,
        "groups": 34,
        "component_instances": 7224,
        "texts": 0,
        "images": 0
      },
      "model_delta": {
        "edges": 54638,
        "faces": 1082,
        "groups": 34,
        "component_instances": 7224,
        "texts": 0,
        "images": 0
      },
      "layers_before": 1,
      "layers_after": 4,
      "layers_delta": 3,
      "finished_at": "2026-03-30T02:37:15Z",
      "runtime_seconds": 4.784,
      "_returncode": 0,
      "_wall_seconds": 11.108,
      "_input_pdf": "C:\\Users\\Rowdy Payton\\Downloads\\alvord_garden_map_PRINT.pdf"
    },
    {
      "test_id": "SU-ALV-04",
      "platform": "SU",
      "status": "PASS",
      "message": "Import completed.",
      "started_at": "2026-03-30T02:37:22Z",
      "loader": "C:/Users/Rowdy Payton/AppData/Roaming/SketchUp/SketchUp 2017/SketchUp/Plugins/bc_pdf_vector_importer/main",
      "input_pdf": "C:\\Users\\Rowdy Payton\\Downloads\\Alvord TX ??? Garden Map ?? Final.pdf",
      "preset": "Full",
      "page_range": "all",
      "pipeline_stats": {
        "pages": 1,
        "primitives": 0,
        "edges": 0,
        "faces": 0,
        "arcs": 0,
        "text": 0,
        "components": 0,
        "layers": [],
        "cleanup": {},
        "generic": null,
        "mode_used": null,
        "xobjects": 0,
        "text_mode": "geometry",
        "raster_fallback_used": true,
        "elapsed_seconds": 6.1,
        "log_path": "C:/TMP/bc_pdf_importer/last_import.log"
      },
      "model_counts_before": {
        "edges": 0,
        "faces": 0,
        "groups": 0,
        "component_instances": 0,
        "texts": 0,
        "images": 0
      },
      "model_counts_after": {
        "edges": 0,
        "faces": 0,
        "groups": 0,
        "component_instances": 0,
        "texts": 0,
        "images": 1
      },
      "model_delta": {
        "edges": 0,
        "faces": 0,
        "groups": 0,
        "component_instances": 0,
        "texts": 0,
        "images": 1
      },
      "layers_before": 1,
      "layers_after": 2,
      "layers_delta": 1,
      "finished_at": "2026-03-30T02:37:28Z",
      "runtime_seconds": 6.097,
      "_returncode": 0,
      "_wall_seconds": 12.169,
      "_input_pdf": "C:\\Users\\Rowdy Payton\\Downloads\\Alvord TX \u2014 Garden Map \u00b7 Final.pdf"
    },
    {
      "test_id": "SU-ALV-05",
      "platform": "SU",
      "status": "PASS",
      "message": "Import completed.",
      "started_at": "2026-03-30T02:37:35Z",
      "loader": "C:/Users/Rowdy Payton/AppData/Roaming/SketchUp/SketchUp 2017/SketchUp/Plugins/bc_pdf_vector_importer/main",
      "input_pdf": "C:\\Users\\Rowdy Payton\\Downloads\\Alvord TX ??? Garden Plan ?? Final.pdf",
      "preset": "Full",
      "page_range": "all",
      "pipeline_stats": {
        "pages": 7,
        "primitives": 0,
        "edges": 0,
        "faces": 0,
        "arcs": 0,
        "text": 0,
        "components": 0,
        "layers": [],
        "cleanup": {},
        "generic": null,
        "mode_used": null,
        "xobjects": 0,
        "text_mode": "geometry",
        "raster_fallback_used": true,
        "elapsed_seconds": 10.1,
        "log_path": "C:/TMP/bc_pdf_importer/last_import.log"
      },
      "model_counts_before": {
        "edges": 0,
        "faces": 0,
        "groups": 0,
        "component_instances": 0,
        "texts": 0,
        "images": 0
      },
      "model_counts_after": {
        "edges": 0,
        "faces": 0,
        "groups": 0,
        "component_instances": 0,
        "texts": 0,
        "images": 7
      },
      "model_delta": {
        "edges": 0,
        "faces": 0,
        "groups": 0,
        "component_instances": 0,
        "texts": 0,
        "images": 7
      },
      "layers_before": 1,
      "layers_after": 2,
      "layers_delta": 1,
      "finished_at": "2026-03-30T02:37:45Z",
      "runtime_seconds": 10.089,
      "_returncode": 0,
      "_wall_seconds": 16.112,
      "_input_pdf": "C:\\Users\\Rowdy Payton\\Downloads\\Alvord TX \u2014 Garden Plan \u00b7 Final.pdf"
    }
  ],
  "totals": {
    "freecad": {
      "total": 5,
      "passed": 5,
      "failed": 0
    },
    "sketchup": {
      "total": 5,
      "passed": 5,
      "failed": 0
    }
  }
}
```

### PDFVectorImporter/qa_runs/20260329_213208/consolidated_alvord_report.md

- Path: `PDFVectorImporter/qa_runs/20260329_213208/consolidated_alvord_report.md`
- Size: `1.09 KB`
- Modified: `2026-03-29 21:37:47`

~~~markdown
# Alvord Verification Report (20260329_213208)

- Output folder: `C:\1FC-PDFimporter\PDFVectorImporter\qa_runs\20260329_213208`
- FreeCAD: 5/5 pass
- SketchUp: 5/5 pass

## Freecad
- `FC-ALV-01` | `PASS` | `9.518s` | `TX_Alvord_20220525_TM_geo.pdf` | Import completed.
- `FC-ALV-02` | `PASS` | `1.935s` | `alvord_plant_list.pdf` | Import completed.
- `FC-ALV-03` | `PASS` | `3.589s` | `alvord_garden_map_PRINT.pdf` | Import completed.
- `FC-ALV-04` | `PASS` | `1.535s` | `Alvord TX — Garden Map · Final.pdf` | Import completed.
- `FC-ALV-05` | `PASS` | `1.865s` | `Alvord TX — Garden Plan · Final.pdf` | Import completed.

## Sketchup
- `SU-ALV-01` | `PASS` | `263.182s` | `TX_Alvord_20220525_TM_geo.pdf` | Import completed.
- `SU-ALV-02` | `PASS` | `12.105s` | `alvord_plant_list.pdf` | Import completed.
- `SU-ALV-03` | `PASS` | `11.108s` | `alvord_garden_map_PRINT.pdf` | Import completed.
- `SU-ALV-04` | `PASS` | `12.169s` | `Alvord TX — Garden Map · Final.pdf` | Import completed.
- `SU-ALV-05` | `PASS` | `16.112s` | `Alvord TX — Garden Plan · Final.pdf` | Import completed.
~~~

### PDFVectorImporter/qa_runs/20260329_213208/FC-ALV-01.json

- Path: `PDFVectorImporter/qa_runs/20260329_213208/FC-ALV-01.json`
- Size: `2.03 KB`
- Modified: `2026-03-29 21:32:17`

```json
{
  "test_id": "FC-ALV-01",
  "platform": "FC",
  "status": "PASS",
  "message": "Import completed.",
  "started_at": "2026-03-30T02:32:08Z",
  "mod_dir": "C:\\Users\\Rowdy Payton\\AppData\\Roaming\\FreeCAD\\Mod\\PDFVectorImporter",
  "sys_path_head": [
    "C:\\Users\\Rowdy Payton\\AppData\\Roaming\\FreeCAD\\Mod\\PDFVectorImporter\\src",
    "C:\\Users\\Rowdy Payton\\AppData\\Roaming\\FreeCAD\\Mod\\PDFVectorImporter",
    "C:\\Users\\Rowdy Payton\\AppData\\Roaming\\FreeCAD\\Mod",
    "C:\\Users\\Rowdy Payton\\AppData\\Roaming\\FreeCAD\\v1-1\\Mod\\PDFVectorImporter\\.\\",
    "C:\\Users\\Rowdy Payton\\AppData\\Roaming\\FreeCAD\\v1-1\\Mod\\PDFVectorImporter",
    "C:\\Users\\Rowdy Payton\\AppData\\Roaming\\FreeCAD\\v1-1\\Mod\\CombineFiles_SingleText_Clear.ps1",
    "C:\\Users\\Rowdy Payton\\AppData\\Roaming\\FreeCAD\\v1-1\\Mod\\CombineFiles_SingleText_Clear.bat",
    "C:\\Program Files\\FreeCAD 1.1\\Mod\\Web",
    "C:\\Program Files\\FreeCAD 1.1\\Mod\\Tux",
    "C:\\Program Files\\FreeCAD 1.1\\Mod\\Test",
    "C:\\Program Files\\FreeCAD 1.1\\Mod\\TechDraw",
    "C:\\Program Files\\FreeCAD 1.1\\Mod\\Surface"
  ],
  "pymupdf": {
    "status": "available_from_lib_dir",
    "installed_now": false,
    "lib_dir": "C:\\Users\\Rowdy Payton\\AppData\\Roaming\\FreeCAD\\Mod\\PDFVectorImporter\\src\\lib"
  },
  "input_pdf": "C:\\Users\\Rowdy Payton\\Downloads\\TX_Alvord_20220525_TM_geo.pdf",
  "preset": "Shop Drawing",
  "page_range": "all",
  "pages": [
    1
  ],
  "counts_before": {
    "objects_total": 0,
    "groups": 0,
    "wires": 0,
    "faces": 0,
    "texts": 0
  },
  "counts_after": {
    "objects_total": 2,
    "groups": 1,
    "wires": 0,
    "faces": 0,
    "texts": 0
  },
  "counts_delta": {
    "objects_total": 2,
    "groups": 1,
    "wires": 0,
    "faces": 0,
    "texts": 0
  },
  "finished_at": "2026-03-30T02:32:17Z",
  "runtime_seconds": 8.857,
  "_returncode": 0,
  "_wall_seconds": 9.518,
  "_input_pdf": "C:\\Users\\Rowdy Payton\\Downloads\\TX_Alvord_20220525_TM_geo.pdf"
}
```

### PDFVectorImporter/qa_runs/20260329_213208/FC-ALV-02.json

- Path: `PDFVectorImporter/qa_runs/20260329_213208/FC-ALV-02.json`
- Size: `2.03 KB`
- Modified: `2026-03-29 21:32:19`

```json
{
  "test_id": "FC-ALV-02",
  "platform": "FC",
  "status": "PASS",
  "message": "Import completed.",
  "started_at": "2026-03-30T02:32:18Z",
  "mod_dir": "C:\\Users\\Rowdy Payton\\AppData\\Roaming\\FreeCAD\\Mod\\PDFVectorImporter",
  "sys_path_head": [
    "C:\\Users\\Rowdy Payton\\AppData\\Roaming\\FreeCAD\\Mod\\PDFVectorImporter\\src",
    "C:\\Users\\Rowdy Payton\\AppData\\Roaming\\FreeCAD\\Mod\\PDFVectorImporter",
    "C:\\Users\\Rowdy Payton\\AppData\\Roaming\\FreeCAD\\Mod",
    "C:\\Users\\Rowdy Payton\\AppData\\Roaming\\FreeCAD\\v1-1\\Mod\\PDFVectorImporter\\.\\",
    "C:\\Users\\Rowdy Payton\\AppData\\Roaming\\FreeCAD\\v1-1\\Mod\\PDFVectorImporter",
    "C:\\Users\\Rowdy Payton\\AppData\\Roaming\\FreeCAD\\v1-1\\Mod\\CombineFiles_SingleText_Clear.ps1",
    "C:\\Users\\Rowdy Payton\\AppData\\Roaming\\FreeCAD\\v1-1\\Mod\\CombineFiles_SingleText_Clear.bat",
    "C:\\Program Files\\FreeCAD 1.1\\Mod\\Web",
    "C:\\Program Files\\FreeCAD 1.1\\Mod\\Tux",
    "C:\\Program Files\\FreeCAD 1.1\\Mod\\Test",
    "C:\\Program Files\\FreeCAD 1.1\\Mod\\TechDraw",
    "C:\\Program Files\\FreeCAD 1.1\\Mod\\Surface"
  ],
  "pymupdf": {
    "status": "available_from_lib_dir",
    "installed_now": false,
    "lib_dir": "C:\\Users\\Rowdy Payton\\AppData\\Roaming\\FreeCAD\\Mod\\PDFVectorImporter\\src\\lib"
  },
  "input_pdf": "C:\\Users\\Rowdy Payton\\Downloads\\alvord_plant_list.pdf",
  "preset": "Shop Drawing",
  "page_range": "all",
  "pages": [
    1,
    2
  ],
  "counts_before": {
    "objects_total": 0,
    "groups": 0,
    "wires": 0,
    "faces": 0,
    "texts": 0
  },
  "counts_after": {
    "objects_total": 309,
    "groups": 10,
    "wires": 123,
    "faces": 87,
    "texts": 0
  },
  "counts_delta": {
    "objects_total": 309,
    "groups": 10,
    "wires": 123,
    "faces": 87,
    "texts": 0
  },
  "finished_at": "2026-03-30T02:32:19Z",
  "runtime_seconds": 1.525,
  "_returncode": 0,
  "_wall_seconds": 1.935,
  "_input_pdf": "C:\\Users\\Rowdy Payton\\Downloads\\alvord_plant_list.pdf"
}
```

### PDFVectorImporter/qa_runs/20260329_213208/FC-ALV-03.json

- Path: `PDFVectorImporter/qa_runs/20260329_213208/FC-ALV-03.json`
- Size: `2.07 KB`
- Modified: `2026-03-29 21:32:23`

```json
{
  "test_id": "FC-ALV-03",
  "platform": "FC",
  "status": "PASS",
  "message": "Import completed.",
  "started_at": "2026-03-30T02:32:19Z",
  "mod_dir": "C:\\Users\\Rowdy Payton\\AppData\\Roaming\\FreeCAD\\Mod\\PDFVectorImporter",
  "sys_path_head": [
    "C:\\Users\\Rowdy Payton\\AppData\\Roaming\\FreeCAD\\Mod\\PDFVectorImporter\\src",
    "C:\\Users\\Rowdy Payton\\AppData\\Roaming\\FreeCAD\\Mod\\PDFVectorImporter",
    "C:\\Users\\Rowdy Payton\\AppData\\Roaming\\FreeCAD\\Mod",
    "C:\\Users\\Rowdy Payton\\AppData\\Roaming\\FreeCAD\\v1-1\\Mod\\PDFVectorImporter\\.\\",
    "C:\\Users\\Rowdy Payton\\AppData\\Roaming\\FreeCAD\\v1-1\\Mod\\PDFVectorImporter",
    "C:\\Users\\Rowdy Payton\\AppData\\Roaming\\FreeCAD\\v1-1\\Mod\\CombineFiles_SingleText_Clear.ps1",
    "C:\\Users\\Rowdy Payton\\AppData\\Roaming\\FreeCAD\\v1-1\\Mod\\CombineFiles_SingleText_Clear.bat",
    "C:\\Program Files\\FreeCAD 1.1\\Mod\\Web",
    "C:\\Program Files\\FreeCAD 1.1\\Mod\\Tux",
    "C:\\Program Files\\FreeCAD 1.1\\Mod\\Test",
    "C:\\Program Files\\FreeCAD 1.1\\Mod\\TechDraw",
    "C:\\Program Files\\FreeCAD 1.1\\Mod\\Surface"
  ],
  "pymupdf": {
    "status": "available_from_lib_dir",
    "installed_now": false,
    "lib_dir": "C:\\Users\\Rowdy Payton\\AppData\\Roaming\\FreeCAD\\Mod\\PDFVectorImporter\\src\\lib"
  },
  "input_pdf": "C:\\Users\\Rowdy Payton\\Downloads\\alvord_garden_map_PRINT.pdf",
  "preset": "Shop Drawing",
  "page_range": "all",
  "pages": [
    1,
    2,
    3,
    4
  ],
  "counts_before": {
    "objects_total": 0,
    "groups": 0,
    "wires": 0,
    "faces": 0,
    "texts": 0
  },
  "counts_after": {
    "objects_total": 3024,
    "groups": 38,
    "wires": 1181,
    "faces": 1118,
    "texts": 0
  },
  "counts_delta": {
    "objects_total": 3024,
    "groups": 38,
    "wires": 1181,
    "faces": 1118,
    "texts": 0
  },
  "finished_at": "2026-03-30T02:32:23Z",
  "runtime_seconds": 3.136,
  "_returncode": 0,
  "_wall_seconds": 3.589,
  "_input_pdf": "C:\\Users\\Rowdy Payton\\Downloads\\alvord_garden_map_PRINT.pdf"
}
```

### PDFVectorImporter/qa_runs/20260329_213208/FC-ALV-04.json

- Path: `PDFVectorImporter/qa_runs/20260329_213208/FC-ALV-04.json`
- Size: `2.06 KB`
- Modified: `2026-03-29 21:32:24`

```json
{
  "test_id": "FC-ALV-04",
  "platform": "FC",
  "status": "PASS",
  "message": "Import completed.",
  "started_at": "2026-03-30T02:32:23Z",
  "mod_dir": "C:\\Users\\Rowdy Payton\\AppData\\Roaming\\FreeCAD\\Mod\\PDFVectorImporter",
  "sys_path_head": [
    "C:\\Users\\Rowdy Payton\\AppData\\Roaming\\FreeCAD\\Mod\\PDFVectorImporter\\src",
    "C:\\Users\\Rowdy Payton\\AppData\\Roaming\\FreeCAD\\Mod\\PDFVectorImporter",
    "C:\\Users\\Rowdy Payton\\AppData\\Roaming\\FreeCAD\\Mod",
    "C:\\Users\\Rowdy Payton\\AppData\\Roaming\\FreeCAD\\v1-1\\Mod\\PDFVectorImporter\\.\\",
    "C:\\Users\\Rowdy Payton\\AppData\\Roaming\\FreeCAD\\v1-1\\Mod\\PDFVectorImporter",
    "C:\\Users\\Rowdy Payton\\AppData\\Roaming\\FreeCAD\\v1-1\\Mod\\CombineFiles_SingleText_Clear.ps1",
    "C:\\Users\\Rowdy Payton\\AppData\\Roaming\\FreeCAD\\v1-1\\Mod\\CombineFiles_SingleText_Clear.bat",
    "C:\\Program Files\\FreeCAD 1.1\\Mod\\Web",
    "C:\\Program Files\\FreeCAD 1.1\\Mod\\Tux",
    "C:\\Program Files\\FreeCAD 1.1\\Mod\\Test",
    "C:\\Program Files\\FreeCAD 1.1\\Mod\\TechDraw",
    "C:\\Program Files\\FreeCAD 1.1\\Mod\\Surface"
  ],
  "pymupdf": {
    "status": "available_from_lib_dir",
    "installed_now": false,
    "lib_dir": "C:\\Users\\Rowdy Payton\\AppData\\Roaming\\FreeCAD\\Mod\\PDFVectorImporter\\src\\lib"
  },
  "input_pdf": "C:\\Users\\Rowdy Payton\\Downloads\\Alvord TX \u2014 Garden Map \u00b7 Final.pdf",
  "preset": "Shop Drawing",
  "page_range": "all",
  "pages": [
    1
  ],
  "counts_before": {
    "objects_total": 0,
    "groups": 0,
    "wires": 0,
    "faces": 0,
    "texts": 0
  },
  "counts_after": {
    "objects_total": 2,
    "groups": 1,
    "wires": 0,
    "faces": 0,
    "texts": 0
  },
  "counts_delta": {
    "objects_total": 2,
    "groups": 1,
    "wires": 0,
    "faces": 0,
    "texts": 0
  },
  "finished_at": "2026-03-30T02:32:24Z",
  "runtime_seconds": 1.153,
  "_returncode": 0,
  "_wall_seconds": 1.535,
  "_input_pdf": "C:\\Users\\Rowdy Payton\\Downloads\\Alvord TX \u2014 Garden Map \u00b7 Final.pdf"
}
```

### PDFVectorImporter/qa_runs/20260329_213208/FC-ALV-05.json

- Path: `PDFVectorImporter/qa_runs/20260329_213208/FC-ALV-05.json`
- Size: `2.11 KB`
- Modified: `2026-03-29 21:32:26`

```json
{
  "test_id": "FC-ALV-05",
  "platform": "FC",
  "status": "PASS",
  "message": "Import completed.",
  "started_at": "2026-03-30T02:32:25Z",
  "mod_dir": "C:\\Users\\Rowdy Payton\\AppData\\Roaming\\FreeCAD\\Mod\\PDFVectorImporter",
  "sys_path_head": [
    "C:\\Users\\Rowdy Payton\\AppData\\Roaming\\FreeCAD\\Mod\\PDFVectorImporter\\src",
    "C:\\Users\\Rowdy Payton\\AppData\\Roaming\\FreeCAD\\Mod\\PDFVectorImporter",
    "C:\\Users\\Rowdy Payton\\AppData\\Roaming\\FreeCAD\\Mod",
    "C:\\Users\\Rowdy Payton\\AppData\\Roaming\\FreeCAD\\v1-1\\Mod\\PDFVectorImporter\\.\\",
    "C:\\Users\\Rowdy Payton\\AppData\\Roaming\\FreeCAD\\v1-1\\Mod\\PDFVectorImporter",
    "C:\\Users\\Rowdy Payton\\AppData\\Roaming\\FreeCAD\\v1-1\\Mod\\CombineFiles_SingleText_Clear.ps1",
    "C:\\Users\\Rowdy Payton\\AppData\\Roaming\\FreeCAD\\v1-1\\Mod\\CombineFiles_SingleText_Clear.bat",
    "C:\\Program Files\\FreeCAD 1.1\\Mod\\Web",
    "C:\\Program Files\\FreeCAD 1.1\\Mod\\Tux",
    "C:\\Program Files\\FreeCAD 1.1\\Mod\\Test",
    "C:\\Program Files\\FreeCAD 1.1\\Mod\\TechDraw",
    "C:\\Program Files\\FreeCAD 1.1\\Mod\\Surface"
  ],
  "pymupdf": {
    "status": "available_from_lib_dir",
    "installed_now": false,
    "lib_dir": "C:\\Users\\Rowdy Payton\\AppData\\Roaming\\FreeCAD\\Mod\\PDFVectorImporter\\src\\lib"
  },
  "input_pdf": "C:\\Users\\Rowdy Payton\\Downloads\\Alvord TX \u2014 Garden Plan \u00b7 Final.pdf",
  "preset": "Shop Drawing",
  "page_range": "all",
  "pages": [
    1,
    2,
    3,
    4,
    5,
    6,
    7
  ],
  "counts_before": {
    "objects_total": 0,
    "groups": 0,
    "wires": 0,
    "faces": 0,
    "texts": 0
  },
  "counts_after": {
    "objects_total": 14,
    "groups": 7,
    "wires": 0,
    "faces": 0,
    "texts": 0
  },
  "counts_delta": {
    "objects_total": 14,
    "groups": 7,
    "wires": 0,
    "faces": 0,
    "texts": 0
  },
  "finished_at": "2026-03-30T02:32:26Z",
  "runtime_seconds": 1.472,
  "_returncode": 0,
  "_wall_seconds": 1.865,
  "_input_pdf": "C:\\Users\\Rowdy Payton\\Downloads\\Alvord TX \u2014 Garden Plan \u00b7 Final.pdf"
}
```

### PDFVectorImporter/qa_runs/20260329_213208/SU-ALV-01.json

- Path: `PDFVectorImporter/qa_runs/20260329_213208/SU-ALV-01.json`
- Size: `2.16 KB`
- Modified: `2026-03-29 21:36:50`

```json
{
  "test_id": "SU-ALV-01",
  "platform": "SU",
  "status": "PASS",
  "message": "Import completed.",
  "started_at": "2026-03-30T02:36:33Z",
  "loader": "C:/Users/Rowdy Payton/AppData/Roaming/SketchUp/SketchUp 2017/SketchUp/Plugins/bc_pdf_vector_importer/main",
  "input_pdf": "C:\\Users\\Rowdy Payton\\Downloads\\TX_Alvord_20220525_TM_geo.pdf",
  "preset": "Full",
  "page_range": "all",
  "pipeline_stats": {
    "pages": 1,
    "primitives": 0,
    "edges": 0,
    "faces": 0,
    "arcs": 0,
    "text": 0,
    "components": 0,
    "layers": [
      "??\u0000L\u0000a\u0000b\u0000e\u0000l\u0000s",
      "Map Collar",
      "Map Elements",
      "Map Frame",
      "Boundaries",
      "Federal Administrated Lands",
      "Forest Service",
      "Jurisdictional Boundaries",
      "County or Equivalent",
      "State or Territory",
      "Woodland",
      "Terrain",
      "Shaded Relief",
      "Contours",
      "Hydrography",
      "Wetlands",
      "Transportation",
      "Airports",
      "Railroads",
      "Road Features",
      "Road Names and Shields",
      "Structures",
      "Geographic Names",
      "Projection and Grids",
      "Images",
      "Orthoimage",
      "Barcode"
    ],
    "cleanup": {},
    "generic": null,
    "mode_used": null,
    "xobjects": 0,
    "text_mode": "geometry",
    "raster_fallback_used": true,
    "elapsed_seconds": 16.6,
    "log_path": "C:/TMP/bc_pdf_importer/last_import.log"
  },
  "model_counts_before": {
    "edges": 0,
    "faces": 0,
    "groups": 0,
    "component_instances": 0,
    "texts": 0,
    "images": 0
  },
  "model_counts_after": {
    "edges": 0,
    "faces": 0,
    "groups": 0,
    "component_instances": 0,
    "texts": 0,
    "images": 1
  },
  "model_delta": {
    "edges": 0,
    "faces": 0,
    "groups": 0,
    "component_instances": 0,
    "texts": 0,
    "images": 1
  },
  "layers_before": 1,
  "layers_after": 29,
  "layers_delta": 28,
  "finished_at": "2026-03-30T02:36:49Z",
  "runtime_seconds": 16.61,
  "_returncode": 0,
  "_wall_seconds": 263.182,
  "_input_pdf": "C:\\Users\\Rowdy Payton\\Downloads\\TX_Alvord_20220525_TM_geo.pdf"
}
```

### PDFVectorImporter/qa_runs/20260329_213208/SU-ALV-02.json

- Path: `PDFVectorImporter/qa_runs/20260329_213208/SU-ALV-02.json`
- Size: `1.61 KB`
- Modified: `2026-03-29 21:37:03`

```json
{
  "test_id": "SU-ALV-02",
  "platform": "SU",
  "status": "PASS",
  "message": "Import completed.",
  "started_at": "2026-03-30T02:37:01Z",
  "loader": "C:/Users/Rowdy Payton/AppData/Roaming/SketchUp/SketchUp 2017/SketchUp/Plugins/bc_pdf_vector_importer/main",
  "input_pdf": "C:\\Users\\Rowdy Payton\\Downloads\\alvord_plant_list.pdf",
  "preset": "Full",
  "page_range": "all",
  "pipeline_stats": {
    "pages": 2,
    "primitives": 125,
    "edges": 11018,
    "faces": 87,
    "arcs": 0,
    "text": 2767,
    "components": 0,
    "layers": [],
    "cleanup": {
      "merged_verts": 0,
      "removed_dupes": 0,
      "removed_micro": 0,
      "joined_collinear": 0,
      "closed_gaps": 0
    },
    "generic": null,
    "mode_used": null,
    "xobjects": 0,
    "text_mode": "geometry",
    "elapsed_seconds": 1.4,
    "log_path": "C:/TMP/bc_pdf_importer/last_import.log"
  },
  "model_counts_before": {
    "edges": 0,
    "faces": 0,
    "groups": 0,
    "component_instances": 0,
    "texts": 0,
    "images": 0
  },
  "model_counts_after": {
    "edges": 10946,
    "faces": 87,
    "groups": 8,
    "component_instances": 2767,
    "texts": 0,
    "images": 0
  },
  "model_delta": {
    "edges": 10946,
    "faces": 87,
    "groups": 8,
    "component_instances": 2767,
    "texts": 0,
    "images": 0
  },
  "layers_before": 1,
  "layers_after": 4,
  "layers_delta": 3,
  "finished_at": "2026-03-30T02:37:03Z",
  "runtime_seconds": 1.423,
  "_returncode": 0,
  "_wall_seconds": 12.105,
  "_input_pdf": "C:\\Users\\Rowdy Payton\\Downloads\\alvord_plant_list.pdf"
}
```

### PDFVectorImporter/qa_runs/20260329_213208/SU-ALV-03.json

- Path: `PDFVectorImporter/qa_runs/20260329_213208/SU-ALV-03.json`
- Size: `1.63 KB`
- Modified: `2026-03-29 21:37:15`

```json
{
  "test_id": "SU-ALV-03",
  "platform": "SU",
  "status": "PASS",
  "message": "Import completed.",
  "started_at": "2026-03-30T02:37:10Z",
  "loader": "C:/Users/Rowdy Payton/AppData/Roaming/SketchUp/SketchUp 2017/SketchUp/Plugins/bc_pdf_vector_importer/main",
  "input_pdf": "C:\\Users\\Rowdy Payton\\Downloads\\alvord_garden_map_PRINT.pdf",
  "preset": "Full",
  "page_range": "all",
  "pipeline_stats": {
    "pages": 4,
    "primitives": 1769,
    "edges": 47432,
    "faces": 1082,
    "arcs": 0,
    "text": 7224,
    "components": 0,
    "layers": [],
    "cleanup": {
      "merged_verts": 0,
      "removed_dupes": 0,
      "removed_micro": 0,
      "joined_collinear": 0,
      "closed_gaps": 0
    },
    "generic": null,
    "mode_used": null,
    "xobjects": 0,
    "text_mode": "geometry",
    "elapsed_seconds": 4.7,
    "log_path": "C:/TMP/bc_pdf_importer/last_import.log"
  },
  "model_counts_before": {
    "edges": 0,
    "faces": 0,
    "groups": 0,
    "component_instances": 0,
    "texts": 0,
    "images": 0
  },
  "model_counts_after": {
    "edges": 54638,
    "faces": 1082,
    "groups": 34,
    "component_instances": 7224,
    "texts": 0,
    "images": 0
  },
  "model_delta": {
    "edges": 54638,
    "faces": 1082,
    "groups": 34,
    "component_instances": 7224,
    "texts": 0,
    "images": 0
  },
  "layers_before": 1,
  "layers_after": 4,
  "layers_delta": 3,
  "finished_at": "2026-03-30T02:37:15Z",
  "runtime_seconds": 4.784,
  "_returncode": 0,
  "_wall_seconds": 11.108,
  "_input_pdf": "C:\\Users\\Rowdy Payton\\Downloads\\alvord_garden_map_PRINT.pdf"
}
```

### PDFVectorImporter/qa_runs/20260329_213208/SU-ALV-04.json

- Path: `PDFVectorImporter/qa_runs/20260329_213208/SU-ALV-04.json`
- Size: `1.52 KB`
- Modified: `2026-03-29 21:37:29`

```json
{
  "test_id": "SU-ALV-04",
  "platform": "SU",
  "status": "PASS",
  "message": "Import completed.",
  "started_at": "2026-03-30T02:37:22Z",
  "loader": "C:/Users/Rowdy Payton/AppData/Roaming/SketchUp/SketchUp 2017/SketchUp/Plugins/bc_pdf_vector_importer/main",
  "input_pdf": "C:\\Users\\Rowdy Payton\\Downloads\\Alvord TX ??? Garden Map ?? Final.pdf",
  "preset": "Full",
  "page_range": "all",
  "pipeline_stats": {
    "pages": 1,
    "primitives": 0,
    "edges": 0,
    "faces": 0,
    "arcs": 0,
    "text": 0,
    "components": 0,
    "layers": [],
    "cleanup": {},
    "generic": null,
    "mode_used": null,
    "xobjects": 0,
    "text_mode": "geometry",
    "raster_fallback_used": true,
    "elapsed_seconds": 6.1,
    "log_path": "C:/TMP/bc_pdf_importer/last_import.log"
  },
  "model_counts_before": {
    "edges": 0,
    "faces": 0,
    "groups": 0,
    "component_instances": 0,
    "texts": 0,
    "images": 0
  },
  "model_counts_after": {
    "edges": 0,
    "faces": 0,
    "groups": 0,
    "component_instances": 0,
    "texts": 0,
    "images": 1
  },
  "model_delta": {
    "edges": 0,
    "faces": 0,
    "groups": 0,
    "component_instances": 0,
    "texts": 0,
    "images": 1
  },
  "layers_before": 1,
  "layers_after": 2,
  "layers_delta": 1,
  "finished_at": "2026-03-30T02:37:28Z",
  "runtime_seconds": 6.097,
  "_returncode": 0,
  "_wall_seconds": 12.169,
  "_input_pdf": "C:\\Users\\Rowdy Payton\\Downloads\\Alvord TX \u2014 Garden Map \u00b7 Final.pdf"
}
```

### PDFVectorImporter/qa_runs/20260329_213208/SU-ALV-05.json

- Path: `PDFVectorImporter/qa_runs/20260329_213208/SU-ALV-05.json`
- Size: `1.52 KB`
- Modified: `2026-03-29 21:37:46`

```json
{
  "test_id": "SU-ALV-05",
  "platform": "SU",
  "status": "PASS",
  "message": "Import completed.",
  "started_at": "2026-03-30T02:37:35Z",
  "loader": "C:/Users/Rowdy Payton/AppData/Roaming/SketchUp/SketchUp 2017/SketchUp/Plugins/bc_pdf_vector_importer/main",
  "input_pdf": "C:\\Users\\Rowdy Payton\\Downloads\\Alvord TX ??? Garden Plan ?? Final.pdf",
  "preset": "Full",
  "page_range": "all",
  "pipeline_stats": {
    "pages": 7,
    "primitives": 0,
    "edges": 0,
    "faces": 0,
    "arcs": 0,
    "text": 0,
    "components": 0,
    "layers": [],
    "cleanup": {},
    "generic": null,
    "mode_used": null,
    "xobjects": 0,
    "text_mode": "geometry",
    "raster_fallback_used": true,
    "elapsed_seconds": 10.1,
    "log_path": "C:/TMP/bc_pdf_importer/last_import.log"
  },
  "model_counts_before": {
    "edges": 0,
    "faces": 0,
    "groups": 0,
    "component_instances": 0,
    "texts": 0,
    "images": 0
  },
  "model_counts_after": {
    "edges": 0,
    "faces": 0,
    "groups": 0,
    "component_instances": 0,
    "texts": 0,
    "images": 7
  },
  "model_delta": {
    "edges": 0,
    "faces": 0,
    "groups": 0,
    "component_instances": 0,
    "texts": 0,
    "images": 7
  },
  "layers_before": 1,
  "layers_after": 2,
  "layers_delta": 1,
  "finished_at": "2026-03-30T02:37:45Z",
  "runtime_seconds": 10.089,
  "_returncode": 0,
  "_wall_seconds": 16.112,
  "_input_pdf": "C:\\Users\\Rowdy Payton\\Downloads\\Alvord TX \u2014 Garden Plan \u00b7 Final.pdf"
}
```

### PDFVectorImporter/qa_runs/cross_platform_20260403/bl_results.json

- Path: `PDFVectorImporter/qa_runs/cross_platform_20260403/bl_results.json`
- Size: `375.00 B`
- Modified: `2026-04-03 18:41:03`

```json
{
  "total": 1,
  "passed": 1,
  "failed": 0,
  "blocked": 0,
  "p0_failed": 0,
  "results": [
    {
      "test_id": "BL-SMOKE-001",
      "platform": "BL",
      "priority": "P0",
      "automation": "AUTO",
      "result": "Pass",
      "runtime_seconds": 0.349,
      "notes": "Imported 178 primitives across 1 page(s). | adapter_status=PASS"
    }
  ]
}
```

### PDFVectorImporter/qa_runs/cross_platform_20260403/lc_results.json

- Path: `PDFVectorImporter/qa_runs/cross_platform_20260403/lc_results.json`
- Size: `356.00 B`
- Modified: `2026-04-03 18:41:03`

```json
{
  "total": 1,
  "passed": 1,
  "failed": 0,
  "blocked": 0,
  "p0_failed": 0,
  "results": [
    {
      "test_id": "LC-SMOKE-001",
      "platform": "LC",
      "priority": "P0",
      "automation": "AUTO",
      "result": "Pass",
      "runtime_seconds": 1.091,
      "notes": "Exported 265 entities. | adapter_status=PASS"
    }
  ]
}
```

### PDFVectorImporter/qa_runs/cross_platform_20260403/qa_config_cross_platform.json

- Path: `PDFVectorImporter/qa_runs/cross_platform_20260403/qa_config_cross_platform.json`
- Size: `1.80 KB`
- Modified: `2026-04-03 18:40:23`

```json
{
  "workspace": "C:/1FC-PDFimporter/PDFVectorImporter",
  "adapters": {
    "sketchup": {
      "command": "python adapters/sketchup_adapter.py --config qa_runs/cross_platform_20260403/qa_config_cross_platform.json --test-id {test_id} --input \"{input}\"",
      "timeout_seconds": 420
    },
    "freecad": {
      "command": "python adapters/freecad_adapter.py --config qa_runs/cross_platform_20260403/qa_config_cross_platform.json --test-id {test_id} --input \"{input}\"",
      "timeout_seconds": 1800
    },
    "blender": {
      "command": "python adapters/blender_adapter.py --config qa_runs/cross_platform_20260403/qa_config_cross_platform.json --test-id {test_id} --input \"{input}\" --preset technical --page-range 1 --min-primitives 1",
      "timeout_seconds": 1800
    },
    "librecad": {
      "command": "python adapters/librecad_adapter.py --config qa_runs/cross_platform_20260403/qa_config_cross_platform.json --test-id {test_id} --input \"{input}\" --preset technical --page-range 1 --min-entities 1",
      "timeout_seconds": 1800
    }
  },
  "sketchup": {
    "automation_supported": false,
    "exe": "C:/Program Files/SketchUp/SketchUp 2017/SketchUp.exe",
    "plugins_dir": "%APPDATA%/SketchUp/SketchUp 2017/SketchUp/Plugins",
    "extension_root": "%APPDATA%/SketchUp/SketchUp 2017/SketchUp/Plugins/bc_pdf_vector_importer",
    "ruby_harness": "adapters/sketchup_harness.rb"
  },
  "freecad": {
    "freecadcmd_exe": "C:/Program Files/FreeCAD 1.0/bin/FreeCADCmd.exe",
    "mod_dir": "%APPDATA%/FreeCAD/Mod/PDFVectorImporter",
    "python_harness": "adapters/freecad_harness.py"
  },
  "blender": {
    "repo_dir": "C:/1BL-PDFimporter",
    "python_exe": "python",
    "timeout_seconds": 1800
  },
  "librecad": {
    "repo_dir": "C:/1LC-PDFimporter",
    "python_exe": "python",
    "timeout_seconds": 1800
  }
}
```

### PDFVectorImporter/qa_runs/feature_compare_20260404_033716/feature_matrix.json

- Path: `PDFVectorImporter/qa_runs/feature_compare_20260404_033716/feature_matrix.json`
- Size: `5.72 KB`
- Modified: `2026-04-04 03:37:17`

```json
{
  "generated_at_local": "2026-04-04 03:37:17",
  "repos": {
    "SU": "C:\\1SU-PDFimporter",
    "FC": "C:\\1FC-PDFimporter",
    "BL": "C:\\1BL-PDFimporter",
    "LC": "C:\\1LC-PDFimporter",
    "APP": "C:\\1 Structural_Steel_Shapes_App"
  },
  "summary": {
    "SU": {
      "applicable": 19,
      "yes": 16,
      "no": 3
    },
    "FC": {
      "applicable": 19,
      "yes": 19,
      "no": 0
    },
    "BL": {
      "applicable": 20,
      "yes": 18,
      "no": 2
    },
    "LC": {
      "applicable": 20,
      "yes": 18,
      "no": 2
    },
    "APP": {
      "applicable": 3,
      "yes": 3,
      "no": 0
    }
  },
  "features": [
    {
      "key": "vector_primitives",
      "label": "Vector primitive extraction",
      "status": {
        "SU": "yes",
        "FC": "yes",
        "BL": "yes",
        "LC": "yes",
        "APP": "na"
      }
    },
    {
      "key": "arc_rebuild",
      "label": "Arc/circle reconstruction",
      "status": {
        "SU": "yes",
        "FC": "yes",
        "BL": "yes",
        "LC": "yes",
        "APP": "na"
      }
    },
    {
      "key": "dash_mapping",
      "label": "Dash pattern preservation",
      "status": {
        "SU": "yes",
        "FC": "yes",
        "BL": "yes",
        "LC": "yes",
        "APP": "na"
      }
    },
    {
      "key": "text_labels",
      "label": "Text as labels",
      "status": {
        "SU": "yes",
        "FC": "yes",
        "BL": "yes",
        "LC": "yes",
        "APP": "na"
      }
    },
    {
      "key": "text_geometry",
      "label": "Text as geometry",
      "status": {
        "SU": "yes",
        "FC": "yes",
        "BL": "yes",
        "LC": "yes",
        "APP": "na"
      }
    },
    {
      "key": "strict_text",
      "label": "Strict text fidelity mode",
      "status": {
        "SU": "yes",
        "FC": "yes",
        "BL": "yes",
        "LC": "yes",
        "APP": "na"
      }
    },
    {
      "key": "embedded_images",
      "label": "Embedded image extraction",
      "status": {
        "SU": "no",
        "FC": "yes",
        "BL": "yes",
        "LC": "yes",
        "APP": "na"
      }
    },
    {
      "key": "raster_only",
      "label": "Raster-only mode",
      "status": {
        "SU": "yes",
        "FC": "yes",
        "BL": "yes",
        "LC": "yes",
        "APP": "na"
      }
    },
    {
      "key": "hybrid_mode",
      "label": "Hybrid raster+vector mode",
      "status": {
        "SU": "no",
        "FC": "yes",
        "BL": "yes",
        "LC": "yes",
        "APP": "na"
      }
    },
    {
      "key": "hatch_modes",
      "label": "Hatch handling modes",
      "status": {
        "SU": "yes",
        "FC": "yes",
        "BL": "yes",
        "LC": "yes",
        "APP": "na"
      }
    },
    {
      "key": "ocg_layers",
      "label": "OCG/layer mapping",
      "status": {
        "SU": "yes",
        "FC": "yes",
        "BL": "yes",
        "LC": "yes",
        "APP": "na"
      }
    },
    {
      "key": "grouping_modes",
      "label": "Advanced grouping modes",
      "status": {
        "SU": "yes",
        "FC": "yes",
        "BL": "yes",
        "LC": "yes",
        "APP": "na"
      }
    },
    {
      "key": "lineweight_modes",
      "label": "Lineweight handling modes",
      "status": {
        "SU": "yes",
        "FC": "yes",
        "BL": "yes",
        "LC": "yes",
        "APP": "na"
      }
    },
    {
      "key": "doc_profiling",
      "label": "Document profiling/classification",
      "status": {
        "SU": "yes",
        "FC": "yes",
        "BL": "yes",
        "LC": "yes",
        "APP": "na"
      }
    },
    {
      "key": "scale_reference",
      "label": "Scale by reference tooling",
      "status": {
        "SU": "yes",
        "FC": "yes",
        "BL": "no",
        "LC": "yes",
        "APP": "na"
      }
    },
    {
      "key": "cli_surface",
      "label": "CLI surface",
      "status": {
        "SU": "no",
        "FC": "yes",
        "BL": "yes",
        "LC": "yes",
        "APP": "na"
      }
    },
    {
      "key": "gui_surface",
      "label": "GUI surface",
      "status": {
        "SU": "yes",
        "FC": "yes",
        "BL": "yes",
        "LC": "yes",
        "APP": "na"
      }
    },
    {
      "key": "batch_import",
      "label": "Batch import workflows",
      "status": {
        "SU": "yes",
        "FC": "yes",
        "BL": "no",
        "LC": "no",
        "APP": "na"
      }
    },
    {
      "key": "qa_automation",
      "label": "Automated QA harness",
      "status": {
        "SU": "yes",
        "FC": "yes",
        "BL": "yes",
        "LC": "no",
        "APP": "na"
      }
    },
    {
      "key": "all_pages_default",
      "label": "Default imports all pages",
      "status": {
        "SU": "na",
        "FC": "na",
        "BL": "yes",
        "LC": "yes",
        "APP": "na"
      }
    },
    {
      "key": "app_aisc",
      "label": "AISC dataset integration",
      "status": {
        "SU": "na",
        "FC": "na",
        "BL": "na",
        "LC": "na",
        "APP": "yes"
      }
    },
    {
      "key": "app_measurement_engine",
      "label": "Measurement/unit parsing engine",
      "status": {
        "SU": "na",
        "FC": "na",
        "BL": "na",
        "LC": "na",
        "APP": "yes"
      }
    },
    {
      "key": "app_svg_blueprints",
      "label": "SVG blueprint rendering",
      "status": {
        "SU": "na",
        "FC": "na",
        "BL": "na",
        "LC": "na",
        "APP": "yes"
      }
    }
  ]
}
```

### PDFVectorImporter/qa_runs/feature_compare_20260404_033716/feature_matrix.md

- Path: `PDFVectorImporter/qa_runs/feature_compare_20260404_033716/feature_matrix.md`
- Size: `1.67 KB`
- Modified: `2026-04-04 03:37:17`

```markdown
# Cross-Repo Feature Matrix

Generated: 2026-04-04 03:37:17

| Feature | SU | FC | BL | LC | App |
|---|---|---|---|---|---|
| Vector primitive extraction | Yes | Yes | Yes | Yes | N/A |
| Arc/circle reconstruction | Yes | Yes | Yes | Yes | N/A |
| Dash pattern preservation | Yes | Yes | Yes | Yes | N/A |
| Text as labels | Yes | Yes | Yes | Yes | N/A |
| Text as geometry | Yes | Yes | Yes | Yes | N/A |
| Strict text fidelity mode | Yes | Yes | Yes | Yes | N/A |
| Embedded image extraction | No | Yes | Yes | Yes | N/A |
| Raster-only mode | Yes | Yes | Yes | Yes | N/A |
| Hybrid raster+vector mode | No | Yes | Yes | Yes | N/A |
| Hatch handling modes | Yes | Yes | Yes | Yes | N/A |
| OCG/layer mapping | Yes | Yes | Yes | Yes | N/A |
| Advanced grouping modes | Yes | Yes | Yes | Yes | N/A |
| Lineweight handling modes | Yes | Yes | Yes | Yes | N/A |
| Document profiling/classification | Yes | Yes | Yes | Yes | N/A |
| Scale by reference tooling | Yes | Yes | No | Yes | N/A |
| CLI surface | No | Yes | Yes | Yes | N/A |
| GUI surface | Yes | Yes | Yes | Yes | N/A |
| Batch import workflows | Yes | Yes | No | No | N/A |
| Automated QA harness | Yes | Yes | Yes | No | N/A |
| Default imports all pages | N/A | N/A | Yes | Yes | N/A |
| AISC dataset integration | N/A | N/A | N/A | N/A | Yes |
| Measurement/unit parsing engine | N/A | N/A | N/A | N/A | Yes |
| SVG blueprint rendering | N/A | N/A | N/A | N/A | Yes |

## Coverage Summary

| Repo | Applicable | Yes | No | Coverage |
|---|---:|---:|---:|---:|
| SU | 19 | 16 | 3 | 84.2% |
| FC | 19 | 19 | 0 | 100.0% |
| BL | 20 | 18 | 2 | 90.0% |
| LC | 20 | 18 | 2 | 90.0% |
| APP | 3 | 3 | 0 | 100.0% |
```

### PDFVectorImporter/qa_runs/feature_compare_20260404_034635/feature_matrix.json

- Path: `PDFVectorImporter/qa_runs/feature_compare_20260404_034635/feature_matrix.json`
- Size: `5.72 KB`
- Modified: `2026-04-04 03:46:36`

```json
{
  "generated_at_local": "2026-04-04 03:46:36",
  "repos": {
    "SU": "C:\\1SU-PDFimporter",
    "FC": "C:\\1FC-PDFimporter",
    "BL": "C:\\1BL-PDFimporter",
    "LC": "C:\\1LC-PDFimporter",
    "APP": "C:\\1 Structural_Steel_Shapes_App"
  },
  "summary": {
    "SU": {
      "applicable": 19,
      "yes": 16,
      "no": 3
    },
    "FC": {
      "applicable": 19,
      "yes": 19,
      "no": 0
    },
    "BL": {
      "applicable": 20,
      "yes": 19,
      "no": 1
    },
    "LC": {
      "applicable": 20,
      "yes": 18,
      "no": 2
    },
    "APP": {
      "applicable": 3,
      "yes": 3,
      "no": 0
    }
  },
  "features": [
    {
      "key": "vector_primitives",
      "label": "Vector primitive extraction",
      "status": {
        "SU": "yes",
        "FC": "yes",
        "BL": "yes",
        "LC": "yes",
        "APP": "na"
      }
    },
    {
      "key": "arc_rebuild",
      "label": "Arc/circle reconstruction",
      "status": {
        "SU": "yes",
        "FC": "yes",
        "BL": "yes",
        "LC": "yes",
        "APP": "na"
      }
    },
    {
      "key": "dash_mapping",
      "label": "Dash pattern preservation",
      "status": {
        "SU": "yes",
        "FC": "yes",
        "BL": "yes",
        "LC": "yes",
        "APP": "na"
      }
    },
    {
      "key": "text_labels",
      "label": "Text as labels",
      "status": {
        "SU": "yes",
        "FC": "yes",
        "BL": "yes",
        "LC": "yes",
        "APP": "na"
      }
    },
    {
      "key": "text_geometry",
      "label": "Text as geometry",
      "status": {
        "SU": "yes",
        "FC": "yes",
        "BL": "yes",
        "LC": "yes",
        "APP": "na"
      }
    },
    {
      "key": "strict_text",
      "label": "Strict text fidelity mode",
      "status": {
        "SU": "yes",
        "FC": "yes",
        "BL": "yes",
        "LC": "yes",
        "APP": "na"
      }
    },
    {
      "key": "embedded_images",
      "label": "Embedded image extraction",
      "status": {
        "SU": "no",
        "FC": "yes",
        "BL": "yes",
        "LC": "yes",
        "APP": "na"
      }
    },
    {
      "key": "raster_only",
      "label": "Raster-only mode",
      "status": {
        "SU": "yes",
        "FC": "yes",
        "BL": "yes",
        "LC": "yes",
        "APP": "na"
      }
    },
    {
      "key": "hybrid_mode",
      "label": "Hybrid raster+vector mode",
      "status": {
        "SU": "no",
        "FC": "yes",
        "BL": "yes",
        "LC": "yes",
        "APP": "na"
      }
    },
    {
      "key": "hatch_modes",
      "label": "Hatch handling modes",
      "status": {
        "SU": "yes",
        "FC": "yes",
        "BL": "yes",
        "LC": "yes",
        "APP": "na"
      }
    },
    {
      "key": "ocg_layers",
      "label": "OCG/layer mapping",
      "status": {
        "SU": "yes",
        "FC": "yes",
        "BL": "yes",
        "LC": "yes",
        "APP": "na"
      }
    },
    {
      "key": "grouping_modes",
      "label": "Advanced grouping modes",
      "status": {
        "SU": "yes",
        "FC": "yes",
        "BL": "yes",
        "LC": "yes",
        "APP": "na"
      }
    },
    {
      "key": "lineweight_modes",
      "label": "Lineweight handling modes",
      "status": {
        "SU": "yes",
        "FC": "yes",
        "BL": "yes",
        "LC": "yes",
        "APP": "na"
      }
    },
    {
      "key": "doc_profiling",
      "label": "Document profiling/classification",
      "status": {
        "SU": "yes",
        "FC": "yes",
        "BL": "yes",
        "LC": "yes",
        "APP": "na"
      }
    },
    {
      "key": "scale_reference",
      "label": "Scale by reference tooling",
      "status": {
        "SU": "yes",
        "FC": "yes",
        "BL": "yes",
        "LC": "yes",
        "APP": "na"
      }
    },
    {
      "key": "cli_surface",
      "label": "CLI surface",
      "status": {
        "SU": "no",
        "FC": "yes",
        "BL": "yes",
        "LC": "yes",
        "APP": "na"
      }
    },
    {
      "key": "gui_surface",
      "label": "GUI surface",
      "status": {
        "SU": "yes",
        "FC": "yes",
        "BL": "yes",
        "LC": "yes",
        "APP": "na"
      }
    },
    {
      "key": "batch_import",
      "label": "Batch import workflows",
      "status": {
        "SU": "yes",
        "FC": "yes",
        "BL": "no",
        "LC": "no",
        "APP": "na"
      }
    },
    {
      "key": "qa_automation",
      "label": "Automated QA harness",
      "status": {
        "SU": "yes",
        "FC": "yes",
        "BL": "yes",
        "LC": "no",
        "APP": "na"
      }
    },
    {
      "key": "all_pages_default",
      "label": "Default imports all pages",
      "status": {
        "SU": "na",
        "FC": "na",
        "BL": "yes",
        "LC": "yes",
        "APP": "na"
      }
    },
    {
      "key": "app_aisc",
      "label": "AISC dataset integration",
      "status": {
        "SU": "na",
        "FC": "na",
        "BL": "na",
        "LC": "na",
        "APP": "yes"
      }
    },
    {
      "key": "app_measurement_engine",
      "label": "Measurement/unit parsing engine",
      "status": {
        "SU": "na",
        "FC": "na",
        "BL": "na",
        "LC": "na",
        "APP": "yes"
      }
    },
    {
      "key": "app_svg_blueprints",
      "label": "SVG blueprint rendering",
      "status": {
        "SU": "na",
        "FC": "na",
        "BL": "na",
        "LC": "na",
        "APP": "yes"
      }
    }
  ]
}
```

### PDFVectorImporter/qa_runs/feature_compare_20260404_034635/feature_matrix.md

- Path: `PDFVectorImporter/qa_runs/feature_compare_20260404_034635/feature_matrix.md`
- Size: `1.67 KB`
- Modified: `2026-04-04 03:46:36`

```markdown
# Cross-Repo Feature Matrix

Generated: 2026-04-04 03:46:36

| Feature | SU | FC | BL | LC | App |
|---|---|---|---|---|---|
| Vector primitive extraction | Yes | Yes | Yes | Yes | N/A |
| Arc/circle reconstruction | Yes | Yes | Yes | Yes | N/A |
| Dash pattern preservation | Yes | Yes | Yes | Yes | N/A |
| Text as labels | Yes | Yes | Yes | Yes | N/A |
| Text as geometry | Yes | Yes | Yes | Yes | N/A |
| Strict text fidelity mode | Yes | Yes | Yes | Yes | N/A |
| Embedded image extraction | No | Yes | Yes | Yes | N/A |
| Raster-only mode | Yes | Yes | Yes | Yes | N/A |
| Hybrid raster+vector mode | No | Yes | Yes | Yes | N/A |
| Hatch handling modes | Yes | Yes | Yes | Yes | N/A |
| OCG/layer mapping | Yes | Yes | Yes | Yes | N/A |
| Advanced grouping modes | Yes | Yes | Yes | Yes | N/A |
| Lineweight handling modes | Yes | Yes | Yes | Yes | N/A |
| Document profiling/classification | Yes | Yes | Yes | Yes | N/A |
| Scale by reference tooling | Yes | Yes | Yes | Yes | N/A |
| CLI surface | No | Yes | Yes | Yes | N/A |
| GUI surface | Yes | Yes | Yes | Yes | N/A |
| Batch import workflows | Yes | Yes | No | No | N/A |
| Automated QA harness | Yes | Yes | Yes | No | N/A |
| Default imports all pages | N/A | N/A | Yes | Yes | N/A |
| AISC dataset integration | N/A | N/A | N/A | N/A | Yes |
| Measurement/unit parsing engine | N/A | N/A | N/A | N/A | Yes |
| SVG blueprint rendering | N/A | N/A | N/A | N/A | Yes |

## Coverage Summary

| Repo | Applicable | Yes | No | Coverage |
|---|---:|---:|---:|---:|
| SU | 19 | 16 | 3 | 84.2% |
| FC | 19 | 19 | 0 | 100.0% |
| BL | 20 | 19 | 1 | 95.0% |
| LC | 20 | 18 | 2 | 90.0% |
| APP | 3 | 3 | 0 | 100.0% |
```

### PDFVectorImporter/qa_runs/feature_compare_20260404_034914/feature_matrix.json

- Path: `PDFVectorImporter/qa_runs/feature_compare_20260404_034914/feature_matrix.json`
- Size: `5.72 KB`
- Modified: `2026-04-04 03:49:14`

```json
{
  "generated_at_local": "2026-04-04 03:49:14",
  "repos": {
    "SU": "C:\\1SU-PDFimporter",
    "FC": "C:\\1FC-PDFimporter",
    "BL": "C:\\1BL-PDFimporter",
    "LC": "C:\\1LC-PDFimporter",
    "APP": "C:\\1 Structural_Steel_Shapes_App"
  },
  "summary": {
    "SU": {
      "applicable": 19,
      "yes": 16,
      "no": 3
    },
    "FC": {
      "applicable": 19,
      "yes": 19,
      "no": 0
    },
    "BL": {
      "applicable": 20,
      "yes": 20,
      "no": 0
    },
    "LC": {
      "applicable": 20,
      "yes": 19,
      "no": 1
    },
    "APP": {
      "applicable": 3,
      "yes": 3,
      "no": 0
    }
  },
  "features": [
    {
      "key": "vector_primitives",
      "label": "Vector primitive extraction",
      "status": {
        "SU": "yes",
        "FC": "yes",
        "BL": "yes",
        "LC": "yes",
        "APP": "na"
      }
    },
    {
      "key": "arc_rebuild",
      "label": "Arc/circle reconstruction",
      "status": {
        "SU": "yes",
        "FC": "yes",
        "BL": "yes",
        "LC": "yes",
        "APP": "na"
      }
    },
    {
      "key": "dash_mapping",
      "label": "Dash pattern preservation",
      "status": {
        "SU": "yes",
        "FC": "yes",
        "BL": "yes",
        "LC": "yes",
        "APP": "na"
      }
    },
    {
      "key": "text_labels",
      "label": "Text as labels",
      "status": {
        "SU": "yes",
        "FC": "yes",
        "BL": "yes",
        "LC": "yes",
        "APP": "na"
      }
    },
    {
      "key": "text_geometry",
      "label": "Text as geometry",
      "status": {
        "SU": "yes",
        "FC": "yes",
        "BL": "yes",
        "LC": "yes",
        "APP": "na"
      }
    },
    {
      "key": "strict_text",
      "label": "Strict text fidelity mode",
      "status": {
        "SU": "yes",
        "FC": "yes",
        "BL": "yes",
        "LC": "yes",
        "APP": "na"
      }
    },
    {
      "key": "embedded_images",
      "label": "Embedded image extraction",
      "status": {
        "SU": "no",
        "FC": "yes",
        "BL": "yes",
        "LC": "yes",
        "APP": "na"
      }
    },
    {
      "key": "raster_only",
      "label": "Raster-only mode",
      "status": {
        "SU": "yes",
        "FC": "yes",
        "BL": "yes",
        "LC": "yes",
        "APP": "na"
      }
    },
    {
      "key": "hybrid_mode",
      "label": "Hybrid raster+vector mode",
      "status": {
        "SU": "no",
        "FC": "yes",
        "BL": "yes",
        "LC": "yes",
        "APP": "na"
      }
    },
    {
      "key": "hatch_modes",
      "label": "Hatch handling modes",
      "status": {
        "SU": "yes",
        "FC": "yes",
        "BL": "yes",
        "LC": "yes",
        "APP": "na"
      }
    },
    {
      "key": "ocg_layers",
      "label": "OCG/layer mapping",
      "status": {
        "SU": "yes",
        "FC": "yes",
        "BL": "yes",
        "LC": "yes",
        "APP": "na"
      }
    },
    {
      "key": "grouping_modes",
      "label": "Advanced grouping modes",
      "status": {
        "SU": "yes",
        "FC": "yes",
        "BL": "yes",
        "LC": "yes",
        "APP": "na"
      }
    },
    {
      "key": "lineweight_modes",
      "label": "Lineweight handling modes",
      "status": {
        "SU": "yes",
        "FC": "yes",
        "BL": "yes",
        "LC": "yes",
        "APP": "na"
      }
    },
    {
      "key": "doc_profiling",
      "label": "Document profiling/classification",
      "status": {
        "SU": "yes",
        "FC": "yes",
        "BL": "yes",
        "LC": "yes",
        "APP": "na"
      }
    },
    {
      "key": "scale_reference",
      "label": "Scale by reference tooling",
      "status": {
        "SU": "yes",
        "FC": "yes",
        "BL": "yes",
        "LC": "yes",
        "APP": "na"
      }
    },
    {
      "key": "cli_surface",
      "label": "CLI surface",
      "status": {
        "SU": "no",
        "FC": "yes",
        "BL": "yes",
        "LC": "yes",
        "APP": "na"
      }
    },
    {
      "key": "gui_surface",
      "label": "GUI surface",
      "status": {
        "SU": "yes",
        "FC": "yes",
        "BL": "yes",
        "LC": "yes",
        "APP": "na"
      }
    },
    {
      "key": "batch_import",
      "label": "Batch import workflows",
      "status": {
        "SU": "yes",
        "FC": "yes",
        "BL": "yes",
        "LC": "yes",
        "APP": "na"
      }
    },
    {
      "key": "qa_automation",
      "label": "Automated QA harness",
      "status": {
        "SU": "yes",
        "FC": "yes",
        "BL": "yes",
        "LC": "no",
        "APP": "na"
      }
    },
    {
      "key": "all_pages_default",
      "label": "Default imports all pages",
      "status": {
        "SU": "na",
        "FC": "na",
        "BL": "yes",
        "LC": "yes",
        "APP": "na"
      }
    },
    {
      "key": "app_aisc",
      "label": "AISC dataset integration",
      "status": {
        "SU": "na",
        "FC": "na",
        "BL": "na",
        "LC": "na",
        "APP": "yes"
      }
    },
    {
      "key": "app_measurement_engine",
      "label": "Measurement/unit parsing engine",
      "status": {
        "SU": "na",
        "FC": "na",
        "BL": "na",
        "LC": "na",
        "APP": "yes"
      }
    },
    {
      "key": "app_svg_blueprints",
      "label": "SVG blueprint rendering",
      "status": {
        "SU": "na",
        "FC": "na",
        "BL": "na",
        "LC": "na",
        "APP": "yes"
      }
    }
  ]
}
```

### PDFVectorImporter/qa_runs/feature_compare_20260404_034914/feature_matrix.md

- Path: `PDFVectorImporter/qa_runs/feature_compare_20260404_034914/feature_matrix.md`
- Size: `1.67 KB`
- Modified: `2026-04-04 03:49:14`

```markdown
# Cross-Repo Feature Matrix

Generated: 2026-04-04 03:49:14

| Feature | SU | FC | BL | LC | App |
|---|---|---|---|---|---|
| Vector primitive extraction | Yes | Yes | Yes | Yes | N/A |
| Arc/circle reconstruction | Yes | Yes | Yes | Yes | N/A |
| Dash pattern preservation | Yes | Yes | Yes | Yes | N/A |
| Text as labels | Yes | Yes | Yes | Yes | N/A |
| Text as geometry | Yes | Yes | Yes | Yes | N/A |
| Strict text fidelity mode | Yes | Yes | Yes | Yes | N/A |
| Embedded image extraction | No | Yes | Yes | Yes | N/A |
| Raster-only mode | Yes | Yes | Yes | Yes | N/A |
| Hybrid raster+vector mode | No | Yes | Yes | Yes | N/A |
| Hatch handling modes | Yes | Yes | Yes | Yes | N/A |
| OCG/layer mapping | Yes | Yes | Yes | Yes | N/A |
| Advanced grouping modes | Yes | Yes | Yes | Yes | N/A |
| Lineweight handling modes | Yes | Yes | Yes | Yes | N/A |
| Document profiling/classification | Yes | Yes | Yes | Yes | N/A |
| Scale by reference tooling | Yes | Yes | Yes | Yes | N/A |
| CLI surface | No | Yes | Yes | Yes | N/A |
| GUI surface | Yes | Yes | Yes | Yes | N/A |
| Batch import workflows | Yes | Yes | Yes | Yes | N/A |
| Automated QA harness | Yes | Yes | Yes | No | N/A |
| Default imports all pages | N/A | N/A | Yes | Yes | N/A |
| AISC dataset integration | N/A | N/A | N/A | N/A | Yes |
| Measurement/unit parsing engine | N/A | N/A | N/A | N/A | Yes |
| SVG blueprint rendering | N/A | N/A | N/A | N/A | Yes |

## Coverage Summary

| Repo | Applicable | Yes | No | Coverage |
|---|---:|---:|---:|---:|
| SU | 19 | 16 | 3 | 84.2% |
| FC | 19 | 19 | 0 | 100.0% |
| BL | 20 | 20 | 0 | 100.0% |
| LC | 20 | 19 | 1 | 95.0% |
| APP | 3 | 3 | 0 | 100.0% |
```

### PDFVectorImporter/qa_runs/feature_compare_20260404_034940/feature_matrix.json

- Path: `PDFVectorImporter/qa_runs/feature_compare_20260404_034940/feature_matrix.json`
- Size: `5.72 KB`
- Modified: `2026-04-04 03:49:40`

```json
{
  "generated_at_local": "2026-04-04 03:49:40",
  "repos": {
    "SU": "C:\\1SU-PDFimporter",
    "FC": "C:\\1FC-PDFimporter",
    "BL": "C:\\1BL-PDFimporter",
    "LC": "C:\\1LC-PDFimporter",
    "APP": "C:\\1 Structural_Steel_Shapes_App"
  },
  "summary": {
    "SU": {
      "applicable": 19,
      "yes": 16,
      "no": 3
    },
    "FC": {
      "applicable": 19,
      "yes": 19,
      "no": 0
    },
    "BL": {
      "applicable": 20,
      "yes": 20,
      "no": 0
    },
    "LC": {
      "applicable": 20,
      "yes": 20,
      "no": 0
    },
    "APP": {
      "applicable": 3,
      "yes": 3,
      "no": 0
    }
  },
  "features": [
    {
      "key": "vector_primitives",
      "label": "Vector primitive extraction",
      "status": {
        "SU": "yes",
        "FC": "yes",
        "BL": "yes",
        "LC": "yes",
        "APP": "na"
      }
    },
    {
      "key": "arc_rebuild",
      "label": "Arc/circle reconstruction",
      "status": {
        "SU": "yes",
        "FC": "yes",
        "BL": "yes",
        "LC": "yes",
        "APP": "na"
      }
    },
    {
      "key": "dash_mapping",
      "label": "Dash pattern preservation",
      "status": {
        "SU": "yes",
        "FC": "yes",
        "BL": "yes",
        "LC": "yes",
        "APP": "na"
      }
    },
    {
      "key": "text_labels",
      "label": "Text as labels",
      "status": {
        "SU": "yes",
        "FC": "yes",
        "BL": "yes",
        "LC": "yes",
        "APP": "na"
      }
    },
    {
      "key": "text_geometry",
      "label": "Text as geometry",
      "status": {
        "SU": "yes",
        "FC": "yes",
        "BL": "yes",
        "LC": "yes",
        "APP": "na"
      }
    },
    {
      "key": "strict_text",
      "label": "Strict text fidelity mode",
      "status": {
        "SU": "yes",
        "FC": "yes",
        "BL": "yes",
        "LC": "yes",
        "APP": "na"
      }
    },
    {
      "key": "embedded_images",
      "label": "Embedded image extraction",
      "status": {
        "SU": "no",
        "FC": "yes",
        "BL": "yes",
        "LC": "yes",
        "APP": "na"
      }
    },
    {
      "key": "raster_only",
      "label": "Raster-only mode",
      "status": {
        "SU": "yes",
        "FC": "yes",
        "BL": "yes",
        "LC": "yes",
        "APP": "na"
      }
    },
    {
      "key": "hybrid_mode",
      "label": "Hybrid raster+vector mode",
      "status": {
        "SU": "no",
        "FC": "yes",
        "BL": "yes",
        "LC": "yes",
        "APP": "na"
      }
    },
    {
      "key": "hatch_modes",
      "label": "Hatch handling modes",
      "status": {
        "SU": "yes",
        "FC": "yes",
        "BL": "yes",
        "LC": "yes",
        "APP": "na"
      }
    },
    {
      "key": "ocg_layers",
      "label": "OCG/layer mapping",
      "status": {
        "SU": "yes",
        "FC": "yes",
        "BL": "yes",
        "LC": "yes",
        "APP": "na"
      }
    },
    {
      "key": "grouping_modes",
      "label": "Advanced grouping modes",
      "status": {
        "SU": "yes",
        "FC": "yes",
        "BL": "yes",
        "LC": "yes",
        "APP": "na"
      }
    },
    {
      "key": "lineweight_modes",
      "label": "Lineweight handling modes",
      "status": {
        "SU": "yes",
        "FC": "yes",
        "BL": "yes",
        "LC": "yes",
        "APP": "na"
      }
    },
    {
      "key": "doc_profiling",
      "label": "Document profiling/classification",
      "status": {
        "SU": "yes",
        "FC": "yes",
        "BL": "yes",
        "LC": "yes",
        "APP": "na"
      }
    },
    {
      "key": "scale_reference",
      "label": "Scale by reference tooling",
      "status": {
        "SU": "yes",
        "FC": "yes",
        "BL": "yes",
        "LC": "yes",
        "APP": "na"
      }
    },
    {
      "key": "cli_surface",
      "label": "CLI surface",
      "status": {
        "SU": "no",
        "FC": "yes",
        "BL": "yes",
        "LC": "yes",
        "APP": "na"
      }
    },
    {
      "key": "gui_surface",
      "label": "GUI surface",
      "status": {
        "SU": "yes",
        "FC": "yes",
        "BL": "yes",
        "LC": "yes",
        "APP": "na"
      }
    },
    {
      "key": "batch_import",
      "label": "Batch import workflows",
      "status": {
        "SU": "yes",
        "FC": "yes",
        "BL": "yes",
        "LC": "yes",
        "APP": "na"
      }
    },
    {
      "key": "qa_automation",
      "label": "Automated QA harness",
      "status": {
        "SU": "yes",
        "FC": "yes",
        "BL": "yes",
        "LC": "yes",
        "APP": "na"
      }
    },
    {
      "key": "all_pages_default",
      "label": "Default imports all pages",
      "status": {
        "SU": "na",
        "FC": "na",
        "BL": "yes",
        "LC": "yes",
        "APP": "na"
      }
    },
    {
      "key": "app_aisc",
      "label": "AISC dataset integration",
      "status": {
        "SU": "na",
        "FC": "na",
        "BL": "na",
        "LC": "na",
        "APP": "yes"
      }
    },
    {
      "key": "app_measurement_engine",
      "label": "Measurement/unit parsing engine",
      "status": {
        "SU": "na",
        "FC": "na",
        "BL": "na",
        "LC": "na",
        "APP": "yes"
      }
    },
    {
      "key": "app_svg_blueprints",
      "label": "SVG blueprint rendering",
      "status": {
        "SU": "na",
        "FC": "na",
        "BL": "na",
        "LC": "na",
        "APP": "yes"
      }
    }
  ]
}
```

### PDFVectorImporter/qa_runs/feature_compare_20260404_034940/feature_matrix.md

- Path: `PDFVectorImporter/qa_runs/feature_compare_20260404_034940/feature_matrix.md`
- Size: `1.67 KB`
- Modified: `2026-04-04 03:49:40`

```markdown
# Cross-Repo Feature Matrix

Generated: 2026-04-04 03:49:40

| Feature | SU | FC | BL | LC | App |
|---|---|---|---|---|---|
| Vector primitive extraction | Yes | Yes | Yes | Yes | N/A |
| Arc/circle reconstruction | Yes | Yes | Yes | Yes | N/A |
| Dash pattern preservation | Yes | Yes | Yes | Yes | N/A |
| Text as labels | Yes | Yes | Yes | Yes | N/A |
| Text as geometry | Yes | Yes | Yes | Yes | N/A |
| Strict text fidelity mode | Yes | Yes | Yes | Yes | N/A |
| Embedded image extraction | No | Yes | Yes | Yes | N/A |
| Raster-only mode | Yes | Yes | Yes | Yes | N/A |
| Hybrid raster+vector mode | No | Yes | Yes | Yes | N/A |
| Hatch handling modes | Yes | Yes | Yes | Yes | N/A |
| OCG/layer mapping | Yes | Yes | Yes | Yes | N/A |
| Advanced grouping modes | Yes | Yes | Yes | Yes | N/A |
| Lineweight handling modes | Yes | Yes | Yes | Yes | N/A |
| Document profiling/classification | Yes | Yes | Yes | Yes | N/A |
| Scale by reference tooling | Yes | Yes | Yes | Yes | N/A |
| CLI surface | No | Yes | Yes | Yes | N/A |
| GUI surface | Yes | Yes | Yes | Yes | N/A |
| Batch import workflows | Yes | Yes | Yes | Yes | N/A |
| Automated QA harness | Yes | Yes | Yes | Yes | N/A |
| Default imports all pages | N/A | N/A | Yes | Yes | N/A |
| AISC dataset integration | N/A | N/A | N/A | N/A | Yes |
| Measurement/unit parsing engine | N/A | N/A | N/A | N/A | Yes |
| SVG blueprint rendering | N/A | N/A | N/A | N/A | Yes |

## Coverage Summary

| Repo | Applicable | Yes | No | Coverage |
|---|---:|---:|---:|---:|
| SU | 19 | 16 | 3 | 84.2% |
| FC | 19 | 19 | 0 | 100.0% |
| BL | 20 | 20 | 0 | 100.0% |
| LC | 20 | 20 | 0 | 100.0% |
| APP | 3 | 3 | 0 | 100.0% |
```

### PDFVectorImporter/README.md

- Path: `PDFVectorImporter/README.md`
- Size: `5.92 KB`
- Modified: `2026-04-03 18:44:01`

~~~markdown
# PDF Vector Importer for FreeCAD

![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)
![Version: 3.6.6](https://img.shields.io/badge/Version-3.6.6-green.svg)
![Platform: FreeCAD 0.21+](https://img.shields.io/badge/Platform-FreeCAD%200.21%2B-orange.svg)

**Import vector geometry, text, and images from PDF files into FreeCAD as editable Part objects.**

Arc reconstruction, dash mapping, color grouping, OCG layer support, and reference-based scaling -- all powered by pure-Python PDF parsing via PyMuPDF.

> **BlueCollar Systems** -- BUILT. NOT BOUGHT.

---

## Key Features

| Category | Capability |
|---|---|
| **PDF Parsing** | PyMuPDF-powered vector extraction with full path, text, and image support |
| **Import Presets** | Fast Preview, General Vector, Technical Drawing, Shop Drawing, Max Fidelity |
| **Arc Reconstruction** | Kasa algebraic circle fit converts polyline segments back to true arcs |
| **Layer Support** | OCG layers (PDF Optional Content Groups) map to FreeCAD groups |
| **Color Grouping** | Geometry automatically organized by stroke/fill color |
| **Dash Patterns** | Hidden, center, and phantom line types mapped from PDF dash arrays |
| **Scale by Reference** | Pick two points on a known dimension, type the real-world value |
| **Quick Scale** | Architectural presets from 1:1 through 1:200 |
| **Text Import** | Labels or exploded geometry via pdftocairo |
| **Raster Fallback** | Scanned pages imported as positioned images when no vectors are found |
| **Image Extraction** | Embedded images extracted and placed in the model |
| **Hatch Detection** | Three modes: Import, Group, or Skip detected hatch regions |
| **Batch Import** | Multi-file import and drag-and-drop support |
| **SKP Bridge** | Import SketchUp `.skp` models via workbench command when backend support exists |
| **Auto View** | Orthographic top-down view set automatically after import |

---

## Installation

1. Copy the `PDFVectorImporter` folder into your FreeCAD `Mod` directory:

   | OS | Typical Path |
   |---|---|
   | **Windows** | `%APPDATA%\FreeCAD\Mod\` |
   | **macOS** | `~/Library/Preferences/FreeCAD/Mod/` |
   | **Linux** | `~/.FreeCAD/Mod/` |

2. Restart FreeCAD.
3. Switch to the **PDF Vector Importer** workbench from the workbench selector.
4. PyMuPDF installs automatically on first use (requires pip / internet).

---

## Requirements

| Dependency | Required | Notes |
|---|---|---|
| **FreeCAD** | 0.21+ | Tested through 1.0 |
| **PyMuPDF** | Yes | Auto-installed on first run |
| **pdftocairo** | Optional | Required only for text-as-geometry import |

---

## Architecture

```
PDFVectorImporter/
|-- Init.py                     # FreeCAD workbench registration
|-- InitGui.py                  # GUI commands and menus
|-- PDFImportHandler.py         # Top-level import orchestration
|-- PDFTools.py                 # Toolbar actions (Scale, Quick Scale, Batch)
|-- src/
|   |-- PDFImporterCore.py      # Central import pipeline
|   |-- PDFImporterCmd.py       # FreeCAD command wrappers
|   |-- PDFScaleTool.py         # Scale by Reference implementation
|   |-- PDFHatchDetector.py     # Hatch region detection engine
|   |-- PDFPrimitives.py        # Primitive geometry builders
|   |-- PDFSvgTextRenderer.py   # SVG/text rendering pipeline
|   |-- PDFPrimitiveExtractor.py
|   |-- PDFRecognition.py       # Pattern and symbol recognition
|   |-- PDFRegions.py           # Spatial region analysis
|   |-- PDFValidation.py        # Import validation checks
|   |-- PDFDimensionParser.py   # Dimension text extraction
|   |-- PDFDocumentProfiler.py  # Document type classification
|   |-- PDFGenericClassifier.py # Generic element classification
|   |-- PDFGenericRecognizer.py # Generic pattern recognition
|   |-- PDFGeometryCleanup.py   # Duplicate/overlap removal
```

---

## QA and Testing

The project includes a dedicated test runner system for automated validation.

**Test Runner:** `run_pdf_vector_importer_tests.py`

The test harness supports multiple target platforms through an adapter pattern:

| Adapter | Target | Description |
|---|---|---|
| **FreeCAD** | FreeCAD 0.21+ | Full integration tests against live FreeCAD |
| **SketchUp** | SketchUp | Cross-platform validation via SketchUp adapter |
| **Blender** | Blender 3.6+ | Headless CLI validation via Blender importer adapter |
| **LibreCAD** | LibreCAD (DXF flow) | PDF-to-DXF validation via LibreCAD adapter |

**Test artifacts:**
- `qa_config_*.json` -- test suite configuration files
- `qa_results_*.json` / `*.csv` -- machine-readable test results
- Test PDFs in the project root for validation against known inputs

Run the full suite:

```bash
python run_pdf_vector_importer_tests.py --workbook path/to/your_workbook.xlsx --config qa_config_local_full.json
```

Run a smoke test:

```bash
python run_pdf_vector_importer_tests.py --workbook path/to/your_workbook.xlsx --config qa_config_local_smoke.json
```

Run platform-specific smoke tests:

```bash
python run_pdf_vector_importer_tests.py --workbook qa_workbook.xlsx --config qa_config.json --platform BL --automation AUTO
python run_pdf_vector_importer_tests.py --workbook qa_workbook.xlsx --config qa_config.json --platform LC --automation AUTO
```

Workbook platform sheet names are:
`SketchUp Tests`, `FreeCAD Tests`, `Blender Tests`, and `LibreCAD Tests`.

Bootstrap a starter workbook on a fresh clone:

```bash
python run_pdf_vector_importer_tests.py --init-workbook qa_workbook.xlsx
```

---

## Usage

1. Open FreeCAD and switch to the **PDF Vector Importer** workbench.
2. Click **Import PDF** or drag a PDF file onto the 3D view.
3. Select an import preset (or use General Vector for most files).
4. Geometry appears as editable Part objects, grouped by color and layer.
5. Use **Scale by Reference** to calibrate to real-world dimensions.

---

## License

MIT License. See [LICENSE](LICENSE) for details.

Copyright (c) 2024-2026 BlueCollar Systems
~~~

### PDFVectorImporter/resources/ImportPDFVector.svg

- Path: `PDFVectorImporter/resources/ImportPDFVector.svg`
- Size: `665.00 B`
- Modified: `2026-03-23 16:42:08`

```xml
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64">
  <rect x="4" y="4" width="56" height="56" rx="6" fill="#1a1a2e" stroke="#e94560" stroke-width="2"/>
  <text x="32" y="28" text-anchor="middle" font-family="monospace" font-size="14" font-weight="bold" fill="#e94560">PDF</text>
  <path d="M16 36 L48 36" stroke="#0f3460" stroke-width="2" stroke-dasharray="4,2"/>
  <path d="M16 42 L44 42 L44 34" stroke="#16c79a" stroke-width="1.5" fill="none"/>
  <circle cx="16" cy="42" r="2" fill="#16c79a"/>
  <circle cx="44" cy="42" r="2" fill="#16c79a"/>
  <path d="M20 50 L28 50 L28 46 L36 54 L28 58 L28 54 L20 54 Z" fill="#e94560" opacity="0.8"/>
</svg>
```

### PDFVectorImporter/run_pdf_vector_importer_tests.py

- Path: `PDFVectorImporter/run_pdf_vector_importer_tests.py`
- Size: `15.77 KB`
- Modified: `2026-04-03 18:31:17`

```python

#!/usr/bin/env python3
"""
PDF Vector Importer QA runner

Purpose:
- Read the v3 QA workbook
- Validate workbook schema
- Select tests by platform / priority / automation
- Run AUTO/HYBRID tests through external adapters when configured
- Emit CSV + JSON results
- Optionally write a copy of the workbook with updated Status/Notes

Honest limitation:
This harness does not magically drive SketchUp or FreeCAD by itself.
Actual host execution must be provided through adapter commands or wrapper scripts.
"""

import argparse
import csv
import json
import shlex
import subprocess
import sys
import time
from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Dict, List, Optional, Tuple

from openpyxl import Workbook, load_workbook

REQUIRED_HEADERS = [
    "Test ID","Requirement Ref","Category","Priority","Platform","Automation",
    "Test Name","Input","Steps","Expected Result","Metrics / Tolerance","Status","Notes"
]

DEFAULT_SHEETS = ["SketchUp Tests", "FreeCAD Tests", "Blender Tests", "LibreCAD Tests"]

PLATFORM_TO_ADAPTER_KEY = {
    "SU": "sketchup",
    "FC": "freecad",
    "BL": "blender",
    "LC": "librecad",
}

DEFAULT_TEST_ROWS = {
    "SketchUp Tests": {
        "test_id": "SU-SMOKE-001",
        "platform": "SU",
        "name": "SketchUp smoke test placeholder",
    },
    "FreeCAD Tests": {
        "test_id": "FC-SMOKE-001",
        "platform": "FC",
        "name": "FreeCAD smoke test placeholder",
    },
    "Blender Tests": {
        "test_id": "BL-SMOKE-001",
        "platform": "BL",
        "name": "Blender smoke test placeholder",
    },
    "LibreCAD Tests": {
        "test_id": "LC-SMOKE-001",
        "platform": "LC",
        "name": "LibreCAD smoke test placeholder",
    },
}

@dataclass
class TestCase:
    test_id: str
    requirement_ref: str
    category: str
    priority: str
    platform: str
    automation: str
    test_name: str
    input_file: str
    steps: str
    expected_result: str
    metrics: str
    status: str = ""
    notes: str = ""
    sheet_name: str = ""
    row_number: int = 0

@dataclass
class TestResult:
    test_id: str
    platform: str
    priority: str
    automation: str
    result: str
    runtime_seconds: float
    notes: str

def normalize(s):
    return "" if s is None else str(s).strip()


def init_workbook(path: str):
    workbook_path = Path(path)
    workbook_path.parent.mkdir(parents=True, exist_ok=True)

    wb = Workbook()
    wb.remove(wb.active)

    for sheet_name in [*DEFAULT_SHEETS, "All Tests"]:
        ws = wb.create_sheet(title=sheet_name)
        ws.append(REQUIRED_HEADERS)

    for sheet_name in DEFAULT_SHEETS:
        row = DEFAULT_TEST_ROWS[sheet_name]
        values = [
            row["test_id"],
            "REQ-SMOKE-001",
            "Smoke",
            "P0",
            row["platform"],
            "AUTO",
            row["name"],
            "path/to/test.pdf",
            "Run importer using default preset",
            "Importer completes without fatal errors",
            "No crash; geometry count >= 1",
            "",
            "",
        ]
        wb[sheet_name].append(values)
        wb["All Tests"].append(values)

    wb.save(workbook_path)

def load_config(path: Optional[str]) -> Dict:
    if not path:
        return {}
    with open(path, "r", encoding="utf-8") as f:
        if path.lower().endswith(".json"):
            return json.load(f)
        raise ValueError("Only JSON config is supported in this starter harness.")

def validate_headers(ws):
    actual = [normalize(ws.cell(1, c).value) for c in range(1, len(REQUIRED_HEADERS)+1)]
    if actual != REQUIRED_HEADERS:
        raise ValueError(f"{ws.title}: header mismatch.\nExpected: {REQUIRED_HEADERS}\nActual:   {actual}")

def iter_tests(workbook_path: str, sheets: List[str]) -> List[TestCase]:
    wb = load_workbook(workbook_path)
    tests: List[TestCase] = []
    missing_sheets: List[str] = []
    for sheet_name in sheets:
        if sheet_name not in wb.sheetnames:
            missing_sheets.append(sheet_name)
            continue
        ws = wb[sheet_name]
        validate_headers(ws)
        for r in range(2, ws.max_row + 1):
            row = [normalize(ws.cell(r, c).value) for c in range(1, len(REQUIRED_HEADERS)+1)]
            if not row[0]:
                continue
            tests.append(TestCase(
                test_id=row[0],
                requirement_ref=row[1],
                category=row[2],
                priority=row[3],
                platform=row[4],
                automation=row[5],
                test_name=row[6],
                input_file=row[7],
                steps=row[8],
                expected_result=row[9],
                metrics=row[10],
                status=row[11],
                notes=row[12],
                sheet_name=sheet_name,
                row_number=r,
            ))
    if missing_sheets:
        print(
            "Warning: workbook missing optional sheet(s): "
            + ", ".join(missing_sheets),
            file=sys.stderr,
        )
    if not tests:
        raise ValueError(
            "No test rows found. Ensure at least one platform test sheet exists "
            f"with required headers: {', '.join(sheets)}"
        )
    return tests

def select_tests(tests: List[TestCase], platform: Optional[str], priority: Optional[str], automation: Optional[str]) -> List[TestCase]:
    out = []
    for t in tests:
        if platform and t.platform != platform:
            continue
        if priority and t.priority != priority:
            continue
        if automation and t.automation != automation:
            continue
        out.append(t)
    return out

def build_command(template: str, test: TestCase, config: Dict) -> str:
    replacements = {
        "test_id": test.test_id,
        "platform": test.platform,
        "priority": test.priority,
        "automation": test.automation,
        "category": test.category,
        "test_name": test.test_name,
        "input": test.input_file,
        "steps": test.steps,
        "expected": test.expected_result,
        "metrics": test.metrics,
        "workspace": str(Path(config.get("workspace", ".")).resolve()),
    }
    return template.format(**replacements)

def parse_adapter_json(stdout_text: str) -> Optional[Dict]:
    s = (stdout_text or "").strip()
    if not s:
        return None
    try:
        obj = json.loads(s)
        return obj if isinstance(obj, dict) else None
    except json.JSONDecodeError:
        pass

    first = s.find("{")
    last = s.rfind("}")
    if first >= 0 and last > first:
        candidate = s[first:last + 1]
        try:
            obj = json.loads(candidate)
            return obj if isinstance(obj, dict) else None
        except json.JSONDecodeError:
            return None
    return None

def classify_adapter_result(returncode: int, payload: Optional[Dict]) -> Tuple[str, str]:
    if returncode != 0:
        return "Fail", f"Adapter process exit code {returncode}."

    if not payload:
        return "Pass", "Adapter returned exit code 0."

    status = normalize(payload.get("status")).upper()
    message = normalize(payload.get("message"))

    if status in ("PASS", "OK", "SUCCESS"):
        return "Pass", message or f"Adapter status={status}."
    if status in ("DRY_RUN", "BLOCKED", "MANUAL"):
        return "Blocked", message or f"Adapter status={status}."
    if status in ("FAIL", "FAILED", "ERROR", "TIMEOUT", "UNKNOWN"):
        return "Fail", message or f"Adapter status={status}."
    if status:
        return "Fail", message or f"Unrecognized adapter status={status}."
    return "Pass", message or "Adapter returned exit code 0."

def run_one(test: TestCase, config: Dict, dry_run: bool) -> TestResult:
    start = time.perf_counter()

    if test.automation == "MANUAL":
        return TestResult(
            test_id=test.test_id,
            platform=test.platform,
            priority=test.priority,
            automation=test.automation,
            result="Blocked",
            runtime_seconds=0.0,
            notes="Manual test. Not executed by harness."
        )

    adapters = config.get("adapters", {})
    platform_key = PLATFORM_TO_ADAPTER_KEY.get(test.platform)
    if not platform_key:
        return TestResult(
            test_id=test.test_id,
            platform=test.platform,
            priority=test.priority,
            automation=test.automation,
            result="Blocked",
            runtime_seconds=round(time.perf_counter() - start, 3),
            notes=f"Unsupported platform code: {test.platform}",
        )
    adapter = adapters.get(platform_key)

    if dry_run:
        note = "Dry run only."
        if adapter and adapter.get("command"):
            note += f" Adapter command template found for {platform_key}."
        else:
            note += f" No adapter configured for {platform_key}."
        return TestResult(
            test_id=test.test_id,
            platform=test.platform,
            priority=test.priority,
            automation=test.automation,
            result="Blocked",
            runtime_seconds=round(time.perf_counter() - start, 3),
            notes=note,
        )

    if not adapter or not adapter.get("command"):
        return TestResult(
            test_id=test.test_id,
            platform=test.platform,
            priority=test.priority,
            automation=test.automation,
            result="Blocked",
            runtime_seconds=round(time.perf_counter() - start, 3),
            notes=f"No adapter configured for {platform_key}.",
        )

    cmd = build_command(adapter["command"], test, config)
    try:
        completed = subprocess.run(
            shlex.split(cmd),
            cwd=config.get("workspace", None),
            capture_output=True,
            text=True,
            timeout=int(adapter.get("timeout_seconds", 900)),
            check=False,
        )
        stdout = (completed.stdout or "").strip()
        stderr = (completed.stderr or "").strip()
        payload = parse_adapter_json(stdout)
        result, note = classify_adapter_result(completed.returncode, payload)

        note_parts = []
        if note:
            note_parts.append(note)
        if payload:
            status = normalize(payload.get("status"))
            if status:
                note_parts.append(f"adapter_status={status}")
        if not payload and stdout:
            note_parts.append(stdout[:500])
        if stderr:
            note_parts.append("STDERR: " + stderr[:500])

        return TestResult(
            test_id=test.test_id,
            platform=test.platform,
            priority=test.priority,
            automation=test.automation,
            result=result,
            runtime_seconds=round(time.perf_counter() - start, 3),
            notes=" | ".join(note_parts) or f"Adapter exit code {completed.returncode}",
        )
    except subprocess.TimeoutExpired:
        return TestResult(
            test_id=test.test_id,
            platform=test.platform,
            priority=test.priority,
            automation=test.automation,
            result="Fail",
            runtime_seconds=round(time.perf_counter() - start, 3),
            notes="Timed out.",
        )
    except (subprocess.SubprocessError, OSError, ValueError, TypeError) as exc:
        return TestResult(
            test_id=test.test_id,
            platform=test.platform,
            priority=test.priority,
            automation=test.automation,
            result="Fail",
            runtime_seconds=round(time.perf_counter() - start, 3),
            notes=f"Runner exception: {exc}",
        )

def write_results_csv(results: List[TestResult], path: str):
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["test_id","platform","priority","automation","result","runtime_seconds","notes"])
        for r in results:
            w.writerow([r.test_id, r.platform, r.priority, r.automation, r.result, r.runtime_seconds, r.notes])

def write_results_json(results: List[TestResult], path: str):
    summary = {
        "total": len(results),
        "passed": sum(1 for r in results if r.result == "Pass"),
        "failed": sum(1 for r in results if r.result == "Fail"),
        "blocked": sum(1 for r in results if r.result == "Blocked"),
        "p0_failed": sum(1 for r in results if r.priority == "P0" and r.result == "Fail"),
        "results": [asdict(r) for r in results],
    }
    with open(path, "w", encoding="utf-8") as f:
        json.dump(summary, f, indent=2)

def update_workbook(source_path: str, output_path: str, results: List[TestResult]):
    result_map = {r.test_id: r for r in results}
    wb = load_workbook(source_path)
    # Update platform sheets AND "All Tests" so the dashboard stays in sync
    update_sheets = list(DEFAULT_SHEETS)
    if "All Tests" in wb.sheetnames and "All Tests" not in update_sheets:
        update_sheets.append("All Tests")
    for sheet_name in update_sheets:
        if sheet_name not in wb.sheetnames:
            continue
        ws = wb[sheet_name]
        for r in range(2, ws.max_row + 1):
            test_id = normalize(ws.cell(r, 1).value)
            if test_id in result_map:
                res = result_map[test_id]
                ws.cell(r, 12).value = res.result
                ws.cell(r, 13).value = res.notes
    wb.save(output_path)

def print_summary(results: List[TestResult]):
    total = len(results)
    passed = sum(1 for r in results if r.result == "Pass")
    failed = sum(1 for r in results if r.result == "Fail")
    blocked = sum(1 for r in results if r.result == "Blocked")
    p0_failed = sum(1 for r in results if r.priority == "P0" and r.result == "Fail")
    print(json.dumps({
        "total": total,
        "passed": passed,
        "failed": failed,
        "blocked": blocked,
        "p0_failed": p0_failed,
    }, indent=2))

def main():
    ap = argparse.ArgumentParser(description="Run PDF Vector Importer QA tests from workbook.")
    ap.add_argument("--workbook", help="Path to QA workbook .xlsx")
    ap.add_argument(
        "--init-workbook",
        help=(
            "Create a starter QA workbook (.xlsx) at this path and exit. "
            "Useful on a clean clone before first test run."
        ),
    )
    ap.add_argument("--config", help="Path to JSON config for adapters")
    ap.add_argument("--platform", choices=["SU", "FC", "BL", "LC"])
    ap.add_argument("--priority", choices=["P0","P1","P2"])
    ap.add_argument("--automation", choices=["AUTO","MANUAL","HYBRID"])
    ap.add_argument("--dry-run", action="store_true", help="Validate selection and adapters without executing commands")
    ap.add_argument("--validate-only", action="store_true", help="Only validate workbook schema and exit")
    ap.add_argument("--results-csv", default="qa_results.csv")
    ap.add_argument("--results-json", default="qa_results.json")
    ap.add_argument("--updated-workbook", help="Write a copy of the workbook with Status/Notes filled from results")
    args = ap.parse_args()

    if args.init_workbook:
        init_workbook(args.init_workbook)
        print(f"Created starter workbook: {Path(args.init_workbook).resolve()}")
        return 0

    if not args.workbook:
        ap.error("--workbook is required unless --init-workbook is used.")

    config = load_config(args.config)
    tests = iter_tests(args.workbook, DEFAULT_SHEETS)

    if args.validate_only:
        print(f"Workbook schema valid. Loaded {len(tests)} tests.")
        return 0

    selected = select_tests(tests, args.platform, args.priority, args.automation)
    if not selected:
        print("No tests selected.", file=sys.stderr)
        return 2

    results = [run_one(t, config, args.dry_run) for t in selected]
    write_results_csv(results, args.results_csv)
    write_results_json(results, args.results_json)
    if args.updated_workbook:
        update_workbook(args.workbook, args.updated_workbook, results)
    print_summary(results)
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
```

### PDFVectorImporter/src/__init__.py

- Path: `PDFVectorImporter/src/__init__.py`
- Size: `24.00 B`
- Modified: `2026-03-23 16:42:08`

```python
# src subpackage



```

### PDFVectorImporter/src/PDFDimensionParser.py

- Path: `PDFVectorImporter/src/PDFDimensionParser.py`
- Size: `3.97 KB`
- Modified: `2026-03-27 17:29:32`

```python
# -*- coding: utf-8 -*-
# PDFDimensionParser.py — Structured dimension parsing
# BlueCollar Systems — BUILT. NOT BOUGHT.
from __future__ import annotations
import re
from PDFPrimitives import ParsedDimension

MM_PER_INCH = 25.4


def parse(text: str) -> ParsedDimension:
    raw = text
    s = _normalize(raw)
    result = ParsedDimension(raw_text=raw, normalized_text=s)

    qty = _extract_qty(s)
    if qty:
        result.quantity = qty

    # Slot
    m = re.search(r'(\d+(?:\.\d+)?(?:\s*/\s*\d+)?)\s*"?\s*[xX×]\s*(\d+(?:\.\d+)?(?:\s+\d+\s*/\s*\d+)?(?:\s*/\s*\d+)?)\s*"?\s*(?:SLOT|SSL|LSL)', s, re.I)
    if m:
        w, l = _parse_token(m.group(1)), _parse_token(m.group(2))
        if w and l:
            result.kind, result.value = "slot", {"width": w*MM_PER_INCH, "length": l*MM_PER_INCH}
            result.units, result.confidence = "mm", 0.95
            return result

    # Diameter
    if re.search(r'Ø|DIA\b|HOLE', s, re.I):
        clean = re.sub(r'Ø|DIA\b|HOLE\b|\(\d+\)|\d+\s*[-xX]\s*', ' ', s, flags=re.I).strip()
        v = _parse_token(clean)
        if v is not None:
            result.kind, result.value = "diameter", v * MM_PER_INCH
            result.units, result.confidence = "mm", 0.95
            return result

    # Feet-inches
    m = re.match(r"(\d+(?:\.\d+)?)\s*['′]\s*[-–]?\s*(\d+(?:\.\d+)?)?\s*(?:(\d+)\s*/\s*(\d+))?\s*[\"″]?\s*$", s)
    if m:
        ft = float(m.group(1))
        inc = float(m.group(2)) if m.group(2) else 0
        if m.group(3) and m.group(4) and int(m.group(4)) != 0:
            inc += float(m.group(3)) / float(m.group(4))
        result.kind, result.value = "linear", (ft * 12 + inc) * MM_PER_INCH
        result.units, result.confidence = "mm", 0.95
        return result

    # Metric explicit
    m = re.search(r'(\d+(?:\.\d+)?)\s*(MM|CM|M)\b', s, re.I)
    if m:
        v = float(m.group(1))
        u = m.group(2).upper()
        if u == "CM": v *= 10
        elif u == "M": v *= 1000
        result.kind, result.value = "linear", v
        result.units, result.confidence = "mm", 0.90
        return result

    # Imperial fraction/decimal with inch mark
    v = _parse_imperial(s)
    if v is not None:
        result.kind, result.value = "linear", v * MM_PER_INCH
        result.units, result.confidence = "mm", 0.85
        return result

    # Scale
    m = re.search(r'(\d+)\s*:\s*(\d+)', s)
    if m:
        result.kind, result.value = "scale", {"ratio": [float(m.group(1)), float(m.group(2))]}
        result.confidence = 0.80
        return result

    result.confidence = 0.1
    result.warnings.append("Could not parse")
    return result


def _normalize(t):
    t = t.replace('\u2018',"'").replace('\u2019',"'").replace('\u201C','"').replace('\u201D','"')
    t = t.replace('\u2013','-').replace('\u2014','-').replace('\u2044','/')
    t = re.sub(r'DIA\.?', 'DIA', t, flags=re.I)
    return re.sub(r'\s+', ' ', t).strip()


def _extract_qty(s):
    m = re.match(r'\s*\((\d+)\)', s) or re.match(r'\s*(\d+)\s*[-xX]\s*(?:Ø|\d)', s)
    return int(m.group(1)) if m else None


def _parse_token(s):
    if not s: return None
    s = s.strip().rstrip('"\'')
    m = re.match(r'(\d+)\s+(\d+)\s*/\s*(\d+)$', s)
    if m and int(m.group(3)) != 0: return float(m.group(1)) + float(m.group(2))/float(m.group(3))
    m = re.match(r'(\d+)\s*/\s*(\d+)$', s)
    if m and int(m.group(2)) != 0: return float(m.group(1))/float(m.group(2))
    m = re.match(r'(\d+(?:\.\d+)?)$', s)
    if m: return float(m.group(1))
    return None


def _parse_imperial(s):
    m = re.match(r'\s*(\d+)\s+(\d+)\s*/\s*(\d+)\s*["\u2033]?', s)
    if m and int(m.group(3)) != 0: return float(m.group(1)) + float(m.group(2))/float(m.group(3))
    m = re.match(r'\s*(\d+)\s*/\s*(\d+)\s*["\u2033]?\s*$', s)
    if m and int(m.group(2)) != 0: return float(m.group(1))/float(m.group(2))
    m = re.match(r'\s*(\d+(?:\.\d+)?)\s*["\u2033]', s)
    if m: return float(m.group(1))
    return None
```

### PDFVectorImporter/src/PDFDocumentProfiler.py

- Path: `PDFVectorImporter/src/PDFDocumentProfiler.py`
- Size: `2.93 KB`
- Modified: `2026-03-23 16:42:08`

```python
# -*- coding: utf-8 -*-
# PDFDocumentProfiler.py — Auto page-type detection
# BlueCollar Systems — BUILT. NOT BOUGHT.
from __future__ import annotations
from PDFPrimitives import PageData, PageProfile


def profile(page_data: PageData) -> PageProfile:
    """Score page type. Returns PageProfile."""
    prims = page_data.primitives
    texts = page_data.text_items

    lines = sum(1 for p in prims if p.type == "line")
    closed = sum(1 for p in prims if p.type == "closed_loop")
    polylines = sum(1 for p in prims if p.type == "polyline")
    total_geom = len(prims)

    dim_texts = sum(1 for t in texts if "dimension_like" in t.generic_tags)
    scale_texts = sum(1 for t in texts if "scale_like" in t.generic_tags)
    tb_texts = sum(1 for t in texts if "titleblock_like" in t.generic_tags)
    callout_texts = sum(1 for t in texts if "callout_like" in t.generic_tags)
    total_text = len(texts)
    has_layers = bool(page_data.layers)

    # Circles
    circles = 0
    from PDFGeometryCleanup import circle_fit
    for p in prims:
        if p.type == "closed_loop" and p.points and len(p.points) >= 8:
            fit = circle_fit(p.points)
            if fit and fit[3] < 0.5:
                circles += 1

    scores = {}

    s = 0.20 * (circles > 3) + 0.15 * (callout_texts > 2) + 0.15 * (dim_texts > 5)
    s += 0.10 * (closed > 10) + 0.10 * (tb_texts > 2) + 0.10 * (scale_texts > 0)
    scores["fabrication"] = min(s, 1.0)

    s = 0.20 * (lines > 50) + 0.15 * (dim_texts > 3) + 0.15 * has_layers
    s += 0.10 * (closed > 5) + 0.10 * (scale_texts > 0) + 0.10 * (tb_texts > 0)
    scores["cad_drawing"] = min(s, 1.0)

    s = 0.20 * (lines > 100) + 0.15 * has_layers + 0.15 * (dim_texts > 10)
    s += 0.10 * (total_text > 30) - 0.15 * (circles > 10)
    scores["architectural"] = min(max(s, 0), 1.0)

    s = 0.30 * (total_geom > 20 and dim_texts == 0) + 0.20 * (polylines > lines)
    s += 0.10 * (total_text < 5) - 0.20 * has_layers - 0.20 * (dim_texts > 2)
    scores["vector_art"] = min(max(s, 0), 1.0)

    s = 0.90 if total_geom == 0 and total_text == 0 else 0.0
    scores["raster_only"] = s

    primary = max(scores, key=scores.get) if scores else "unknown"
    if max(scores.values(), default=0) < 0.25:
        primary = "cad_drawing" if total_geom > 0 else "unknown"

    return PageProfile(
        page_number=page_data.page_number, primary_type=primary,
        scores=scores, has_layers=has_layers, has_text=total_text > 0,
        has_dimensions=dim_texts > 0, circle_count=circles,
        closed_loop_count=closed, line_count=lines, text_count=total_text,
        titleblock_likely=tb_texts > 2
    )


def suggest_mode(profile: PageProfile) -> str:
    t = profile.primary_type
    if t == "fabrication":
        return "technical"
    elif t == "architectural":
        return "architectural"
    elif t in ("vector_art", "raster_only"):
        return "none"
    return "generic"
```

### PDFVectorImporter/src/PDFGenericClassifier.py

- Path: `PDFVectorImporter/src/PDFGenericClassifier.py`
- Size: `3.32 KB`
- Modified: `2026-03-23 16:42:08`

```python
# -*- coding: utf-8 -*-
# PDFGenericClassifier.py — Domain-neutral classification
# BlueCollar Systems — BUILT. NOT BOUGHT.
"""Classifies text and primitives generically. Domain-neutral."""
from __future__ import annotations
import re
from PDFPrimitives import PageData


def classify_text(page_data: PageData):
    """Add generic tags to text items (in place)."""
    for txt in page_data.text_items:
        tags = list(txt.generic_tags)
        tu = txt.normalized
        if re.search(r"\b(NOTE|NOTES|N\.?T\.?S\.?|SEE\s+DWG)\b", tu):
            tags.append("note_indicator")
        if re.search(r"\b(QTY|EA|EACH|PCS)\b", tu):
            tags.append("quantity_indicator")
        if re.search(r"\bREV[.\s]?[A-Z0-9]?\b", tu):
            tags.append("revision_like")
        if re.search(r"\b(DETAIL|SECTION|VIEW|ELEVATION)\s+[A-Z]", tu):
            tags.append("detail_reference")
        txt.generic_tags = tags


def classify_primitives(page_data: PageData):
    """Add generic tags to primitives (in place)."""
    page_area = page_data.width * page_data.height
    for p in page_data.primitives:
        tags = list(p.generic_tags)
        if p.type == "closed_loop" and p.area and p.area > page_area * 0.7:
            if p.points and len(p.points) <= 5:
                tags.append("page_border")
        if p.type == "closed_loop" and p.area and p.area < 50.0:
            if p.points and len(p.points) <= 5:
                tags.append("possible_table_cell")
        if p.dash_pattern:
            tags.append("dashed_line")
        if p.line_width is not None and p.line_width < 0.3:
            tags.append("thin_line")
        p.generic_tags = tags


def detect_title_block(page_data: PageData):
    """Returns bbox (x0,y0,x1,y1) of likely title block or None."""
    tb = [t for t in page_data.text_items if "titleblock_like" in t.generic_tags]
    if len(tb) < 2:
        return None
    xs = [t.insertion[0] for t in tb]
    ys = [t.insertion[1] for t in tb]
    bbox = (min(xs) - 1, min(ys) - 1, max(xs) + 1, max(ys) + 1)
    if bbox[3] < page_data.height * 0.4:
        return bbox
    return None


def detect_tables(page_data: PageData):
    """Find clusters of small rectangles → table regions."""
    cells = [p for p in page_data.primitives
             if "possible_table_cell" in p.generic_tags]
    if len(cells) < 4:
        return []
    tables = []
    used = set()
    for i, c in enumerate(cells):
        if i in used:
            continue
        cluster = [c]
        used.add(i)
        for j, o in enumerate(cells):
            if j in used:
                continue
            if c.bbox and o.bbox and _bboxes_adjacent(c.bbox, o.bbox, 12.0):
                cluster.append(o)
                used.add(j)
        if len(cluster) >= 4:
            all_x = [v for c2 in cluster for v in (c2.bbox[0], c2.bbox[2]) if c2.bbox]
            all_y = [v for c2 in cluster for v in (c2.bbox[1], c2.bbox[3]) if c2.bbox]
            tables.append({"bbox": (min(all_x), min(all_y), max(all_x), max(all_y)),
                           "cell_count": len(cluster)})
    return tables


def _bboxes_adjacent(b1, b2, threshold):
    gap_x = max(b1[0] - b2[2], b2[0] - b1[2], 0)
    gap_y = max(b1[1] - b2[3], b2[1] - b1[3], 0)
    return gap_x < threshold and gap_y < threshold
```

### PDFVectorImporter/src/PDFGenericRecognizer.py

- Path: `PDFVectorImporter/src/PDFGenericRecognizer.py`
- Size: `2.98 KB`
- Modified: `2026-03-23 16:42:08`

```python
# -*- coding: utf-8 -*-
# PDFGenericRecognizer.py — Domain-neutral recognition
# BlueCollar Systems — BUILT. NOT BOUGHT.
from __future__ import annotations
from dataclasses import dataclass, field
from PDFPrimitives import PageData, RecognitionConfig
from PDFGeometryCleanup import circle_fit
import PDFGenericClassifier as gc
import PDFDocumentProfiler as dp
import PDFDimensionParser as dim_parser
import math


@dataclass
class GenericResults:
    circles: list = field(default_factory=list)
    closed_boundaries: list = field(default_factory=list)
    repeated_patterns: list = field(default_factory=list)
    tables: list = field(default_factory=list)
    title_block_bbox: object = None
    dimension_assocs: list = field(default_factory=list)
    page_profile: object = None


def analyze(page_data: PageData, config: RecognitionConfig = None) -> GenericResults:
    if config is None:
        config = RecognitionConfig()
    gc.classify_text(page_data)
    gc.classify_primitives(page_data)
    profile = dp.profile(page_data)

    circles = []
    for p in page_data.primitives:
        if p.type == "closed_loop" and p.closed and p.points and len(p.points) >= 6:
            fit = circle_fit(p.points)
            if fit and fit[3] < config.circle_fit_tol:
                circles.append({"center":(fit[0],fit[1]),"radius":fit[2],"prim_id":p.id,"rms":fit[3]})

    boundaries = [{"prim_id":p.id,"area":p.area,"bbox":p.bbox}
                  for p in page_data.primitives
                  if p.type=="closed_loop" and p.closed and p.area and p.area>=config.closed_loop_min_area]
    boundaries.sort(key=lambda b: -(b["area"] or 0))

    groups = {}
    for p in page_data.primitives:
        if p.type=="closed_loop" and p.area and p.area > 1.0:
            k = f"{round(p.area)}_{len(p.points or [])}"
            groups.setdefault(k,[]).append(p)
    patterns = [{"prim_ids":[q.id for q in g],"count":len(g)} for g in groups.values() if len(g)>=3]

    tables = gc.detect_tables(page_data)
    tb_bbox = gc.detect_title_block(page_data)

    dim_assocs = []
    for txt in page_data.text_items:
        if "dimension_like" not in txt.generic_tags: continue
        pd = dim_parser.parse(txt.text)
        if pd.value is None or pd.confidence < 0.3: continue
        nearest, nd = None, config.dimension_assoc_radius
        for p in page_data.primitives:
            if not p.bbox: continue
            pcx = (p.bbox[0]+p.bbox[2])/2; pcy = (p.bbox[1]+p.bbox[3])/2
            d = math.hypot(txt.insertion[0]-pcx, txt.insertion[1]-pcy)
            if d < nd: nearest, nd = p, d
        dim_assocs.append({"text_id":txt.id,"text":txt.text,"value":pd.value,
                          "kind":pd.kind,"nearest_prim_id":nearest.id if nearest else None})

    return GenericResults(circles=circles, closed_boundaries=boundaries,
        repeated_patterns=patterns, tables=tables, title_block_bbox=tb_bbox,
        dimension_assocs=dim_assocs, page_profile=profile)
```

### PDFVectorImporter/src/PDFGeometryCleanup.py

- Path: `PDFVectorImporter/src/PDFGeometryCleanup.py`
- Size: `2.86 KB`
- Modified: `2026-03-26 05:20:40`

~~~python
# -*- coding: utf-8 -*-
# PDFGeometryCleanup.py — Geometry cleanup on primitives
# BlueCollar Systems — BUILT. NOT BOUGHT.
from __future__ import annotations
import math
from typing import List, Tuple


def circle_fit(points: List[Tuple[float, float]]):
    """Kasa algebraic circle fit → (cx, cy, radius, rms) or None."""
    n = len(points)
    if n < 3:
        return None
    sx = sum(p[0] for p in points)
    sy = sum(p[1] for p in points)
    sx2 = sum(p[0]**2 for p in points)
    sy2 = sum(p[1]**2 for p in points)
    sxy = sum(p[0]*p[1] for p in points)
    sz = sum(p[0]**2 + p[1]**2 for p in points)
    sxz = sum(p[0]*(p[0]**2 + p[1]**2) for p in points)
    syz = sum(p[1]*(p[0]**2 + p[1]**2) for p in points)
    A = [[sx, sy, n], [sx2, sxy, sx], [sxy, sy2, sy]]
    B = [sz, sxz, syz]
    D = _det3(A)
    if abs(D) < 1e-12:
        return None
    A1 = [[B[0],A[0][1],A[0][2]],[B[1],A[1][1],A[1][2]],[B[2],A[2][1],A[2][2]]]
    A2 = [[A[0][0],B[0],A[0][2]],[A[1][0],B[1],A[1][2]],[A[2][0],B[2],A[2][2]]]
    A3 = [[A[0][0],A[0][1],B[0]],[A[1][0],A[1][1],B[1]],[A[2][0],A[2][1],B[2]]]
    a = _det3(A1)/D; b = _det3(A2)/D; c = _det3(A3)/D
    cx, cy = 0.5*a, 0.5*b
    r = math.sqrt(max(0, c + cx*cx + cy*cy))
    rms = math.sqrt(sum((math.hypot(p[0]-cx, p[1]-cy) - r)**2 for p in points) / n)
    return (cx, cy, r, rms)


def _det3(m):
    return (m[0][0]*(m[1][1]*m[2][2]-m[1][2]*m[2][1])
           -m[0][1]*(m[1][0]*m[2][2]-m[1][2]*m[2][0])
           +m[0][2]*(m[1][0]*m[2][1]-m[1][1]*m[2][0]))


def cleanup_primitives(primitives, config=None, cleanup_level=None):
    """Run cleanup on primitive list. Returns stats dict.

    If *cleanup_level* is provided (e.g. "conservative", "balanced", "aggressive"),
    tolerance values are resolved from ``PDFImportConfig.CLEANUP_PRESETS``.
    """
    from PDFPrimitives import RecognitionConfig
    if config is None:
        config = RecognitionConfig()

    # Resolve cleanup_level preset (Phase 2)
    min_seg = config.min_segment_len
    if cleanup_level:
        try:
            from PDFImportConfig import CLEANUP_PRESETS
            preset = CLEANUP_PRESETS.get(cleanup_level.lower(),
                                         CLEANUP_PRESETS.get("balanced", {}))
            if "min_seg" in preset:
                min_seg = preset["min_seg"]
        except ImportError:
            pass

    stats = {"merged": 0, "removed_micro": 0, "removed_dupes": 0}
    # Remove micro segments
    before = len(primitives)
    primitives[:] = [p for p in primitives
                     if not (p.type == "line" and p.points and len(p.points) == 2
                             and math.hypot(p.points[1][0]-p.points[0][0],
                                            p.points[1][1]-p.points[0][1]) < min_seg)]
    stats["removed_micro"] = before - len(primitives)
    return stats
~~~

### PDFVectorImporter/src/PDFHatchDetector.py

- Path: `PDFVectorImporter/src/PDFHatchDetector.py`
- Size: `5.39 KB`
- Modified: `2026-03-23 16:42:08`

~~~python
# -*- coding: utf-8 -*-
# PDFHatchDetector.py — Detect hatching patterns in PyMuPDF drawing groups
# BlueCollar Systems — BUILT. NOT BOUGHT.
"""
Hatching = dense clusters of parallel lines at regular spacing.
Shop drawings use hatching for section cuts; importing it raw
creates thousands of edges that clutter the model.

Modes:
  "import"  — import everything (default)
  "skip"    — remove hatch lines entirely
  "group"   — put hatch lines in a separate hidden group
"""
from __future__ import annotations

import math
from typing import List, Optional, Set, Tuple

# Minimum lines in a cluster to qualify as hatching
MIN_HATCH_LINES = 6
# Angle tolerance for "parallel" (degrees)
ANGLE_TOL_DEG = 3.0
# Spacing regularity tolerance (std_dev / mean ratio)
SPACING_REGULARITY = 0.35
# Length uniformity tolerance (CV)
LENGTH_CV_MAX = 0.50


def _parse_line_segment(item_data) -> Optional[Tuple[float, float, float, float]]:
    """Extract (x0, y0, x1, y1) from a PyMuPDF drawing item."""
    # PyMuPDF 'l' items can have 1 or 2 points
    if len(item_data) >= 2:
        p0, p1 = item_data[0], item_data[1]
        if hasattr(p0, 'x') and hasattr(p1, 'x'):
            return (p0.x, p0.y, p1.x, p1.y)
    return None


def _angle_diff(a: float, b: float) -> float:
    """Angular difference accounting for 0/180 wrap."""
    d = abs(a - b)
    if d > 90.0:
        d = 180.0 - d
    return d


def detect(drawings: List[dict]) -> Set[int]:
    """
    Detect hatch patterns in a list of PyMuPDF drawing groups.

    Parameters
    ----------
    drawings : list of dict
        PyMuPDF page.get_drawings() result.

    Returns
    -------
    set of int
        Indices into ``drawings`` that are hatching lines.
    """
    if not drawings or len(drawings) < MIN_HATCH_LINES:
        return set()

    # Phase 1: Extract line segments with angle + midpoint
    lines: List[dict] = []
    for idx, pg in enumerate(drawings):
        items = pg.get("items", [])
        # Only consider single-segment drawing groups (hatching = one line per group)
        if len(items) < 1:
            continue
        # Must start with moveto + lineto (simple line)
        segs = []
        cur = None
        for item in items:
            kind = item[0]
            data = item[1:]
            if kind == "m":
                pt = data[0] if data else None
                if pt and hasattr(pt, 'x'):
                    cur = (pt.x, pt.y)
            elif kind == "l" and cur is not None:
                parsed = _parse_line_segment(data)
                if parsed:
                    segs.append(parsed)
                else:
                    # Single-point lineto
                    pt = data[0] if data else None
                    if pt and hasattr(pt, 'x'):
                        segs.append((cur[0], cur[1], pt.x, pt.y))
                        cur = (pt.x, pt.y)
            elif kind == "c":
                # Curves are not hatch lines
                break
        if len(segs) == 1:
            x0, y0, x1, y1 = segs[0]
            dx, dy = x1 - x0, y1 - y0
            length = math.hypot(dx, dy)
            if length < 0.5:
                continue
            angle = math.degrees(math.atan2(dy, dx))
            if angle < 0:
                angle += 180.0
            mx, my = (x0 + x1) / 2.0, (y0 + y1) / 2.0
            lines.append({
                "idx": idx, "angle": angle, "len": length,
                "mx": mx, "my": my,
            })

    if len(lines) < MIN_HATCH_LINES:
        return set()

    # Phase 2: Group by angle (parallel lines)
    hatch_indices: Set[int] = set()
    used = [False] * len(lines)

    for i, line in enumerate(lines):
        if used[i]:
            continue
        group = [line]
        used[i] = True

        for j, other in enumerate(lines):
            if j <= i or used[j]:
                continue
            if _angle_diff(line["angle"], other["angle"]) < ANGLE_TOL_DEG:
                group.append(other)
                used[j] = True

        if len(group) < MIN_HATCH_LINES:
            continue

        # Phase 3: Check for regular spacing
        ref_rad = math.radians(group[0]["angle"])
        perp_x = -math.sin(ref_rad)
        perp_y = math.cos(ref_rad)

        projections = sorted(
            [{"proj": l["mx"] * perp_x + l["my"] * perp_y, "line": l}
             for l in group],
            key=lambda p: p["proj"]
        )

        spacings = []
        for k in range(1, len(projections)):
            spacings.append(abs(projections[k]["proj"] - projections[k-1]["proj"]))

        if not spacings:
            continue

        mean_sp = sum(spacings) / len(spacings)
        if mean_sp < 0.3:
            continue

        variance = sum((s - mean_sp) ** 2 for s in spacings) / len(spacings)
        std_dev = math.sqrt(variance)

        if mean_sp > 0 and (std_dev / mean_sp) < SPACING_REGULARITY:
            # Also check length uniformity
            lengths = [l["len"] for l in group]
            mean_len = sum(lengths) / len(lengths)
            len_var = sum((v - mean_len) ** 2 for v in lengths) / len(lengths)
            len_cv = math.sqrt(len_var) / mean_len if mean_len > 0 else 1.0

            if len_cv < LENGTH_CV_MAX:
                for l in group:
                    hatch_indices.add(l["idx"])

    return hatch_indices
~~~

### PDFVectorImporter/src/PDFImportConfig.py

- Path: `PDFVectorImporter/src/PDFImportConfig.py`
- Size: `9.17 KB`
- Modified: `2026-04-03 16:34:06`

~~~python
# -*- coding: utf-8 -*-
# PDFImportConfig.py — Versioned import configuration
# BlueCollar Systems — BUILT. NOT BOUGHT.
"""
Centralised, versioned import configuration for the PDF Vector Importer.

Parallels the SketchUp importer's versioned config pattern so that saved
profiles, presets, and future Phase-2 options all live in one place.
"""
from __future__ import annotations

from dataclasses import dataclass, asdict, fields
from typing import Any, Dict, List, Optional


# ──────────────────────────────────────────────────────────────────────
# Cleanup presets  (tolerance values in mm)
# ──────────────────────────────────────────────────────────────────────
CLEANUP_PRESETS: Dict[str, Dict[str, float]] = {
    "conservative": {
        "merge_tol": 0.5,
        "collinear_tol": 0.25,
        "min_seg": 0.25,
    },
    "balanced": {
        "merge_tol": 0.1,
        "collinear_tol": 0.05,
        "min_seg": 0.05,
    },
    "aggressive": {
        "merge_tol": 0.01,
        "collinear_tol": 0.005,
        "min_seg": 0.01,
    },
}


# ──────────────────────────────────────────────────────────────────────
# ImportConfig dataclass
# ──────────────────────────────────────────────────────────────────────
@dataclass
class ImportConfig:
    """Versioned import configuration for the PDF Vector Importer.

    All fields mirror the options accepted by ``PDFImporterCore.ImportOptions``
    plus Phase-2 additions (arc_mode, cleanup_level, lineweight_mode,
    grouping_mode).
    """

    VERSION: str = "2.0"

    # ── Core geometry options (Phase 1 — existing) ───────────────────
    pages: Optional[List[int]] = None
    scale_to_mm: bool = True
    user_scale: float = 1.0
    flip_y: bool = True
    join_tol: float = 0.1
    min_seg_len: float = 0.0
    curve_step_mm: float = 0.5
    make_faces: bool = True
    import_text: bool = True
    text_mode: str = "labels"               # "labels" | "geometry" | "none"
    strict_text_fidelity: bool = True
    group_by_color: bool = True
    assign_linewidth: bool = True
    map_dashes: bool = True
    verbose: bool = True
    create_top_group: bool = True
    hatch_to_faces: bool = True
    hatch_mode: str = "import"              # "import" | "skip" | "group"
    ignore_images: bool = False
    raster_fallback: bool = True
    raster_dpi: int = 200
    import_mode: str = "auto"               # "auto" | "vectors" | "raster" | "hybrid"
    max_bezier_segments: int = 128

    # ── Arc reconstruction (Phase 1) ─────────────────────────────────
    detect_arcs: bool = True
    arc_fit_tol_mm: float = 0.08
    min_arc_angle_deg: float = 5.0
    arc_sampling_pts: int = 7

    # ── Layering (Phase 1) ───────────────────────────────────────────
    layer_mode: str = "auto"                # "auto" | "ocg" | "color" | "none"

    # ── Object-count management (Phase 1) ────────────────────────────
    compound_batch_size: int = 200
    heavy_page_threshold: int = 3000

    # ── Phase 2 options ──────────────────────────────────────────────
    arc_mode: str = "auto"
    # "auto"     — heuristic per-path (current behaviour)
    # "preserve" — keep arcs found by PyMuPDF as-is
    # "rebuild"  — always run arc-fit on polylines
    # "polyline" — skip arc detection entirely

    cleanup_level: str = "balanced"
    # "conservative" | "balanced" | "aggressive"
    # Maps to tolerance values via CLEANUP_PRESETS.

    lineweight_mode: str = "ignore"
    # "ignore"          — all geometry same lineweight
    # "preserve"        — set ViewObject linewidth from PDF stroke width
    # "group"           — group objects by lineweight
    # "map_to_layers"   — create layers based on lineweight ranges

    grouping_mode: str = "per_page"
    # "single"                — everything in one group
    # "per_page"              — one group per PDF page (current default)
    # "per_layer"             — one group per OCG / colour layer
    # "per_color"             — one group per stroke/fill colour
    # "nested_page_layer"     — page > layer hierarchy
    # "nested_page_lineweight"— page > lineweight hierarchy

    # ─────────────────────────────────────────────────────────────────
    # Serialisation
    # ─────────────────────────────────────────────────────────────────
    def to_dict(self) -> Dict[str, Any]:
        """Return a plain dict compatible with ``PDFImporterCore.ImportOptions``.

        Phase-2 keys are included so that downstream code can opt-in to them
        without breaking older code that simply ignores unknown keys.
        """
        d = asdict(self)
        # VERSION is metadata, not an ImportOptions field
        d.pop("VERSION", None)
        return d

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> "ImportConfig":
        """Create an ``ImportConfig`` from a saved dict (profile loading).

        Unknown keys are silently ignored so that profiles saved by a newer
        version can still be loaded by an older one.
        """
        valid_keys = {f.name for f in fields(cls)}
        filtered = {k: v for k, v in d.items() if k in valid_keys}
        return cls(**filtered)

    # ─────────────────────────────────────────────────────────────────
    # Cleanup tolerance helpers
    # ─────────────────────────────────────────────────────────────────
    def get_cleanup_tolerances(self) -> Dict[str, float]:
        """Return the tolerance dict for the current ``cleanup_level``.

        Falls back to 'balanced' if the level name is unrecognised.
        """
        return dict(CLEANUP_PRESETS.get(self.cleanup_level,
                                        CLEANUP_PRESETS["balanced"]))

    # ─────────────────────────────────────────────────────────────────
    # Named constructors (presets)
    # ─────────────────────────────────────────────────────────────────
    @classmethod
    def fast(cls) -> "ImportConfig":
        """Fast Preview preset — speed over fidelity."""
        return cls(
            curve_step_mm=2.0,
            join_tol=0.5,
            detect_arcs=False,
            map_dashes=False,
            make_faces=False,
            import_text=False,
            text_mode="none",
            strict_text_fidelity=False,
            hatch_mode="skip",
            import_mode="auto",
            cleanup_level="conservative",
            arc_mode="polyline",
            lineweight_mode="ignore",
            grouping_mode="single",
        )

    @classmethod
    def full(cls) -> "ImportConfig":
        """Full / Shop Drawing preset — balanced quality and performance."""
        return cls(
            curve_step_mm=0.5,
            join_tol=0.1,
            detect_arcs=True,
            map_dashes=True,
            make_faces=True,
            import_text=True,
            text_mode="geometry",
            strict_text_fidelity=True,
            hatch_mode="group",
            import_mode="auto",
            cleanup_level="balanced",
            arc_mode="auto",
            lineweight_mode="preserve",
            grouping_mode="per_page",
        )

    @classmethod
    def max_fidelity(cls) -> "ImportConfig":
        """Max Fidelity preset — highest accuracy, slower."""
        return cls(
            curve_step_mm=0.2,
            join_tol=0.05,
            detect_arcs=True,
            map_dashes=True,
            make_faces=True,
            import_text=True,
            text_mode="geometry",
            strict_text_fidelity=True,
            hatch_mode="import",
            import_mode="auto",
            cleanup_level="aggressive",
            arc_mode="rebuild",
            lineweight_mode="preserve",
            grouping_mode="nested_page_layer",
        )
~~~

### PDFVectorImporter/src/PDFImporterCmd.py

- Path: `PDFVectorImporter/src/PDFImporterCmd.py`
- Size: `26.44 KB`
- Modified: `2026-04-03 19:06:01`

```python
# -*- coding: utf-8 -*-
# PDFImporterCmd.py — GUI command to import PDF with options dialog
# BlueCollar Systems — BUILT. NOT BOUGHT.
from __future__ import annotations

import os
import sys

_lib_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "lib")
if _lib_dir not in sys.path:
    sys.path.insert(0, _lib_dir)

try:
    import fitz
except ImportError:
    fitz = None

try:
    from PySide6 import QtWidgets
except ImportError:
    from PySide2 import QtWidgets

import FreeCAD


# ──────────────────────────────────────────────────────────────────────
# Options dialog
# ──────────────────────────────────────────────────────────────────────
class ImportPDFDialog(QtWidgets.QDialog):
    """Preset-based options dialog for the PDF vector importer."""

    # cleanup_level maps to PDFImportConfig.CLEANUP_PRESETS tolerance values.
    # It must stay consistent with join_tol: fast/loose presets → conservative,
    # standard presets → balanced, high-fidelity → aggressive.
    PRESETS = {
        "Fast Preview":     dict(curve_step=2.0, join_tol=0.5,  detect_arcs=False, map_dashes=False, make_faces=False, text="No text",  hatch_mode="skip",   import_mode="auto",   cleanup_level="conservative", strict_text_fidelity=False, arc_mode="polyline",  lineweight_mode="ignore",   grouping_mode="single"),
        "General Vector":   dict(curve_step=1.0, join_tol=0.2,  detect_arcs=False, map_dashes=False, make_faces=True,  text="Geometry", hatch_mode="import", import_mode="auto",   cleanup_level="balanced",     strict_text_fidelity=True,  arc_mode="auto",     lineweight_mode="ignore",   grouping_mode="per_page"),
        "Technical Drawing":dict(curve_step=0.5, join_tol=0.1,  detect_arcs=True,  map_dashes=True,  make_faces=True,  text="Geometry", hatch_mode="group",  import_mode="auto",   cleanup_level="balanced",     strict_text_fidelity=True,  arc_mode="auto",     lineweight_mode="preserve", grouping_mode="per_page"),
        "Shop Drawing":     dict(curve_step=0.5, join_tol=0.1,  detect_arcs=True,  map_dashes=True,  make_faces=True,  text="Geometry", hatch_mode="group",  import_mode="auto",   cleanup_level="balanced",     strict_text_fidelity=True,  arc_mode="auto",     lineweight_mode="preserve", grouping_mode="per_page"),
        "Raster + Vectors": dict(curve_step=0.5, join_tol=0.1,  detect_arcs=True,  map_dashes=True,  make_faces=True,  text="Geometry", hatch_mode="skip",   import_mode="hybrid", cleanup_level="balanced",     strict_text_fidelity=True,  arc_mode="auto",     lineweight_mode="ignore",   grouping_mode="per_page", raster_dpi=200),
        "Raster Only":      dict(curve_step=1.0, join_tol=0.5,  detect_arcs=False, map_dashes=False, make_faces=False, text="No text",  hatch_mode="skip",   import_mode="raster", cleanup_level="conservative", strict_text_fidelity=False, arc_mode="polyline",  lineweight_mode="ignore",   grouping_mode="single",   raster_dpi=300),
        "Max Fidelity":     dict(curve_step=0.2, join_tol=0.05, detect_arcs=True,  map_dashes=True,  make_faces=True,  text="Geometry", hatch_mode="import", import_mode="auto",   cleanup_level="aggressive",   strict_text_fidelity=True,  arc_mode="rebuild",  lineweight_mode="preserve", grouping_mode="nested_page_layer"),
    }

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Import PDF — BlueCollar Systems")
        self.setMinimumWidth(420)
        self._page_count = None

        # ── File row ──
        self.file_edit = QtWidgets.QLineEdit()
        self.file_edit.setPlaceholderText("Choose a PDF file…")
        browse_btn = QtWidgets.QPushButton("Browse…")
        browse_btn.clicked.connect(self._browse)
        file_row = QtWidgets.QHBoxLayout()
        file_row.addWidget(self.file_edit, 1)
        file_row.addWidget(browse_btn, 0)

        # ── Preset ──
        self.preset_combo = QtWidgets.QComboBox()
        self.preset_combo.addItems(list(self.PRESETS.keys()))
        self.preset_combo.setCurrentText("Shop Drawing")
        self.preset_combo.currentTextChanged.connect(self._on_preset_changed)

        # ── Pages ──
        self.page_edit = QtWidgets.QLineEdit("All")
        self.page_edit.setToolTip("1, 1-5, 1,3,7, or All")

        # ── Scale ──
        self.scale_spin = QtWidgets.QDoubleSpinBox()
        self.scale_spin.setDecimals(6)
        self.scale_spin.setRange(1e-6, 100000.0)
        self.scale_spin.setValue(25.4 / 72.0)
        self.scale_spin.setToolTip("Default converts PDF points to mm (25.4/72)")

        # ── Import Text ──
        self.text_combo = QtWidgets.QComboBox()
        self.text_combo.addItems(["Labels", "Geometry", "No text"])
        self.text_combo.setCurrentText("Labels")

        # ── Strict Text Fidelity ──
        self.strict_text_chk = QtWidgets.QCheckBox("Strict glyph fidelity")
        self.strict_text_chk.setChecked(True)
        self.strict_text_chk.setToolTip(
            "When enabled, text import avoids line reconstruction and uses only\n"
            "glyph-accurate placement paths (best visual match to PDF).\n"
            "May create more text objects."
        )

        # ── Hatch Mode ──
        self.hatch_combo = QtWidgets.QComboBox()
        self.hatch_combo.addItems(["Import", "Group (hidden)", "Skip"])
        self.hatch_combo.setCurrentText("Group (hidden)")
        self.hatch_combo.setToolTip(
            "Hatching lines (section cuts):\n"
            "Import = bring in as normal geometry\n"
            "Group = separate hidden group (recommended)\n"
            "Skip = discard entirely")

        # ── Import Mode ──
        self.mode_combo = QtWidgets.QComboBox()
        self.mode_combo.addItems(["Auto", "Vectors Only", "Raster + Vectors", "Raster Only"])
        self.mode_combo.setCurrentText("Auto")
        self.mode_combo.setToolTip(
            "Auto = detect page content and choose best mode\n"
            "Vectors Only = import vector geometry (CAD drawings)\n"
            "Raster + Vectors = render page image + overlay vectors\n"
            "  (best for maps, site plans, PDFs with photos)\n"
            "Raster Only = render page as image, skip vectors")
        self.mode_combo.currentTextChanged.connect(self._on_mode_changed)

        # ── Raster DPI ──
        self.dpi_combo = QtWidgets.QComboBox()
        self.dpi_combo.addItems(["72", "150", "200", "300", "600"])
        self.dpi_combo.setCurrentText("200")
        self.dpi_combo.setToolTip(
            "Resolution for raster rendering.\n"
            "150 = fast preview\n"
            "200 = good balance (default)\n"
            "300 = high quality (larger files)\n"
            "600 = maximum detail (slow, very large)")
        self.dpi_combo.setEnabled(False)  # Enabled when raster mode selected

        # ── Advanced options (Phase 2) ──
        self.arc_mode_combo = QtWidgets.QComboBox()
        self.arc_mode_combo.addItems(["Auto", "Preserve", "Rebuild", "Polyline"])
        self.arc_mode_combo.setCurrentText("Auto")
        self.arc_mode_combo.setToolTip(
            "How to handle arcs found in the PDF:\n"
            "Auto = detect and reconstruct where beneficial\n"
            "Preserve = keep original PDF arc commands\n"
            "Rebuild = force arc fitting on polyline segments\n"
            "Polyline = convert all arcs to polyline segments")

        self.cleanup_combo = QtWidgets.QComboBox()
        self.cleanup_combo.addItems(["Conservative", "Balanced", "Aggressive"])
        self.cleanup_combo.setCurrentText("Balanced")
        self.cleanup_combo.setToolTip(
            "Geometry cleanup aggressiveness:\n"
            "Conservative = minimal cleanup, preserve all detail\n"
            "Balanced = merge near-coincident points, remove micro-segments\n"
            "Aggressive = heavy simplification, tightest tolerances")

        self.lineweight_combo = QtWidgets.QComboBox()
        self.lineweight_combo.addItems(["Ignore", "Preserve", "Group", "Map to Layers"])
        self.lineweight_combo.setCurrentText("Ignore")
        self.lineweight_combo.setToolTip(
            "How to handle line weights from the PDF:\n"
            "Ignore = all lines get default weight\n"
            "Preserve = apply original PDF line widths\n"
            "Group = group objects by line weight\n"
            "Map to Layers = create layers based on line weight")

        self.grouping_combo = QtWidgets.QComboBox()
        self.grouping_combo.addItems([
            "Single", "Per Page", "Per Layer", "Per Color",
            "Nested Page>Layer", "Nested Page>Lineweight"])
        self.grouping_combo.setCurrentText("Per Page")
        self.grouping_combo.setToolTip(
            "How imported objects are grouped in the model tree:\n"
            "Single = everything in one group\n"
            "Per Page = one group per PDF page\n"
            "Per Layer = one group per PDF layer (OCG)\n"
            "Per Color = one group per stroke/fill color\n"
            "Nested Page>Layer = pages containing layer sub-groups\n"
            "Nested Page>Lineweight = pages containing lineweight sub-groups")

        # Apply preset defaults (sets text combo to match preset)
        self._on_preset_changed("Shop Drawing")

        # ── Restore last-used settings ──
        self._restore_settings()

        # ── Layout ──
        form = QtWidgets.QFormLayout()
        form.addRow("PDF file:", file_row)
        form.addRow("Preset:", self.preset_combo)
        form.addRow("Pages:", self.page_edit)
        form.addRow("Scale (mm/pt):", self.scale_spin)
        form.addRow("Import Mode:", self.mode_combo)
        form.addRow("Raster DPI:", self.dpi_combo)
        form.addRow("Import Text:", self.text_combo)
        form.addRow("Text Fidelity:", self.strict_text_chk)
        form.addRow("Hatching:", self.hatch_combo)

        # ── Collapsible Advanced section ──
        adv_group = QtWidgets.QGroupBox("Advanced")
        adv_group.setCheckable(True)
        adv_group.setChecked(False)
        adv_form = QtWidgets.QFormLayout()
        adv_form.addRow("Arc Mode:", self.arc_mode_combo)
        adv_form.addRow("Cleanup Level:", self.cleanup_combo)
        adv_form.addRow("Lineweight:", self.lineweight_combo)
        adv_form.addRow("Grouping:", self.grouping_combo)
        adv_group.setLayout(adv_form)

        # Hide/show advanced widgets when group is toggled
        adv_group.toggled.connect(lambda on: [
            w.setVisible(on) for w in (
                self.arc_mode_combo, self.cleanup_combo,
                self.lineweight_combo, self.grouping_combo)])
        # Start collapsed — hide the inner widgets
        for w in (self.arc_mode_combo, self.cleanup_combo,
                  self.lineweight_combo, self.grouping_combo):
            w.setVisible(False)

        btns = QtWidgets.QDialogButtonBox(
            QtWidgets.QDialogButtonBox.Ok | QtWidgets.QDialogButtonBox.Cancel)
        btns.accepted.connect(self._validate_and_accept)
        btns.rejected.connect(self.reject)

        layout = QtWidgets.QVBoxLayout(self)
        layout.addLayout(form)
        layout.addWidget(adv_group)
        layout.addWidget(btns)

    def _browse(self):
        # Remember last folder across sessions
        try:
            grp = FreeCAD.ParamGet("User parameter:BaseApp/Preferences/Mod/PDFVectorImporter")
            last_dir = grp.GetString("LastImportDir", "")
        except (AttributeError, RuntimeError, ValueError):
            last_dir = ""

        path, _ = QtWidgets.QFileDialog.getOpenFileName(
            self, "Select PDF File", last_dir, "PDF Files (*.pdf)")
        if path:
            # Save this folder for next time
            try:
                grp = FreeCAD.ParamGet("User parameter:BaseApp/Preferences/Mod/PDFVectorImporter")
                grp.SetString("LastImportDir", os.path.dirname(path))
            except (AttributeError, RuntimeError, ValueError):
                pass
            self.file_edit.setText(path)
            if fitz:
                try:
                    with fitz.open(path) as doc:
                        self._page_count = doc.page_count
                    self.page_edit.setPlaceholderText(
                        f"1-{self._page_count}  (PDF has {self._page_count} pages)")
                except (RuntimeError, OSError, ValueError):
                    pass

    def _on_mode_changed(self, mode_text):
        """Enable/disable DPI selector based on import mode."""
        needs_raster = mode_text in ("Raster + Vectors", "Raster Only", "Auto")
        self.dpi_combo.setEnabled(needs_raster)

    _PARAM_PATH = "User parameter:BaseApp/Preferences/Mod/PDFVectorImporter"

    def _restore_settings(self):
        """Load last-used dialog settings from FreeCAD preferences."""
        try:
            grp = FreeCAD.ParamGet(self._PARAM_PATH)
            preset = grp.GetString("LastPreset", "")
            if preset and preset in self.PRESETS:
                self.preset_combo.setCurrentText(preset)
            text_mode = grp.GetString("LastTextMode", "")
            if text_mode:
                self.text_combo.setCurrentText(text_mode)
            hatch_mode = grp.GetString("LastHatchMode", "")
            if hatch_mode:
                self.hatch_combo.setCurrentText(hatch_mode)
            import_mode = grp.GetString("LastImportMode", "")
            if import_mode:
                self.mode_combo.setCurrentText(import_mode)
            dpi = grp.GetString("LastDpi", "")
            if dpi:
                self.dpi_combo.setCurrentText(dpi)
            strict_text = grp.GetBool("LastStrictTextFidelity", self.strict_text_chk.isChecked())
            self.strict_text_chk.setChecked(bool(strict_text))
            scale = grp.GetFloat("LastScale", 0.0)
            if scale > 0:
                self.scale_spin.setValue(scale)
            # Phase-2 advanced options
            arc_mode = grp.GetString("LastArcMode", "")
            if arc_mode:
                self.arc_mode_combo.setCurrentText(arc_mode)
            cleanup = grp.GetString("LastCleanupLevel", "")
            if cleanup:
                self.cleanup_combo.setCurrentText(cleanup)
            lw = grp.GetString("LastLineweightMode", "")
            if lw:
                self.lineweight_combo.setCurrentText(lw)
            grouping = grp.GetString("LastGroupingMode", "")
            if grouping:
                self.grouping_combo.setCurrentText(grouping)
        except (AttributeError, RuntimeError, ValueError):
            pass  # First run or corrupted prefs — use defaults

    def _save_settings(self):
        """Persist current dialog settings to FreeCAD preferences."""
        try:
            grp = FreeCAD.ParamGet(self._PARAM_PATH)
            grp.SetString("LastPreset", self.preset_combo.currentText())
            grp.SetString("LastTextMode", self.text_combo.currentText())
            grp.SetString("LastHatchMode", self.hatch_combo.currentText())
            grp.SetString("LastImportMode", self.mode_combo.currentText())
            grp.SetString("LastDpi", self.dpi_combo.currentText())
            grp.SetBool("LastStrictTextFidelity", self.strict_text_chk.isChecked())
            grp.SetFloat("LastScale", self.scale_spin.value())
            # Phase-2 advanced options
            grp.SetString("LastArcMode", self.arc_mode_combo.currentText())
            grp.SetString("LastCleanupLevel", self.cleanup_combo.currentText())
            grp.SetString("LastLineweightMode", self.lineweight_combo.currentText())
            grp.SetString("LastGroupingMode", self.grouping_combo.currentText())
        except (AttributeError, RuntimeError, ValueError):
            pass

    # Mapping tables for Phase-2 advanced dropdowns (internal value -> UI label)
    _ARC_MODE_MAP = {"auto": "Auto", "preserve": "Preserve", "rebuild": "Rebuild", "polyline": "Polyline"}
    _CLEANUP_MAP = {"conservative": "Conservative", "balanced": "Balanced", "aggressive": "Aggressive"}
    _LINEWEIGHT_MAP = {"ignore": "Ignore", "preserve": "Preserve", "group": "Group", "map_to_layers": "Map to Layers"}
    _GROUPING_MAP = {
        "single": "Single", "per_page": "Per Page", "per_layer": "Per Layer",
        "per_color": "Per Color", "nested_page_layer": "Nested Page>Layer",
        "nested_page_lineweight": "Nested Page>Lineweight",
    }

    def _on_preset_changed(self, preset_name):
        preset = self.PRESETS.get(preset_name)
        if preset:
            if "text" in preset:
                self.text_combo.setCurrentText(preset["text"])
            if "hatch_mode" in preset:
                hatch_map = {"import": "Import", "group": "Group (hidden)", "skip": "Skip"}
                self.hatch_combo.setCurrentText(
                    hatch_map.get(preset["hatch_mode"], "Import"))
            if "import_mode" in preset:
                mode_map = {"auto": "Auto", "vectors": "Vectors Only",
                            "hybrid": "Raster + Vectors", "raster": "Raster Only"}
                self.mode_combo.setCurrentText(
                    mode_map.get(preset["import_mode"], "Auto"))
            if "raster_dpi" in preset:
                self.dpi_combo.setCurrentText(str(preset["raster_dpi"]))
            if "strict_text_fidelity" in preset:
                self.strict_text_chk.setChecked(bool(preset["strict_text_fidelity"]))
            # Phase-2 advanced options
            if "arc_mode" in preset:
                self.arc_mode_combo.setCurrentText(
                    self._ARC_MODE_MAP.get(preset["arc_mode"], "Auto"))
            if "cleanup_level" in preset:
                self.cleanup_combo.setCurrentText(
                    self._CLEANUP_MAP.get(preset["cleanup_level"], "Balanced"))
            if "lineweight_mode" in preset:
                self.lineweight_combo.setCurrentText(
                    self._LINEWEIGHT_MAP.get(preset["lineweight_mode"], "Ignore"))
            if "grouping_mode" in preset:
                self.grouping_combo.setCurrentText(
                    self._GROUPING_MAP.get(preset["grouping_mode"], "Per Page"))

    def _validate_and_accept(self):
        path = self.file_edit.text().strip()
        if not path or not os.path.isfile(path):
            QtWidgets.QMessageBox.warning(
                self, "Missing File", "Please select a valid PDF file.")
            return
        try:
            self._parse_pages()
        except ValueError as e:
            QtWidgets.QMessageBox.warning(
                self, "Invalid Page Selection", str(e))
            return
        self._save_settings()
        self.accept()

    # ── Parse page specification ──
    def _parse_pages(self) -> list:
        text = self.page_edit.text().strip().lower()
        if not text or text in ("all", "*"):
            if self._page_count:
                return list(range(1, self._page_count + 1))
            return [1]

        pages = set()
        bad_parts = []
        for raw_part in text.split(','):
            part = raw_part.strip()
            if not part:
                continue
            if '-' in part:
                a_s, b_s = part.split('-', 1)
                if not (a_s.strip().isdigit() and b_s.strip().isdigit()):
                    bad_parts.append(part)
                    continue
                a = int(a_s)
                b = int(b_s)
                if a <= 0 or b <= 0:
                    bad_parts.append(part)
                    continue
                start, end = sorted((a, b))
                for p in range(start, end + 1):
                    pages.add(p)
            elif part.isdigit():
                p = int(part)
                if p <= 0:
                    bad_parts.append(part)
                    continue
                pages.add(p)
            else:
                bad_parts.append(part)

        if bad_parts:
            raise ValueError(
                "Invalid page entry: {}\nUse examples like 1, 1-5, 1,3,7, or all.".format(
                    ", ".join(bad_parts)
                )
            )
        if not pages:
            raise ValueError("No valid pages selected.")
        if self._page_count:
            over = [p for p in sorted(pages) if p > self._page_count]
            if over:
                raise ValueError(
                    f"Page(s) out of range for this PDF: {', '.join(map(str, over))}. "
                    f"This file has {self._page_count} page(s)."
                )
        return sorted(pages)

    # ── Build ImportOptions from dialog state ──
    def build_options(self):
        import PDFVectorImporter.src.PDFImporterCore as core
        preset_name = self.preset_combo.currentText()
        preset = self.PRESETS.get(preset_name, self.PRESETS["Shop Drawing"])
        text_ui = self.text_combo.currentText()

        # Map UI text mode to ImportOptions fields
        if text_ui == "Geometry":
            import_text, text_mode = True, "geometry"
        elif text_ui == "No text":
            import_text, text_mode = False, "none"
        else:
            import_text, text_mode = True, "labels"

        # Map UI hatch mode
        hatch_ui = self.hatch_combo.currentText()
        if "Skip" in hatch_ui:
            hatch_mode = "skip"
        elif "Group" in hatch_ui:
            hatch_mode = "group"
        else:
            hatch_mode = "import"

        # Map UI import mode to option value
        mode_ui = self.mode_combo.currentText()
        mode_map = {"Auto": "auto", "Vectors Only": "vectors",
                    "Raster + Vectors": "hybrid", "Raster Only": "raster"}
        import_mode = mode_map.get(mode_ui, "auto")

        raster_dpi = int(self.dpi_combo.currentText())

        # Reverse-map UI labels to internal values for Phase-2 options
        _arc_rev = {v: k for k, v in self._ARC_MODE_MAP.items()}
        _cleanup_rev = {v: k for k, v in self._CLEANUP_MAP.items()}
        _lw_rev = {v: k for k, v in self._LINEWEIGHT_MAP.items()}
        _grp_rev = {v: k for k, v in self._GROUPING_MAP.items()}

        opts = core.ImportOptions(
            pages=self._parse_pages(),
            scale_to_mm=False,
            user_scale=float(self.scale_spin.value()),
            flip_y=True,
            join_tol=preset["join_tol"],
            curve_step_mm=preset["curve_step"],
            make_faces=preset["make_faces"],
            import_text=import_text,
            text_mode=text_mode,
            strict_text_fidelity=self.strict_text_chk.isChecked(),
            hatch_mode=hatch_mode,
            group_by_color=True,
            assign_linewidth=True,
            map_dashes=preset["map_dashes"],
            detect_arcs=preset["detect_arcs"],
            ignore_images=(import_mode == "raster"),
            raster_fallback=True,
            raster_dpi=raster_dpi,
            import_mode=import_mode,
            create_top_group=True,
            verbose=True,
        )

        # Phase-2 advanced options — attached to opts for downstream consumers.
        # ImportOptions dataclass does not define these yet, so we set them
        # as extra attributes.  Existing code ignores unknown attrs safely.
        opts.arc_mode = _arc_rev.get(self.arc_mode_combo.currentText(), "auto")
        opts.cleanup_level = _cleanup_rev.get(self.cleanup_combo.currentText(), "balanced")
        opts.lineweight_mode = _lw_rev.get(self.lineweight_combo.currentText(), "ignore")
        opts.grouping_mode = _grp_rev.get(self.grouping_combo.currentText(), "per_page")

        return opts


# ──────────────────────────────────────────────────────────────────────
# FreeCAD Command
# ──────────────────────────────────────────────────────────────────────
class ImportPDFVectorCommand:
    """FreeCAD GUI command: Import PDF Vector…"""

    def GetResources(self):
        icon_path = os.path.join(
            os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
            "resources", "ImportPDFVector.svg")
        return {
            "Pixmap": icon_path if os.path.exists(icon_path) else "",
            "MenuText": "Import PDF Vector…",
            "ToolTip": "Import vector geometry, text, and images from a PDF file.",
        }

    def IsActive(self):
        return True

    def Activated(self):
        # Re-check for fitz each time (may have been installed mid-session)
        try:
            import fitz  # noqa: F811, F401
        except ImportError:
            QtWidgets.QMessageBox.warning(
                None, "PyMuPDF Not Found",
                "PyMuPDF is not installed yet.\n\n"
                "Switch to the PDF Vector Importer workbench — it will\n"
                "offer to install it automatically.")
            return

        dlg = ImportPDFDialog()
        exec_fn = getattr(dlg, "exec", None) or getattr(dlg, "exec_", None)
        if exec_fn is None or exec_fn() != QtWidgets.QDialog.Accepted:
            return

        pdf_path = dlg.file_edit.text().strip()
        opts = dlg.build_options()

        import PDFVectorImporter.src.PDFImporterCore as core
        try:
            core.import_pdf(pdf_path, opts)
            FreeCAD.Console.PrintMessage("PDF import complete.\n")

            # Auto-switch to orthographic top view
            try:
                import FreeCADGui
                view = FreeCADGui.ActiveDocument.ActiveView
                if view:
                    view.setCameraType("Orthographic")
                    view.viewTop()
                    view.fitAll()
            except (AttributeError, RuntimeError):
                pass

        except (RuntimeError, ValueError, TypeError, OSError, AttributeError, ImportError) as e:
            import traceback
            FreeCAD.Console.PrintError(f"Import failed: {e}\n{traceback.format_exc()}")
            QtWidgets.QMessageBox.critical(
                None, "Import Failed", str(e))



```

### PDFVectorImporter/src/PDFImporterCore.py

- Path: `PDFVectorImporter/src/PDFImporterCore.py`
- Size: `129.18 KB`
- Modified: `2026-04-03 17:43:33`

~~~python
# -*- coding: utf-8 -*-
# PDFImporterCore.py — FreeCAD PDF Vector Import Engine
# BlueCollar Systems — BUILT. NOT BOUGHT.
# License: MIT (PyMuPDF itself is AGPL-3 / commercial)
"""
Converts PDF vector paths, text, and embedded images into native FreeCAD
Part geometry (wires, faces, arcs) with full color/layer grouping.

Converts PDF drawings into editable FreeCAD geometry with text and image support.
"""
from __future__ import annotations

import math
import os
import re
import sys
import time
import traceback
from dataclasses import dataclass
from typing import Dict, List, Optional, Tuple

# Ensure bundled PyMuPDF is importable
_lib_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "lib")
if _lib_dir not in sys.path:
    sys.path.insert(0, _lib_dir)

import fitz  # PyMuPDF

# FreeCAD modules — lazy import for IDE friendliness outside FreeCAD
try:
    import FreeCAD
    import Draft
    import Part
    from FreeCAD import Placement, Rotation, Vector
except ImportError:
    FreeCAD = Draft = Part = None
    Vector = Placement = Rotation = None

try:
    import ImageGui  # noqa: F401
    IMAGE_WB = True
except ImportError:
    IMAGE_WB = False

# ──────────────────────────────────────────────────────────────────────
# Constants
# ──────────────────────────────────────────────────────────────────────
MM_PER_PT = 25.4 / 72.0       # 1 PDF point = 0.352778 mm
ZERO_TOL  = 1e-9              # near-zero length tolerance
CLOSE_TOL = 1e-6              # endpoint-coincidence tolerance

# Auto-mode heuristics for pages that contain mostly vectorized glyph fills.
# These PDFs often look "vector" to PyMuPDF but are effectively not useful as
# editable CAD geometry (thousands of tiny filled path groups).
AUTO_GLYPH_DRAWING_THRESHOLD = 1500
AUTO_GLYPH_FILL_RATIO = 0.75          # was 0.85 — loosened to catch more flood types
AUTO_GLYPH_TINY_RECT_RATIO = 0.45
AUTO_GLYPH_TEXT_BLOCK_THRESHOLD = 50  # was 200 — text-sparse maps still trigger
AUTO_GLYPH_WORD_THRESHOLD = 400       # was 800 — lower text requirement
AUTO_GLYPH_STROKE_SPARSE_RATIO = 0.05
AUTO_GLYPH_TINY_RECT_AREA_PT2 = 36.0

# Fill-art flood detection — catches map PDFs, illustrated layouts, decorative
# art where most drawing groups are filled shapes rather than engineering strokes.
# Unlike glyph-flood (text-as-vectors), these pages have organic filled areas
# (tree canopies, planting beds, terrain fills) with almost no stroked lines.
AUTO_FILL_DRAWING_THRESHOLD = 400  # minimum groups to trigger fill-art check
AUTO_FILL_HEAVY_RATIO = 0.60       # fill-only ratio — 60%+ fills signals art/map
AUTO_FILL_STROKE_MAX = 0.22        # stroke ratio ceiling — if too many strokes
#                                    it's a hybrid worth processing as vectors
#
# PyMuPDF 1.27+ can coalesce many path ops into fewer drawing groups. That means
# some decorative art pages now present as ~10-50 groups (not hundreds), but are
# still pure fill geometry with almost no useful CAD strokes.
AUTO_FILL_PURE_RATIO = 0.95
AUTO_FILL_PURE_STROKE_MAX = 0.02
AUTO_FILL_PURE_MIN_GROUPS = 12
AUTO_FILL_PURE_MIN_ITEMS = 24
AUTO_FILL_PURE_LARGE_RECT_RATIO = 0.03


# ──────────────────────────────────────────────────────────────────────
# Logging
# ──────────────────────────────────────────────────────────────────────
def _msg(s: str):
    if FreeCAD:
        FreeCAD.Console.PrintMessage(s + "\n")

def _warn(s: str):
    if FreeCAD:
        FreeCAD.Console.PrintWarning(s + "\n")

def _err(s: str):
    if FreeCAD:
        FreeCAD.Console.PrintError(s + "\n")


# ──────────────────────────────────────────────────────────────────────
# Vector helpers  (FreeCAD.Vector.multiply is IN-PLACE — never use it
# for math expressions.  Use the * operator which returns a NEW vector.)
# ──────────────────────────────────────────────────────────────────────
def _v(x: float, y: float, z: float = 0.0) -> "Vector":
    return Vector(x, y, z)


def _len2d(a: "Vector", b: "Vector") -> float:
    return math.hypot(a.x - b.x, a.y - b.y)


def _pts_closed(pts: List["Vector"], tol: float = CLOSE_TOL) -> bool:
    return len(pts) > 2 and _len2d(pts[0], pts[-1]) <= tol


# ──────────────────────────────────────────────────────────────────────
# PyMuPDF 1.24+ / 1.26 compatibility  (objects may be Point, tuple, etc.)
# ──────────────────────────────────────────────────────────────────────
def _is_point(obj) -> bool:
    return hasattr(obj, "x") and hasattr(obj, "y")


def _is_rect(obj) -> bool:
    return all(hasattr(obj, a) for a in ("x0", "y0", "x1", "y1"))


def _xy(obj) -> Tuple[float, float]:
    """Extract (x, y) from a fitz.Point, tuple, or list."""
    if _is_point(obj):
        return float(obj.x), float(obj.y)
    if isinstance(obj, (tuple, list)) and len(obj) >= 2:
        return float(obj[0]), float(obj[1])
    return float(obj), 0.0


def _rect_coords(obj) -> Tuple[float, float, float, float]:
    """Return (x0, y0, w, h) from a fitz.Rect or 4-element sequence."""
    if _is_rect(obj):
        x0, y0 = float(obj.x0), float(obj.y0)
        return x0, y0, float(obj.x1) - x0, float(obj.y1) - y0
    if isinstance(obj, (tuple, list)) and len(obj) >= 4:
        x0, y0, x1, y1 = float(obj[0]), float(obj[1]), float(obj[2]), float(obj[3])
        return x0, y0, x1 - x0, y1 - y0
    return 0.0, 0.0, 0.0, 0.0


def _rect_area(obj) -> Optional[float]:
    """Return absolute rectangle area in PDF point units² or None."""
    try:
        _x, _y, w, h = _rect_coords(obj)
        return abs(float(w) * float(h))
    except (TypeError, ValueError):
        return None


def _vector_group_stats(drawings: List[dict], page_area: Optional[float] = None) -> Dict[str, float]:
    """Profile coarse vector composition for auto-mode heuristics."""
    total = len(drawings)
    if total <= 0:
        return {
            "fill_only_ratio": 0.0,
            "stroke_ratio": 0.0,
            "tiny_rect_ratio": 0.0,
            "fill_only_count": 0.0,
            "stroke_count": 0.0,
            "tiny_rect_count": 0.0,
            "total_item_count": 0.0,
            "avg_items_per_group": 0.0,
            "max_rect_ratio": 0.0,
        }

    fill_only = 0
    stroke_count = 0
    tiny_rect_count = 0
    total_item_count = 0
    max_rect_ratio = 0.0

    for grp in drawings:
        fill = grp.get("fill")
        stroke = grp.get("color") or grp.get("stroke")
        if fill is not None and stroke is None:
            fill_only += 1
        if stroke is not None:
            stroke_count += 1
        total_item_count += len(grp.get("items", []) or [])
        area = _rect_area(grp.get("rect"))
        if area is not None and area <= AUTO_GLYPH_TINY_RECT_AREA_PT2:
            tiny_rect_count += 1
        if area is not None and page_area and page_area > 0:
            ratio = area / page_area
            if ratio > max_rect_ratio:
                max_rect_ratio = ratio

    denom = float(total)
    return {
        "fill_only_ratio": fill_only / denom,
        "stroke_ratio": stroke_count / denom,
        "tiny_rect_ratio": tiny_rect_count / denom,
        "fill_only_count": float(fill_only),
        "stroke_count": float(stroke_count),
        "tiny_rect_count": float(tiny_rect_count),
        "total_item_count": float(total_item_count),
        "avg_items_per_group": (float(total_item_count) / denom),
        "max_rect_ratio": max_rect_ratio,
    }


def _looks_like_vector_glyph_flood(n_drawings: int,
                                   n_text_blocks: int,
                                   n_words: int,
                                   stats: Dict[str, float]) -> bool:
    """Heuristic for pages where text/vector art overwhelms usable CAD lines.

    Targets PDFs where text characters are stored as filled vector paths
    (each glyph = one filled path group), producing thousands of objects
    that are geometrically useless for CAD but look like line work to PyMuPDF.
    """
    if n_drawings < AUTO_GLYPH_DRAWING_THRESHOLD:
        return False
    text_dense = (n_text_blocks >= AUTO_GLYPH_TEXT_BLOCK_THRESHOLD
                  or n_words >= AUTO_GLYPH_WORD_THRESHOLD)
    if not text_dense:
        return False
    return (stats.get("fill_only_ratio", 0.0) >= AUTO_GLYPH_FILL_RATIO
            and stats.get("tiny_rect_ratio", 0.0) >= AUTO_GLYPH_TINY_RECT_RATIO)


def _looks_like_fill_art_flood(n_drawings: int,
                               stats: Dict[str, float]) -> bool:
    """Detect map / illustrated-art PDFs dominated by filled decorative shapes.

    These pages differ from glyph floods: they are not text-as-vectors but
    rather artistic fills — garden beds, terrain contours, tree canopies,
    landscape features — where each shape is a complex filled path.  Importing
    as vectors produces an unusable tangle of faces; raster is far better.

    Signature: high fill-only ratio, very low stroke ratio, many groups.
    This check is intentionally independent of text density so it fires even
    on map pages with few text labels (e.g. a garden plan with only plant names).
    """
    fill_ratio = stats.get("fill_only_ratio", 0.0)
    stroke_ratio = stats.get("stroke_ratio", 0.0)
    total_items = stats.get("total_item_count", 0.0)
    max_rect_ratio = stats.get("max_rect_ratio", 0.0)

    # New fast path for coalesced pure-fill PDFs (common with newer PyMuPDF):
    # if the page is almost entirely fill-only and has virtually no stroke
    # signals, treat it as decorative/map art even at low drawing-group counts.
    pure_fill = (fill_ratio >= AUTO_FILL_PURE_RATIO
                 and stroke_ratio <= AUTO_FILL_PURE_STROKE_MAX)
    if pure_fill and n_drawings >= AUTO_FILL_PURE_MIN_GROUPS:
        if total_items >= AUTO_FILL_PURE_MIN_ITEMS:
            return True
        if max_rect_ratio >= AUTO_FILL_PURE_LARGE_RECT_RATIO:
            return True

    # Legacy high-count fallback (kept for older parser behavior).
    if n_drawings < AUTO_FILL_DRAWING_THRESHOLD:
        return False
    return fill_ratio >= AUTO_FILL_HEAVY_RATIO and stroke_ratio <= AUTO_FILL_STROKE_MAX


def _as_float(v) -> Optional[float]:
    """Coerce a value to float (handles fitz.Point, scalar, tuple)."""
    try:
        if hasattr(v, "x") and not isinstance(v, (int, float)):
            return float(v.x)
        return float(v)
    except (TypeError, ValueError, AttributeError):
        if isinstance(v, (tuple, list)) and v:
            try:
                return float(v[0])
            except (TypeError, ValueError):
                pass
    return None


def _as_float_list(seq) -> List[float]:
    out = []
    for x in (seq or []):
        fx = _as_float(x)
        if fx is not None:
            out.append(fx)
    return out


def _parse_dashes(val) -> List[float]:
    """Parse a dash pattern from PyMuPDF which may be:
    - A string like '[ 6 6 ] 0'  (bracket-delimited, with trailing phase)
    - A list of floats [6.0, 6.0]
    - None or empty
    Returns a list of float dash lengths (no phase value)."""
    if val is None:
        return []
    if isinstance(val, str):
        # Extract numbers from between brackets: "[ 6 6 ] 0" → [6.0, 6.0]
        bracket_match = re.search(r'\[([^\]]*)\]', val)
        if bracket_match:
            inner = bracket_match.group(1).strip()
            if not inner:
                return []  # empty brackets = solid
            nums = []
            for part in inner.split():
                try:
                    nums.append(float(part))
                except ValueError:
                    pass
            return nums
        # No brackets — try splitting as space-separated numbers
        nums = []
        for part in val.split():
            try:
                nums.append(float(part))
            except ValueError:
                pass
        return nums
    # Handle nested tuple/list: ([dash_array], phase) from newer PyMuPDF
    if isinstance(val, (tuple, list)) and len(val) >= 1:
        if isinstance(val[0], (tuple, list)):
            return _as_float_list(val[0])
    # Already a flat list/tuple
    return _as_float_list(val)


# ──────────────────────────────────────────────────────────────────────
# Color normalization
# ──────────────────────────────────────────────────────────────────────
def _clamp01(v) -> float:
    try:
        return max(0.0, min(1.0, float(v)))
    except (TypeError, ValueError):
        return 0.0


def _norm_color(col) -> Tuple[float, float, float]:
    """Normalize any PyMuPDF color representation to (r, g, b) in [0..1]."""
    if col is None:
        return (0.0, 0.0, 0.0)
    try:
        if isinstance(col, (int, float)):
            g = _clamp01(col)
            return (g, g, g)
        vals = []
        for c in col:
            f = _as_float(c)
            vals.append(_clamp01(f) if f is not None else 0.0)
        if len(vals) == 0:
            return (0.0, 0.0, 0.0)
        if len(vals) == 1:
            return (vals[0], vals[0], vals[0])
        if len(vals) >= 4:
            # PyMuPDF can return CMYK tuples for some PDFs. Convert CMYK -> RGB
            # instead of incorrectly truncating to the first 3 channels.
            c, m, y, k = vals[0], vals[1], vals[2], vals[3]
            r = (1.0 - c) * (1.0 - k)
            g = (1.0 - m) * (1.0 - k)
            b = (1.0 - y) * (1.0 - k)
            return (_clamp01(r), _clamp01(g), _clamp01(b))
        while len(vals) < 3:
            vals.append(vals[-1])
        return (vals[0], vals[1], vals[2])
    except (TypeError, ValueError, AttributeError):
        return (0.0, 0.0, 0.0)


# ──────────────────────────────────────────────────────────────────────
# Options
# ──────────────────────────────────────────────────────────────────────
@dataclass
class ImportOptions:
    pages: Optional[List[int]] = None       # 1-based page numbers; None → [1]
    scale_to_mm: bool = True                # convert PDF points → mm
    user_scale: float = 1.0                 # additional multiplier
    flip_y: bool = True                     # PDF Y-down → CAD Y-up
    join_tol: float = 0.1                   # mm — snap endpoints
    min_seg_len: float = 0.0                # skip degenerate micro-edges
    curve_step_mm: float = 0.5              # Bezier linearization chord
    make_faces: bool = True                 # close filled paths → Part::Face
    import_text: bool = True
    text_mode: str = "labels"             # "labels" | "geometry" | "none"
    # When enabled, disables text reconstruction and uses glyph-accurate
    # placement paths only (pdftocairo geometry or exact per-span labels).
    strict_text_fidelity: bool = True
    group_by_color: bool = True
    assign_linewidth: bool = True
    map_dashes: bool = True
    verbose: bool = True
    create_top_group: bool = True
    hatch_to_faces: bool = True
    hatch_mode: str = "import"              # "import" | "skip" | "group"
    ignore_images: bool = False
    raster_fallback: bool = True             # render page as image if no vectors
    raster_dpi: int = 200                    # DPI for raster fallback rendering
    raster_dpi_user_set: bool = False        # True when user explicitly chose the DPI
    # Import mode: "auto" | "vectors" | "raster" | "hybrid"
    #   auto    — detect scanned/image-heavy and vector-glyph-flood pages
    #   vectors — vector geometry only (original behavior)
    #   raster  — render full page as image, skip vectors
    #   hybrid  — raster background + vector geometry on top
    import_mode: str = "auto"
    max_bezier_segments: int = 128
    # Arc reconstruction
    detect_arcs: bool = True
    arc_fit_tol_mm: float = 0.08
    min_arc_angle_deg: float = 5.0
    arc_sampling_pts: int = 7
    # Layering
    layer_mode: str = "auto"                # "auto" | "ocg" | "color" | "none"
    # Object-count management (prevents Windows GDI handle exhaustion)
    compound_batch_size: int = 200          # batch N shapes into one Part::Compound
    #   0 = no batching (original behavior, risky on large PDFs)
    # Heavy-page safe mode — auto-engaged when drawing groups exceed threshold
    heavy_page_threshold: int = 3000        # above this: larger batches, throttled
    #   progress updates, deferred arc fitting on polyline runs
    #   0 = never auto-engage heavy mode


# ──────────────────────────────────────────────────────────────────────
# Coordinate transform
# ──────────────────────────────────────────────────────────────────────
def _to_fc(xy: Tuple[float, float], page_h: float,
           opts: ImportOptions, scale: float) -> "Vector":
    """Transform a PDF coordinate pair into a FreeCAD Vector."""
    x, y = xy
    if opts.flip_y:
        y = page_h - y
    return _v(x * scale, y * scale, 0)


# ──────────────────────────────────────────────────────────────────────
# Cubic Bezier evaluation  (SAFE — never mutates vectors)
# ──────────────────────────────────────────────────────────────────────
def _bezier_point(p0: "Vector", p1: "Vector", p2: "Vector",
                  p3: "Vector", t: float) -> "Vector":
    """De Casteljau evaluation of cubic Bézier at parameter t ∈ [0,1].

    FreeCAD.Vector.multiply() is **in-place** and returns None, so we
    must use the ``*`` and ``+`` operators which return new Vectors.
    """
    u = 1.0 - t
    # B(t) = (1-t)^3·P0 + 3(1-t)^2·t·P1 + 3(1-t)·t^2·P2 + t^3·P3
    return (p0 * (u * u * u)
            + p1 * (3.0 * u * u * t)
            + p2 * (3.0 * u * t * t)
            + p3 * (t * t * t))


# ──────────────────────────────────────────────────────────────────────
# Circle / arc fitting  (Kåsa algebraic fit)
# ──────────────────────────────────────────────────────────────────────
def _circle_fit(points: List["Vector"]) -> Tuple["Vector", float, float]:
    """Return (center, radius, rms_error) via Kåsa algebraic circle fit."""
    n = len(points)
    if n < 3:
        raise ValueError("Need ≥ 3 points")
    sx  = sum(p.x for p in points)
    sy  = sum(p.y for p in points)
    sx2 = sum(p.x * p.x for p in points)
    sy2 = sum(p.y * p.y for p in points)
    sxy = sum(p.x * p.y for p in points)
    sz  = sum(p.x * p.x + p.y * p.y for p in points)
    sxz = sum(p.x * (p.x * p.x + p.y * p.y) for p in points)
    syz = sum(p.y * (p.x * p.x + p.y * p.y) for p in points)

    A = [[sx, sy, n], [sx2, sxy, sx], [sxy, sy2, sy]]
    B = [sz, sxz, syz]

    def det3(m):
        return (m[0][0] * (m[1][1] * m[2][2] - m[1][2] * m[2][1])
              - m[0][1] * (m[1][0] * m[2][2] - m[1][2] * m[2][0])
              + m[0][2] * (m[1][0] * m[2][1] - m[1][1] * m[2][0]))

    D = det3(A)
    if abs(D) < 1e-12:
        raise ValueError("Singular matrix in circle fit")

    A1 = [[B[0], A[0][1], A[0][2]], [B[1], A[1][1], A[1][2]], [B[2], A[2][1], A[2][2]]]
    A2 = [[A[0][0], B[0], A[0][2]], [A[1][0], B[1], A[1][2]], [A[2][0], B[2], A[2][2]]]
    A3 = [[A[0][0], A[0][1], B[0]], [A[1][0], A[1][1], B[1]], [A[2][0], A[2][1], B[2]]]

    a = det3(A1) / D
    b = det3(A2) / D
    c = det3(A3) / D
    cx, cy = 0.5 * a, 0.5 * b
    r = math.sqrt(max(0, c + cx * cx + cy * cy))
    center = _v(cx, cy, 0)
    rms = math.sqrt(sum((_len2d(p, center) - r) ** 2 for p in points) / n)
    return center, r, rms


def _arc_from_cubic(p0, p1, p2, p3, opts: ImportOptions):
    """If cubic ≈ circular arc, return (start, mid, end) for Part.Arc."""
    if not opts.detect_arcs:
        return None
    m = max(3, opts.arc_sampling_pts)
    if m % 2 == 0:
        m += 1
    tvals = [i / (m - 1) for i in range(m)]
    pts = [_bezier_point(p0, p1, p2, p3, t) for t in tvals]
    try:
        center, r, rms = _circle_fit(pts)
    except ValueError:
        return None
    if rms > opts.arc_fit_tol_mm:
        return None

    # Guard against fits that only look good on average.
    max_err = max(abs(_len2d(p, center) - r) for p in pts)
    if max_err > max(opts.arc_fit_tol_mm * 2.5, r * 0.01):
        return None

    v0 = p0 - center
    v3 = p3 - center
    if v0.Length < ZERO_TOL or v3.Length < ZERO_TOL:
        return None
    a0 = math.atan2(v0.y, v0.x)
    a3 = math.atan2(v3.y, v3.x)
    d = a3 - a0
    while d <= -math.pi:
        d += 2 * math.pi
    while d > math.pi:
        d -= 2 * math.pi
    if abs(d) * 180.0 / math.pi < opts.min_arc_angle_deg:
        return None

    # Midpoint must align with the selected minor sweep.
    pmid = pts[len(pts) // 2]
    vm = pmid - center
    if vm.Length < ZERO_TOL:
        return None
    am = math.atan2(vm.y, vm.x)
    expected_mid = _normalize_angle(a0 + (d * 0.5))
    mid_diff = abs(_normalize_angle(am - expected_mid))
    if mid_diff > (math.pi / 3.0):
        return None

    # Tangents at cubic endpoints should be close to perpendicular to the
    # radius vector for a true circular arc.
    t0 = p1 - p0
    t3 = p3 - p2
    for tan, rad in ((t0, v0), (t3, v3)):
        if tan.Length <= ZERO_TOL or rad.Length <= ZERO_TOL:
            continue
        cosang = abs((tan.x * rad.x + tan.y * rad.y) / (tan.Length * rad.Length))
        if cosang > 0.35:
            return None

    return (p0, pmid, p3)


# ──────────────────────────────────────────────────────────────────────
# Edge / wire / face builders
# ──────────────────────────────────────────────────────────────────────
def _edge_line(p1: "Vector", p2: "Vector"):
    """Part.Edge from two points; returns None if degenerate."""
    try:
        if _len2d(p1, p2) <= ZERO_TOL:
            return None
        return Part.LineSegment(p1, p2).toShape()
    except (RuntimeError, ValueError, TypeError):
        return None


def _edge_arc(p1: "Vector", pmid: "Vector", p2: "Vector"):
    try:
        return Part.Arc(p1, pmid, p2).toShape()
    except (RuntimeError, ValueError, TypeError):
        return None


def _normalize_angle(angle: float) -> float:
    """Normalize angle to (-pi, pi]."""
    while angle <= -math.pi:
        angle += 2.0 * math.pi
    while angle > math.pi:
        angle -= 2.0 * math.pi
    return angle


def _polyline_run_is_smooth(verts: List["Vector"], max_turn_deg: float = 60.0) -> bool:
    """Return True when a run behaves like a smooth arc candidate.

    Rejects runs with hard corners or turn-direction reversals that commonly
    produce false giant arcs when circle-fitting mixed corner+line geometry.
    """
    if len(verts) < 5:
        return False

    max_turn = math.radians(max_turn_deg)
    prev_sign = 0
    valid_turns = 0

    for i in range(1, len(verts) - 1):
        a = verts[i] - verts[i - 1]
        b = verts[i + 1] - verts[i]
        ax, ay = a.x, a.y
        bx, by = b.x, b.y

        la = math.hypot(ax, ay)
        lb = math.hypot(bx, by)
        if la <= ZERO_TOL or lb <= ZERO_TOL:
            continue

        cross = ax * by - ay * bx
        dot = ax * bx + ay * by
        turn = abs(math.atan2(cross, dot))
        if turn > max_turn:
            return False

        sign = 1 if cross > 1e-9 else (-1 if cross < -1e-9 else 0)
        if sign != 0:
            if prev_sign != 0 and sign != prev_sign:
                return False
            prev_sign = sign

        valid_turns += 1

    return valid_turns >= 2


def _make_shape_obj(edges: List, closed: bool, make_face: bool, fc_doc=None):
    """Build Part::Feature from edges, optionally closing + making a Face."""
    if not edges:
        return None
    doc = fc_doc or FreeCAD.ActiveDocument
    try:
        wire = Part.Wire(edges)
        if closed and not wire.isClosed():
            # Use wire vertexes (topologically safe) instead of edge vertexes
            if wire.Vertexes:
                p0 = wire.Vertexes[0].Point
                pN = wire.Vertexes[-1].Point
                if _len2d(_v(p0.x, p0.y), _v(pN.x, pN.y)) > ZERO_TOL:
                    closer = Part.LineSegment(pN, p0).toShape()
                    wire = Part.Wire(edges + [closer])
        if make_face and wire.isClosed():
            try:
                face = Part.Face(wire)
                obj = doc.addObject("Part::Feature", "Face")
                obj.Shape = face
                return obj
            except (RuntimeError, ValueError, TypeError):
                pass
        obj = doc.addObject("Part::Feature", "Wire")
        obj.Shape = wire
        return obj
    except (RuntimeError, ValueError, TypeError):
        return None


def _apply_style(obj, stroke_rgb, width, dashes, opts: ImportOptions):
    """Set line color, width, and dash style on a Part::Feature ViewObject."""
    try:
        vo = obj.ViewObject
        if stroke_rgb is not None:
            vo.LineColor = stroke_rgb
        if opts.assign_linewidth and width is not None:
            try:
                # PDF line widths in points are tiny; scale and enforce a visible minimum
                lw = float(width) * (0.7 if opts.scale_to_mm else 1.0)
                # Minimum 2.0 so lines are always visible regardless of background
                vo.LineWidth = max(2.0, lw)
            except (TypeError, ValueError, AttributeError):
                vo.LineWidth = 2.0
        else:
            # Even with no width info, make lines visible
            try:
                vo.LineWidth = 2.0
            except (AttributeError, RuntimeError):
                pass
        if opts.map_dashes and dashes and len(dashes) >= 2:
            if all(d > 0 for d in dashes):
                if len(dashes) == 2:
                    # [dash, gap] → simple dashed
                    vo.DrawStyle = "Dashed"
                elif len(dashes) >= 4:
                    # [dash, gap, dot, gap] → center line / dashdot
                    vo.DrawStyle = "Dashdot"
                elif len(dashes) == 3:
                    vo.DrawStyle = "Dashdot"
    except (AttributeError, RuntimeError, TypeError, ValueError):
        pass


def _make_group(parent, label: str, fc_doc=None):
    doc = fc_doc or FreeCAD.ActiveDocument
    grp = doc.addObject("App::DocumentObjectGroup", label)
    parent.addObject(grp)
    return grp


_temp_files: List[str] = []

def _register_temp_cleanup(path: str):
    """Track a temp file for later cleanup."""
    _temp_files.append(path)

def cleanup_temp_files():
    """Remove temp raster images from previous imports."""
    removed = 0
    for p in list(_temp_files):
        try:
            if os.path.isfile(p):
                os.remove(p)
                removed += 1
            _temp_files.remove(p)
        except OSError:
            pass
    if removed:
        _msg(f"Cleaned up {removed} temporary raster image(s)")

def _ensure_doc():
    doc = FreeCAD.ActiveDocument
    if doc is None:
        doc = FreeCAD.newDocument("PDF_Import")
    # Note: temp file cleanup is deferred to explicit calls, not run
    # automatically here, to avoid deleting images still referenced by
    # Image::ImagePlane objects from the previous import.
    return doc


# ──────────────────────────────────────────────────────────────────────
# Path item parsing helpers  (handles all PyMuPDF item formats)
# ──────────────────────────────────────────────────────────────────────
def _parse_point(data) -> Tuple[float, float]:
    """Parse a moveto / lineto data payload → (x, y)."""
    if len(data) == 1:
        return _xy(data[0])
    if len(data) >= 2:
        if _is_point(data[0]):
            return _xy(data[0])
        return float(data[0]), float(data[1])
    return 0.0, 0.0


def _parse_cubic(data) -> Tuple[Tuple[float, float], ...]:
    """Parse curveto data → ((x1,y1), (x2,y2), (x3,y3))."""
    if len(data) == 3 and all(_is_point(d) for d in data):
        return _xy(data[0]), _xy(data[1]), _xy(data[2])
    if len(data) >= 6:
        return ((float(data[0]), float(data[1])),
                (float(data[2]), float(data[3])),
                (float(data[4]), float(data[5])))
    # 3 points as tuples
    if len(data) == 3:
        return _xy(data[0]), _xy(data[1]), _xy(data[2])
    raise ValueError(f"Cannot parse cubic data: {data}")


def _parse_quad(data) -> Tuple[Tuple[float, float], Tuple[float, float]]:
    """Parse quadratic Bezier ('v') → ((cx,cy), (x,y))."""
    if len(data) == 2 and all(_is_point(d) for d in data):
        return _xy(data[0]), _xy(data[1])
    if len(data) >= 4:
        return ((float(data[0]), float(data[1])),
                (float(data[2]), float(data[3])))
    if len(data) == 2:
        return _xy(data[0]), _xy(data[1])
    raise ValueError(f"Cannot parse quad data: {data}")


def _parse_rect(data) -> Tuple[float, float, float, float]:
    """Parse 're' data → (x, y, w, h). Handles Rect, (Rect, int), or 4 floats."""
    # PyMuPDF may give (Rect,), (Rect, winding_number), or (x, y, w, h)
    if len(data) >= 1 and _is_rect(data[0]):
        return _rect_coords(data[0])
    if len(data) == 1:
        return _rect_coords(data[0])
    if len(data) >= 4:
        try:
            return float(data[0]), float(data[1]), float(data[2]), float(data[3])
        except (TypeError, ValueError, IndexError):
            pass
    if len(data) >= 2 and _is_point(data[0]) and _is_point(data[1]):
        x0, y0 = _xy(data[0])
        x1, y1 = _xy(data[1])
        return x0, y0, x1 - x0, y1 - y0
    return 0.0, 0.0, 0.0, 0.0


def _polyline_edges_to_arcs(edges: List, opts: ImportOptions) -> List:
    """Detect runs of line segments that form circular arcs and replace
    them with true Part::Arc edges.

    Many PDF generators (Tekla, SDS2, etc.) pre-linearize circles and arcs
    into 16-32 segment polylines. This function reconstructs true arcs.
    """
    if len(edges) < 3:
        return edges

    # Extract vertices from consecutive line edges
    verts = []
    for e in edges:
        try:
            v = e.Vertexes
            if not verts:
                verts.append(v[0].Point)
            verts.append(v[-1].Point)
        except (AttributeError, TypeError, IndexError):
            verts.append(None)  # non-line edge (already an arc, etc.)

    if len(verts) < 4:
        return edges

    # Scan for runs of vertices that fit a circle
    result_edges = []
    i = 0
    n = len(edges)

    while i < n:
        # Try to find the longest arc starting at position i
        best_arc_end = -1
        best_arc = None

        # Need at least 4 edges (5 vertices) for a reliable arc fit.
        # 3-edge runs are often orthogonal corners that can falsely circle-fit.
        for j in range(i + 4, min(i + 65, n + 1)):  # max 64 segments
            run_verts = verts[i:j + 1]
            # Skip if any vertex is None (non-line edge in the run)
            if any(v is None for v in run_verts):
                break
            if len(run_verts) < 5:
                continue
            if not _polyline_run_is_smooth(run_verts):
                continue

            try:
                pts_2d = [_v(v.x, v.y, 0) for v in run_verts]
                center, r, rms = _circle_fit(pts_2d)

                # Accept if fit is good relative to the radius
                tol = max(opts.arc_fit_tol_mm, r * 0.005)  # 0.5% of radius
                if rms < tol and r > 0.1:
                    # Check arc sweep is meaningful and midpoint-consistent.
                    # We only accept the minor sweep between endpoints; if the
                    # sampled midpoint is far from that sweep's centerline,
                    # this is likely a false arc candidate.
                    v0 = pts_2d[0] - center
                    vN = pts_2d[-1] - center
                    vm = pts_2d[len(pts_2d) // 2] - center
                    if v0.Length > ZERO_TOL and vN.Length > ZERO_TOL and vm.Length > ZERO_TOL:
                        a0 = math.atan2(v0.y, v0.x)
                        aN = math.atan2(vN.y, vN.x)
                        am = math.atan2(vm.y, vm.x)

                        sweep = _normalize_angle(aN - a0)
                        if abs(sweep) * 180.0 / math.pi < opts.min_arc_angle_deg:
                            continue

                        test_mid = _normalize_angle(a0 + sweep * 0.5)
                        mid_diff = abs(_normalize_angle(am - test_mid))
                        if mid_diff > (math.pi / 2.0):
                            continue

                        best_arc_end = j
                        mid_idx = len(pts_2d) // 2
                        best_arc = (run_verts[0], run_verts[mid_idx], run_verts[-1])
            except ValueError:
                pass

        if best_arc is not None and best_arc_end > i + 3:
            # Replace edges[i:best_arc_end] with a single arc
            p_start, p_mid, p_end = best_arc
            arc_edge = _edge_arc(p_start, p_mid, p_end)
            if arc_edge is not None:
                result_edges.append(arc_edge)
                i = best_arc_end
                continue

        # No arc found starting here — keep the original edge
        result_edges.append(edges[i])
        i += 1

    return result_edges


# ──────────────────────────────────────────────────────────────────────
# Text fraction reconstruction
# ──────────────────────────────────────────────────────────────────────
# Common denominators in structural/architectural drawings
# Engineering drawing inch fractions are overwhelmingly base-2 denominators.
# Keeping this strict avoids false positives like "206" -> "2/06" for part IDs.
_VALID_DENOMS = {2, 4, 8, 16, 32, 64}


def _try_split_fraction(text: str) -> Optional[Tuple[str, str]]:
    """Try to split a combined numerator+denominator string like '18' → ('1','8').
    Returns (numerator, denominator) or None if no valid fraction found."""
    if not text or len(text) < 2:
        return None
    # Try each split point: "916" → ("9","16"), ("91","6")
    best = None
    for i in range(1, len(text)):
        num_s, den_s = text[:i], text[i:]
        try:
            num, den = int(num_s), int(den_s)
        except ValueError:
            continue
        if den in _VALID_DENOMS and 0 < num < den:
            # Prefer the split that gives a standard fraction
            if best is None:
                best = (num_s, den_s)
            # Prefer smaller denominators (more common)
            elif int(best[1]) > den:
                best = (num_s, den_s)
    return best


def _is_fraction_slash(span: dict) -> bool:
    """Check if a span is a fraction bar '/' drawn between stacked numbers."""
    text = span.get("text", "").strip()
    return text == "/"


def _is_superscript(span: dict) -> bool:
    """Check if span has the superscript flag (bit 0 of flags)."""
    return bool(span.get("flags", 0) & 1)


def _is_smaller_font(span: dict, ref_size: float) -> bool:
    """Check if span is noticeably smaller than the reference size."""
    size = float(span.get("size", 0))
    return size > 0 and size < ref_size * 0.95


def _reconstruct_line_text(spans: list) -> str:
    """Reconstruct a line of text, converting stacked fractions back to inline.

    PyMuPDF extracts PDF fractions (stacked numerator/denominator) as separate
    spans. CRITICALLY, the "/" fraction bar often appears on a completely
    separate PyMuPDF line — so we CANNOT rely on seeing "/" within this line.

    Detection strategy: if we see small-font digit strings that form a valid
    fraction (numerator < denominator, denominator is a standard value), we
    reconstruct it as "num/denom" regardless of whether "/" is present.
    """
    if not spans:
        return ""

    # Single span — only try fraction split on longer digit strings (3+ chars)
    # Short strings like "12" are ambiguous (twelve vs 1/2) and at main text
    # size they're always the number. Real fractions like "1516" are 3+ chars.
    if len(spans) == 1:
        text = spans[0].get("text", "")
        if text.isdigit() and len(text) >= 3:
            frac = _try_split_fraction(text)
            if frac:
                return frac[0] + "/" + frac[1]
        return text

    # Find the dominant non-slash font size in this line. In many CAD PDFs the
    # fraction slash is rendered slightly larger than nearby digits; using it as
    # the reference causes mixed-fraction detection to miss common patterns.
    non_slash_sizes = [
        float(s.get("size", 0))
        for s in spans
        if not _is_fraction_slash(s)
    ]
    sizes = [float(s.get("size", 0)) for s in spans]
    main_size = max(non_slash_sizes) if non_slash_sizes else (max(sizes) if sizes else 10.0)

    result = []
    i = 0

    def _append_frac(frac_str: str):
        """Append a fraction string with conservative spacing.
        Keep fractions tight after hyphens / parens / apostrophes so strings like
        PIPE1-1/2STD do not become PIPE1-1/2 STD. Only insert a space when the
        previous token really looks like a separate word/number."""
        if result and result[-1]:
            last_char = result[-1][-1]
            if last_char not in (" ", "-", "(", "[", "/", "'"):
                if last_char.isalpha() or last_char.isdigit():
                    result.append(" ")
        result.append(frac_str)

    while i < len(spans):
        span = spans[i]
        text = span.get("text", "")
        size = float(span.get("size", 0))

        # Skip standalone "/" — fraction bar (content already reconstructed)
        if _is_fraction_slash(span):
            if result and "/" in result[-1]:
                i += 1
                continue
            result.append(text)
            i += 1
            continue

        # Case A: Superscript numerator + denominator (with or without "/")
        # Pattern 1: ('7', flags=5) + ('16', small) → "7/16"
        # Pattern 2: ('7', flags=5) + ('/', slash) + ('16', small) → "7/16"
        if (_is_superscript(span) and _is_smaller_font(span, main_size)
                and text.isdigit() and i + 1 < len(spans)):
            next_span = spans[i + 1]
            next_text = next_span.get("text", "")

            # Pattern 1: numerator immediately followed by denominator
            if next_text.isdigit() and _is_smaller_font(next_span, main_size):
                try:
                    num_v, den_v = int(text), int(next_text)
                    if den_v in _VALID_DENOMS and 0 < num_v < den_v:
                        _append_frac(text + "/" + next_text)
                        i += 2
                        if i < len(spans) and _is_fraction_slash(spans[i]):
                            i += 1
                        continue
                except ValueError:
                    pass

            # Pattern 2: numerator + "/" + denominator (slash merged from adjacent line)
            if (_is_fraction_slash(next_span) and i + 2 < len(spans)):
                den_span = spans[i + 2]
                den_text = den_span.get("text", "")
                if den_text.isdigit() and _is_smaller_font(den_span, main_size):
                    try:
                        num_v, den_v = int(text), int(den_text)
                        if den_v in _VALID_DENOMS and 0 < num_v < den_v:
                            _append_frac(text + "/" + den_text)
                            i += 3  # skip num, slash, denom
                            continue
                    except ValueError:
                        pass

        # Case B: Small-font combined digits (with or without "/")
        # e.g. ('1516', size=10) → "15/16"
        # e.g. ('18', size=10) → "1/8"
        # e.g. ('12', size=10) → "1/2"
        if _is_smaller_font(span, main_size) and text.isdigit() and len(text) >= 3:
            frac = _try_split_fraction(text)
            if frac:
                _append_frac(frac[0] + "/" + frac[1])
                i += 1
                # Skip trailing "/" if present
                if i < len(spans) and _is_fraction_slash(spans[i]):
                    i += 1
                continue

        # Case C: Two same-sized digit spans → standalone fraction
        # e.g. ('5', size=10) + ('8', size=10) → "5/8"
        # Also handles: ('5', size=10) + ('/', slash) + ('8', size=10) → "5/8"
        if (text.isdigit() and _is_smaller_font(span, main_size) and i + 1 < len(spans)):
            next_span = spans[i + 1]
            next_text = next_span.get("text", "")
            next_size = float(next_span.get("size", 0))

            # Pattern 1: num + denom (adjacent)
            if (next_text.isdigit() and abs(size - next_size) < 1.0):
                try:
                    num_v, den_v = int(text), int(next_text)
                    if den_v in _VALID_DENOMS and 0 < num_v < den_v:
                        _append_frac(text + "/" + next_text)
                        i += 2
                        if i < len(spans) and _is_fraction_slash(spans[i]):
                            i += 1
                        continue
                except ValueError:
                    pass

            # Pattern 2: num + "/" + denom
            if (_is_fraction_slash(next_span) and i + 2 < len(spans)):
                den_span = spans[i + 2]
                den_text = den_span.get("text", "")
                den_size = float(den_span.get("size", 0))
                if (den_text.isdigit() and abs(size - den_size) < 1.0):
                    try:
                        num_v, den_v = int(text), int(den_text)
                        if den_v in _VALID_DENOMS and 0 < num_v < den_v:
                            _append_frac(text + "/" + den_text)
                            i += 3
                            continue
                    except ValueError:
                        pass

        # Case D: compact fraction digits followed by trailing slash
        # e.g. ('34') + ('/') → "3/4"
        if text.isdigit() and len(text) >= 2 and i + 1 < len(spans):
            next_span = spans[i + 1]
            if _is_fraction_slash(next_span):
                frac = _try_split_fraction(text)
                if frac:
                    _append_frac(frac[0] + "/" + frac[1])
                    i += 2
                    continue

        # Case E: mixed fraction where slash trails the compact frac span
        # e.g. ('2') + ('12') + ('/') → "2 1/2"
        # e.g. ("37'-10") + ('12') + ('/') → "37'-10 1/2"
        if i + 2 < len(spans):
            next_span = spans[i + 1]
            slash_span = spans[i + 2]
            next_text = next_span.get("text", "")
            if (
                next_text.isdigit()
                and len(next_text) >= 2
                and _is_fraction_slash(slash_span)
                and _is_smaller_font(next_span, main_size)
            ):
                frac = _try_split_fraction(next_text)
                if frac:
                    result.append(text)
                    _append_frac(frac[0] + "/" + frac[1])
                    i += 3
                    continue

        # Default: just append the text
        result.append(text)
        i += 1

    return "".join(result)


# ──────────────────────────────────────────────────────────────────────
# Text layout helpers
# ──────────────────────────────────────────────────────────────────────
def _estimate_text_width_units(text: str) -> float:
    """Rough width estimate in font-size units for Draft text."""
    units = 0.0
    for ch in text or "":
        if ch in "ilI|":
            units += 0.35
        elif ch == "1":
            units += 0.45
        elif ch in " /'-\".":
            units += 0.30
        elif ch in "MW@#%":
            units += 0.95
        else:
            units += 0.65
    return units


def _estimate_text_width_mm(text: str, font_size_fc: float) -> float:
    return _estimate_text_width_units(text) * font_size_fc


def _same_text_line(y1: float, y2: float, size1: float, size2: float) -> bool:
    tol = 0.25 * max(size1, size2, 1.0)
    return abs(y1 - y2) <= tol


# Lowercase characters whose glyphs genuinely descend below the baseline.
# ONLY lowercase forms — uppercase Q, J, etc. do NOT descend in standard
# engineering/technical fonts.  Symbols like / ( ) [ ] | are rendered ON
# the baseline in virtually all fonts used in shop drawings.
_DESCENDER_CHARS = frozenset("gjpqyçÿýĝĵ")


def _effective_descender(text: str, font_descender: float) -> float:
    """Return the descender offset to apply for *text*.

    Draft.make_text anchors at the bottom-left of the bounding box,
    but PDF positions text at the baseline.  The full font descender
    must be applied only when the rendered text actually contains
    glyphs that descend below the baseline (g, j, p, q, y — lowercase
    only).

    For all-caps or non-descending text (common in BOMs, dimension
    labels, and title blocks), we apply only a small fraction of the
    descender to avoid pushing the label below its correct position
    within table cells and annotation boxes.
    """
    if not text:
        return font_descender
    has_descenders = any(ch in _DESCENDER_CHARS for ch in text)
    if has_descenders:
        return font_descender          # full correction
    # All-caps / numeric rows in schedules and title blocks are typically
    # baseline-tight; keep the correction minimal for these runs.
    if text.upper() == text:
        return font_descender * 0.02
    # No descending glyphs — apply only a small fraction of the descender.
    # Draft and PDF font metrics can differ slightly; using too much offset
    # pushes all-caps table text visibly low.
    # Keep a conservative baseline-to-bbox gap for non-descending text.
    #
    # Tuned from 15% -> 8% based on OCR/engineering title-block samples.
    # This keeps descender-bearing words accurate while improving alignment
    # for labels like "TOTAL WEIGHT THIS DRAWING".
    # No descending glyphs — apply ~8% of the descender as a minimal
    # baseline-to-bottom-of-bbox gap (accounts for the tiny space most
    # fonts leave below the baseline even for non-descending glyphs).
    return font_descender * 0.08


def _normalize_pdf_font_name(font_name: str) -> str:
    """Normalize PDF font names to practical system font family names.

    PDF fonts often arrive as subset names like "ABCDEE+Helvetica-Bold".
    Draft accepts family names more reliably than subset/raw PDF names.
    """
    raw = str(font_name or "").strip()
    if not raw:
        return ""

    if "+" in raw:
        prefix, rest = raw.split("+", 1)
        if len(prefix) == 6 and prefix.isupper():
            raw = rest.strip()

    low = raw.lower()
    if "helvetica" in low or "arial" in low:
        family = "Arial"
    elif "times" in low:
        family = "Times New Roman"
    elif "courier" in low:
        family = "Courier New"
    elif "calibri" in low:
        family = "Calibri"
    else:
        return raw

    is_bold = bool(re.search(r"\bbold\b|\bbd\b", low))
    is_italic = bool(re.search(r"\bitalic\b|\boblique\b|\bit\b", low))
    if is_bold and is_italic:
        return f"{family} Bold Italic"
    if is_bold:
        return f"{family} Bold"
    if is_italic:
        return f"{family} Italic"
    return family


def _line_angle_deg(line: dict) -> float:
    text_dir = line.get("dir", (1.0, 0.0))
    if text_dir and len(text_dir) >= 2:
        try:
            dx, dy = float(text_dir[0]), float(text_dir[1])
            return -math.degrees(math.atan2(dy, dx))
        except (TypeError, ValueError):
            pass
    return 0.0


def _normalize_text_angle_deg(angle_deg: float) -> float:
    """Normalize to [-90, 90] for orientation tests."""
    a = float(angle_deg) % 180.0
    if a > 90.0:
        a -= 180.0
    return a


def _rotated_text_threshold_deg(default: float = 12.0) -> float:
    """Shared threshold for routing rotated/diagonal labels."""
    raw = os.environ.get("BC_PDF_ROTATED_LABEL_DEG", "").strip()
    if raw:
        try:
            val = float(raw)
            if 0.0 <= val <= 89.0:
                return val
        except (TypeError, ValueError):
            pass
    return float(default)


def _apply_text_local_y_offset(pos: "Vector", angle_deg: float, offset_fc: float) -> "Vector":
    """Apply baseline->bbox offset in the text's local +Y axis (rotation aware)."""
    if abs(float(offset_fc)) <= 1e-12:
        return pos
    a = math.radians(float(angle_deg))
    dx = -math.sin(a) * float(offset_fc)
    dy = math.cos(a) * float(offset_fc)
    try:
        pos.x += dx
        pos.y += dy
    except (AttributeError, RuntimeError, TypeError, ValueError):
        pass
    return pos


def _span_origin_pdf(span: dict) -> Optional[Tuple[float, float]]:
    """Return a best-effort PDF-space baseline origin for one span."""
    o = span.get("origin")
    if o and len(o) >= 2:
        try:
            return float(o[0]), float(o[1])
        except (TypeError, ValueError):
            pass

    bbox = span.get("bbox")
    if bbox and len(bbox) >= 4:
        try:
            x0, _y0, _x1, y1 = [float(v) for v in bbox[:4]]
            size_pt = max(0.0, float(span.get("size", 0.0) or 0.0))
            desc = abs(float(span.get("descender", -0.2) or -0.2))
            return x0, (y1 - desc * size_pt)
        except (TypeError, ValueError):
            return None
    return None


def _render_text_spans_exact_labels(
    tdict: dict,
    text_group,
    page_h: float,
    opts: ImportOptions,
    scale: float,
    only_rotated: bool = False,
) -> int:
    """Render one Draft text object per PDF span for highest label fidelity."""
    if Draft is None or text_group is None:
        return 0

    count = 0
    # Per-text placement registry to suppress near-identical duplicate spans
    # (common in some PDFs with layered text paints), while preserving
    # genuinely distinct nearby labels.
    seen = {}
    rotated_threshold = _rotated_text_threshold_deg()
    for block in tdict.get("blocks", []):
        if block.get("type") != 0:
            continue
        for line in block.get("lines", []):
            spans = line.get("spans", []) or []
            if not spans:
                continue
            angle_deg = _line_angle_deg(line)
            norm_angle = _normalize_text_angle_deg(angle_deg)
            if only_rotated and abs(norm_angle) < rotated_threshold:
                continue
            rot = Rotation(Vector(0, 0, 1), angle_deg)

            for span in spans:
                text = span.get("text", "")
                if not text or text.isspace():
                    continue
                origin = _span_origin_pdf(span)
                if not origin:
                    continue

                try:
                    size_pt = float(span.get("size", 0.0) or 0.0)
                except (TypeError, ValueError):
                    size_pt = 0.0
                font_size_fc = max(0.1, (size_pt if size_pt > 0.0 else 3.0) * scale)
                txt = str(text).strip()
                if not txt:
                    continue

                dedupe_key = (
                    txt,
                    round(float(norm_angle), 1),
                    round(float(font_size_fc), 2),
                )
                bucket = seen.setdefault(dedupe_key, [])
                is_duplicate = False
                ox = float(origin[0])
                oy = float(origin[1])
                for px, py in bucket:
                    # Tight tolerance: only collapse effectively overlaid spans.
                    if abs(ox - px) <= 0.35 and abs(oy - py) <= 0.35:
                        is_duplicate = True
                        break
                if is_duplicate:
                    continue
                bucket.append((ox, oy))

                pos = _to_fc(origin, page_h, opts, scale)
                font_name = _normalize_pdf_font_name(span.get("font", ""))
                # Draft text anchoring differs slightly from PDF span origins for
                # rotated labels; apply a conservative local-Y nudge only for
                # clearly non-horizontal text to improve vertical/diagonal fit.
                if abs(norm_angle) >= rotated_threshold:
                    try:
                        desc = float(span.get("descender", -0.2) or -0.2)
                    except (TypeError, ValueError):
                        desc = -0.2
                    offset_fc = _effective_descender(txt, desc) * font_size_fc * 0.35
                    pos = _apply_text_local_y_offset(pos, angle_deg, offset_fc)
                try:
                    t = Draft.make_text([text], placement=Placement(pos, rot))
                except (RuntimeError, ValueError, TypeError, AttributeError):
                    continue

                try:
                    t.ViewObject.FontSize = font_size_fc
                    if font_name:
                        t.ViewObject.FontName = font_name
                    t.ViewObject.Justification = "Left"
                except (AttributeError, RuntimeError, TypeError, ValueError):
                    pass

                try:
                    text_group.addObject(t)
                except (AttributeError, RuntimeError, TypeError, ValueError):
                    pass
                count += 1
    return count


def _is_near_horizontal(dx: float, dy: float) -> bool:
    return abs(dx) > 0.95 and abs(dy) < 0.10


def _preprocess_text_blocks(tdict: dict) -> dict:
    """Split PyMuPDF lines conservatively when span coordinates prove the text
    is not a single clean run. This helps when PyMuPDF merges neighboring runs
    that are on almost the same line but should remain separate."""
    for block in tdict.get("blocks", []):
        if block.get("type") != 0:
            continue
        fixed_lines = []
        for line in block.get("lines", []):
            spans = line.get("spans", []) or []
            if not spans:
                continue
            line_dir = line.get("dir", (1.0, 0.0))
            try:
                dx, dy = float(line_dir[0]), float(line_dir[1])
            except (TypeError, ValueError, IndexError):
                dx, dy = 1.0, 0.0
            is_horizontal = _is_near_horizontal(dx, dy)
            current_spans = [spans[0]]
            current_bbox = list(spans[0].get("bbox", (0, 0, 0, 0)))
            prev_bbox = current_bbox[:]
            for span in spans[1:]:
                bbox = list(span.get("bbox", (0, 0, 0, 0)))
                should_split = False
                if is_horizontal:
                    gap_x = float(bbox[0]) - float(prev_bbox[2])
                    gap_y = abs(float(bbox[1]) - float(prev_bbox[1]))
                    # Conservative: split on strong wrap-back / large gaps / clear stacked shift.
                    if gap_x < -1.0 or gap_x > 28.0 or gap_y > 4.0:
                        should_split = True
                else:
                    gap_x = abs(float(bbox[0]) - float(prev_bbox[0]))
                    gap_y = float(bbox[1]) - float(prev_bbox[3])
                    if gap_y > 28.0 or gap_x > 4.0:
                        should_split = True
                if should_split:
                    fixed_lines.append({"spans": current_spans, "bbox": tuple(current_bbox), "dir": line_dir})
                    current_spans = [span]
                    current_bbox = bbox[:]
                else:
                    current_spans.append(span)
                    current_bbox[0] = min(current_bbox[0], bbox[0])
                    current_bbox[1] = min(current_bbox[1], bbox[1])
                    current_bbox[2] = max(current_bbox[2], bbox[2])
                    current_bbox[3] = max(current_bbox[3], bbox[3])
                prev_bbox = bbox[:]
            if current_spans:
                fixed_lines.append({"spans": current_spans, "bbox": tuple(current_bbox), "dir": line_dir})
        block["lines"] = fixed_lines
    return tdict


def _resolve_horizontal_run_overlaps(layout_items: List[dict], scale: float) -> List[dict]:
    """Push later horizontal sibling runs right only when they truly overlap.

    Uses the measured PDF bbox width when available and only falls back to
    estimated render width when needed. This avoids false-positive nudges that
    can misalign callouts in technical drawings.
    """
    if not layout_items:
        return layout_items
    s = max(scale, 1e-12)
    # IMPORTANT: tiny baseline jitter (e.g. 334.560 vs 334.562) can invert run
    # order when sorting primarily by baseline. Preserve left-to-right order
    # within each logical text line using a coarse line key when available.
    items = sorted(
        layout_items,
        key=lambda d: (d.get("line_key", round(d["baseline_y_pdf"], 1)), d["x_pdf"]),
    )
    prev = None
    for item in items:
        if not item.get("eligible_for_nudge", False):
            prev = item if item.get("is_horizontal", False) else prev
            continue
        if prev is None or not prev.get("eligible_for_nudge", False):
            prev = item
            continue
        if not _same_text_line(item["baseline_y_pdf"], prev["baseline_y_pdf"], item["font_size_fc"], prev["font_size_fc"]):
            prev = item
            continue
        prev_width = float(prev.get("orig_width_pdf", 0.0) or 0.0)
        if prev_width <= 1e-6:
            prev_width = float(prev.get("render_width_pdf", 0.0) or 0.0)
        prev_right = float(prev["x_pdf"]) + prev_width
        this_left = item["x_pdf"]
        overlap = prev_right - float(this_left)
        if overlap > 0.0:
            # Keep a tiny separation in PDF-space units.
            pad_pdf = min(
                0.75,
                (0.04 * max(prev["font_size_fc"], item["font_size_fc"], 1.0)) / s,
            )
            item["x_pdf"] += overlap + pad_pdf
        prev = item
    return items




_MIXED_FRACTION_RE = re.compile(
    r"""(?:
        \d+\s+\d+/\d+
        |
        \d+'-\d+\s+\d+/\d+"?
    )""",
    re.VERBOSE,
)


def _is_near_vertical_angle(angle_deg: float, tol_deg: float = 15.0) -> bool:
    a = angle_deg % 180.0
    return abs(a - 90.0) <= tol_deg


def _has_mixed_fraction_text(text: str) -> bool:
    return bool(_MIXED_FRACTION_RE.search((text or '').strip()))


def _projected_text_extents(item: dict, scale: float, font_size_fc: Optional[float] = None) -> Tuple[float, float, float, float]:
    """Projected extents in PDF-space for overlap checks.

    Returns (along_min, along_max, normal_min, normal_max). The anchor model
    matches how this importer places text today: left-justified runs extend
    forward from the insertion point; centered runs extend equally both ways.
    """
    fs = float(font_size_fc if font_size_fc is not None else item.get('font_size_fc', 0.0))
    s = max(scale, 1e-12)
    width_pdf = _estimate_text_width_mm(item.get('content', ''), fs) / s
    height_pdf = fs / s

    a = math.radians(float(item.get('angle_deg', 0.0)))
    ux, uy = math.cos(a), math.sin(a)
    nx, ny = -uy, ux

    x = float(item.get('x_pdf', 0.0))
    y = float(item.get('baseline_y_pdf', 0.0))
    anchor_along = x * ux + y * uy
    anchor_normal = x * nx + y * ny

    just = item.get('justification', 'Left')
    if just == 'Center':
        along_min = anchor_along - width_pdf / 2.0
        along_max = anchor_along + width_pdf / 2.0
    elif just == 'Right':
        along_min = anchor_along - width_pdf
        along_max = anchor_along
    else:
        along_min = anchor_along
        along_max = anchor_along + width_pdf

    normal_min = anchor_normal - height_pdf / 2.0
    normal_max = anchor_normal + height_pdf / 2.0
    return along_min, along_max, normal_min, normal_max


def _intervals_overlap(a0: float, a1: float, b0: float, b1: float, tol: float = 0.0) -> bool:
    return not (a1 < b0 - tol or b1 < a0 - tol)


def _axis_gap(a0: float, a1: float, b0: float, b1: float) -> float:
    if _intervals_overlap(a0, a1, b0, b1):
        return 0.0
    if a1 < b0:
        return b0 - a1
    return a0 - b1


def _apply_vertical_mixed_fraction_compaction(layout_items: List[dict], scale: float) -> List[dict]:
    """Shrink risky rotated mixed-fraction runs slightly when they would collide
    along their text direction.

    This is intentionally conservative: it touches only near-vertical mixed
    fractions and only when a projected overlap risk exists.
    """
    if not layout_items:
        return layout_items

    for item in layout_items:
        text = item.get('content', '')
        angle = float(item.get('angle_deg', 0.0))
        if not (_is_near_vertical_angle(angle) and _has_mixed_fraction_text(text)):
            continue

        base_fs = float(item.get('font_size_fc', 0.0))
        if base_fs <= 0:
            continue

        def risky(test_fs: float, _item=item) -> bool:
            a0, a1, n0, n1 = _projected_text_extents(_item, scale, test_fs)
            normal_tol = 0.20 * max(test_fs / max(scale, 1e-12), 1.0)
            min_clearance = 0.18 * max(test_fs / max(scale, 1e-12), 1.0)
            for other in layout_items:
                if other is _item:
                    continue
                oa0, oa1, on0, on1 = _projected_text_extents(other, scale)
                if not _intervals_overlap(n0, n1, on0, on1, tol=normal_tol):
                    continue
                if _axis_gap(a0, a1, oa0, oa1) < min_clearance:
                    return True
            return False

        if risky(base_fs):
            new_fs = base_fs
            for factor in (0.92, 0.88, 0.84):
                trial = base_fs * factor
                if not risky(trial):
                    new_fs = trial
                    break
                new_fs = trial
            item['font_size_fc'] = new_fs

    return layout_items


# ──────────────────────────────────────────────────────────────────────
# Raster page import (scanned PDF fallback)
# ──────────────────────────────────────────────────────────────────────
def _import_page_as_raster(pdf_doc, page, page_num: int, page_h: float,
                           opts: ImportOptions, scale: float,
                           parent, fc_doc):
    """Render a PDF page as a raster image and place it as an ImagePlane.

    Used for scanned PDFs, map/art PDFs, or pages with no usable vector content.
    DPI is auto-scaled to page physical size so small pages stay crisp and
    very large pages don't exhaust memory.
    """
    dpi = opts.raster_dpi or 200

    # Adaptive DPI: scale with page physical size so the image is always
    # readable without wasting memory on large sheets.
    #   A4 / Letter   (≤ 700 cm²)  → 200 DPI (default)
    #   A3 / Tabloid  (700–2000 cm²) → 300 DPI (maps need more detail)
    #   A2 and larger (> 2000 cm²) → 150 DPI (save memory, still readable)
    if not opts.raster_dpi_user_set:   # only adjust when user hasn't explicitly set a value
        w_cm = page.rect.width  * MM_PER_PT / 10.0
        h_cm = page.rect.height * MM_PER_PT / 10.0
        area_cm2 = w_cm * h_cm
        if area_cm2 > 2000:
            dpi = 150
        elif area_cm2 > 700:
            dpi = 300

    zoom = dpi / 72.0
    mat = fitz.Matrix(zoom, zoom)
    pix = page.get_pixmap(matrix=mat)

    # Save to temp file
    tmpdir = os.path.join(FreeCAD.getUserAppDataDir(),
                          "Mod", "PDFVectorImporter", "temp")
    os.makedirs(tmpdir, exist_ok=True)
    img_path = os.path.join(tmpdir, f"page_{page_num}_{dpi}dpi.png")
    pix.save(img_path)
    # Register cleanup: remove temp image when document is closed or on next import
    _register_temp_cleanup(img_path)

    # Calculate real-world size in mm from PDF page dimensions
    w_mm = page.rect.width * MM_PER_PT
    h_mm = page.rect.height * MM_PER_PT

    try:
        ip = fc_doc.addObject("Image::ImagePlane", f"Page_{page_num}_raster")
        ip.ImageFile = img_path
        ip.XSize = w_mm
        ip.YSize = h_mm
        ip.Placement = Placement(_v(0, 0, -0.1), Rotation())  # slightly behind vectors
        parent.addObject(ip)
        _msg(f"Placed page {page_num} as {dpi} DPI raster ({w_mm:.0f} x {h_mm:.0f} mm)")
    except (RuntimeError, OSError, ValueError, TypeError) as e:
        _warn(f"Raster placement failed: {e}\n"
              f"Image saved to: {img_path}")


# ──────────────────────────────────────────────────────────────────────
# Page importer
# ──────────────────────────────────────────────────────────────────────
def import_pdf_page(pdf_path: str, page_num: int = 1,
                    opts: Optional[ImportOptions] = None):
    """Import a single PDF page into the active FreeCAD document."""
    if opts is None:
        opts = ImportOptions(ignore_images=not IMAGE_WB)
    fc_doc = _ensure_doc()  # Store reference — don't rely on ActiveDocument later

    # Validate PDF before opening
    try:
        with open(pdf_path, 'rb') as f:
            header = f.read(5)
        if header != b'%PDF-':
            raise ValueError(f"Not a valid PDF file: {pdf_path}")
    except OSError as e:
        raise ValueError(f"Cannot read PDF file: {e}") from e

    pdf_doc = fitz.open(pdf_path)
    try:
        return _import_pdf_page_inner(pdf_doc, pdf_path, page_num, opts, fc_doc)
    finally:
        pdf_doc.close()


def _import_pdf_page_inner(pdf_doc, pdf_path, page_num, opts, fc_doc):
    """Inner implementation — pdf_doc is guaranteed to be closed by caller."""
    if pdf_doc.is_encrypted:
        raise ValueError(
            "This PDF is encrypted and cannot be imported. "
            "Please remove the encryption (e.g., print to a new PDF) and try again.")
    if page_num < 1 or page_num > len(pdf_doc):
        raise ValueError(f"Page {page_num} out of range 1..{len(pdf_doc)}")

    page = pdf_doc.load_page(page_num - 1)
    page_h = page.rect.height
    scale = (MM_PER_PT if opts.scale_to_mm else 1.0) * opts.user_scale

    # Top-level group
    top_group = None
    if opts.create_top_group:
        top_group = fc_doc.addObject(
            "App::DocumentObjectGroup", f"PDF_Page_{page_num}")

    # ── Layer / color grouping ──
    use_ocg = False
    if opts.layer_mode in ("auto", "ocg"):
        try:
            ocgs = pdf_doc.get_ocgs()
            use_ocg = bool(ocgs)
        except (RuntimeError, AttributeError, ValueError):
            use_ocg = False

    group_by_color = False
    if opts.layer_mode == "color":
        group_by_color = True
    elif opts.layer_mode == "none":
        group_by_color = False
    elif opts.layer_mode == "ocg":
        group_by_color = False
    else:  # auto
        group_by_color = opts.group_by_color and not use_ocg

    color_groups: Dict[Tuple[float, float, float], object] = {}
    layer_groups: Dict[str, object] = {}

    def _parent_for(stroke_rgb, layer_name):
        parent = top_group or fc_doc
        if use_ocg and layer_name:
            if layer_name not in layer_groups:
                layer_groups[layer_name] = _make_group(parent, f"Layer_{layer_name}", fc_doc)
            return layer_groups[layer_name]
        if group_by_color and stroke_rgb is not None:
            key = stroke_rgb
            if key not in color_groups:
                r, g, b = key
                label = f"Color_{int(r*255):02X}{int(g*255):02X}{int(b*255):02X}"
                color_groups[key] = _make_group(parent, label, fc_doc)
            return color_groups[key]
        return parent

    # ── Progress dialog (created early to cover all phases) ──
    _import_start = time.time()
    progress = None
    QtWidgets = None
    try:
        if FreeCAD.GuiUp:
            from PySide6 import QtWidgets, QtCore
    except ImportError:
        try:
            from PySide2 import QtWidgets, QtCore
        except ImportError:
            QtWidgets = None

    if FreeCAD.GuiUp and QtWidgets:
        try:
            progress = QtWidgets.QProgressDialog(
                f"Importing PDF page {page_num}...", "Cancel", 0, 100)
            progress.setWindowTitle("PDF Vector Importer")
            progress.setMinimumDuration(500)  # only show if > 500ms
            progress.setWindowModality(QtCore.Qt.WindowModal)
            progress.setValue(0)
        except (AttributeError, RuntimeError, TypeError):
            progress = None

    def _progress_check_cancel():
        """Check if user cancelled; closes dialog and returns True if cancelled."""
        if progress and progress.wasCanceled():
            _warn("Import cancelled by user")
            progress.close()
            return True
        return False

    def _progress_update(value, label):
        """Update progress dialog value and label, process events."""
        if not progress:
            return
        elapsed = time.time() - _import_start
        progress.setValue(value)
        progress.setLabelText(f"{label}  [{elapsed:.1f}s]")
        try:
            QtWidgets.QApplication.processEvents()
        except (AttributeError, RuntimeError):
            pass

    # ── Vector drawings ──
    try:
        drawings = page.get_drawings()
    except Exception as e:
        _warn(f"get_drawings() failed: {e}")
        drawings = []
    n_drawings = len(drawings)
    try:
        n_images = len(page.get_images(full=True))
    except Exception as e:
        _warn(f"get_images() failed: {e}")
        n_images = 0
    if opts.verbose:
        _msg(f"PDF page {page_num}: {n_drawings} drawing groups, "
             f"{n_images} embedded images found")

    # ── Determine effective import mode ──
    effective_mode = opts.import_mode
    if effective_mode == "auto":
        # Auto-detect: profile the page content to choose best mode
        _progress_update(2, "Analyzing page content...")
        try:
            tdict = page.get_text("dict")
        except Exception as e:
            _warn(f"get_text(dict) failed during auto-mode: {e}")
            tdict = {"blocks": []}
        n_text_blocks = sum(1 for b in tdict.get("blocks", []) if b.get("type") == 0)

        # Build lightweight vector density metrics once so multiple auto rules
        # can reuse the same profile without rescanning the page.
        vg_stats = _vector_group_stats(
            drawings,
            page_area=(page.rect.width * page.rect.height)
        ) if n_drawings > 0 else {}

        # Word extraction is only needed for heavy vector pages where we need
        # to distinguish CAD drawings from text-outline floods.
        n_words = 0
        if n_drawings >= AUTO_GLYPH_DRAWING_THRESHOLD:
            try:
                n_words = len(page.get_text("words"))
            except (RuntimeError, ValueError, TypeError, OSError):
                n_words = 0

        glyph_flood = _looks_like_vector_glyph_flood(
            n_drawings, n_text_blocks, n_words, vg_stats)
        fill_art_flood = _looks_like_fill_art_flood(n_drawings, vg_stats)

        _flood_reason = ""  # human-readable explanation for the log

        if n_drawings < 5 and n_text_blocks < 3:
            # Scanned / pure raster page — no usable vector content
            effective_mode = "raster"
            _flood_reason = "scanned/raster page (no usable vector content)"

        elif glyph_flood:
            # Vectorized text/map-art flood: huge counts of tiny filled groups.
            # Preserve only a raster appearance by default; if substantial
            # stroked vectors exist, keep a hybrid overlay.
            if vg_stats.get("stroke_ratio", 0.0) <= AUTO_GLYPH_STROKE_SPARSE_RATIO:
                effective_mode = "raster"
            else:
                effective_mode = "hybrid"
            _flood_reason = (
                f"vector glyph flood — "
                f"{n_drawings} groups, "
                f"fill-only={vg_stats.get('fill_only_ratio', 0.0):.0%}, "
                f"tiny-rect={vg_stats.get('tiny_rect_ratio', 0.0):.0%}, "
                f"text_blocks={n_text_blocks}"
            )

        elif fill_art_flood:
            # Map / illustrated-art flood: dominated by filled decorative shapes
            # (garden beds, terrain fills, tree canopies, etc.) with few strokes.
            # Importing as vectors creates unusable geometry — use raster instead.
            # If a meaningful stroke layer exists, hybrid preserves those lines.
            if vg_stats.get("stroke_ratio", 0.0) > AUTO_GLYPH_STROKE_SPARSE_RATIO:
                effective_mode = "hybrid"
            else:
                effective_mode = "raster"
            _flood_reason = (
                f"fill-art flood — "
                f"{n_drawings} groups, "
                f"fill-only={vg_stats.get('fill_only_ratio', 0.0):.0%}, "
                f"strokes={vg_stats.get('stroke_ratio', 0.0):.0%} "
                f"(map/decorative PDF — vectors would be unusable geometry)"
            )

        elif n_drawings > 3000 and n_images > 20:
            # GIS / map PDF — thousands of contour vectors on top of tiled
            # raster imagery (USGS topo maps, aerial surveys, etc.).
            # Importing vectors produces unusable results; render as raster.
            effective_mode = "raster"
            _flood_reason = (
                f"GIS/topo map — {n_drawings} vector groups over "
                f"{n_images} embedded images"
            )

        elif n_images > 0 and n_drawings > 0:
            # Has both images and vectors — hybrid gives best result
            effective_mode = "hybrid"

        else:
            effective_mode = "vectors"

        if opts.verbose:
            if _flood_reason:
                _msg(
                    f"Page {page_num}: smart mode override — {_flood_reason}"
                )
            _msg(f"Page {page_num}: auto-detected mode = {effective_mode}"
                 + (" (use Import Mode = Vectors to override)"
                    if effective_mode == "raster" and _flood_reason else ""))

    if _progress_check_cancel():
        if progress:
            progress.close()
        fc_doc.recompute()
        return top_group

    # ── Raster-only mode ──
    if effective_mode == "raster":
        _msg(f"Page {page_num}: rendering at {opts.raster_dpi} DPI (raster mode)")
        _progress_update(5, f"Rendering raster image at {opts.raster_dpi} DPI...")
        _import_page_as_raster(
            pdf_doc, page, page_num, page_h, opts, scale,
            top_group or fc_doc, fc_doc)
        if progress:
            progress.setValue(100)
            progress.close()
        fc_doc.recompute()
        _msg(f"Page {page_num}: imported as raster image")
        return top_group

    # ── Hybrid mode: place raster background, then overlay vectors ──
    if effective_mode == "hybrid":
        _msg(f"Page {page_num}: placing {opts.raster_dpi} DPI raster background…")
        _progress_update(5, f"Rendering raster image at {opts.raster_dpi} DPI...")
        _import_page_as_raster(
            pdf_doc, page, page_num, page_h, opts, scale,
            top_group or fc_doc, fc_doc)
        _msg(f"Page {page_num}: overlaying vector geometry…")
        # Fall through to vector import below

    # ── Legacy raster fallback (vectors mode, backwards compat) ──
    if effective_mode == "vectors" and opts.raster_fallback and n_drawings < 5:
        tdict = page.get_text("dict")
        n_text = sum(1 for b in tdict.get("blocks", []) if b.get("type") == 0)
        if n_text < 3:
            _msg(f"Page {page_num}: appears to be scanned/raster — "
                 f"rendering at {opts.raster_dpi} DPI")
            _progress_update(5, f"Rendering raster image at {opts.raster_dpi} DPI...")
            _import_page_as_raster(
                pdf_doc, page, page_num, page_h, opts, scale,
                top_group or fc_doc, fc_doc)
            if progress:
                progress.setValue(100)
                progress.close()
            fc_doc.recompute()
            _msg(f"Page {page_num}: imported as raster image")
            return top_group

    # ── Hatch detection ──
    hatch_indices = set()
    hatch_drawings = []
    if opts.hatch_mode != "import" and n_drawings > 20:
        try:
            import PDFHatchDetector
            hatch_indices = PDFHatchDetector.detect(drawings)
            if hatch_indices:
                n_hatch = len(hatch_indices)
                if opts.verbose:
                    _msg(f"Page {page_num}: {n_hatch} hatch lines detected "
                         f"(mode: {opts.hatch_mode})")
                if opts.hatch_mode == "skip":
                    drawings = [d for i, d in enumerate(drawings)
                                if i not in hatch_indices]
                    n_drawings = len(drawings)
                elif opts.hatch_mode == "group":
                    hatch_drawings = [d for i, d in enumerate(drawings)
                                      if i in hatch_indices]
                    drawings = [d for i, d in enumerate(drawings)
                                if i not in hatch_indices]
                    n_drawings = len(drawings)
        except (RuntimeError, ValueError, TypeError, AttributeError, KeyError, IndexError) as e:
            _warn(f"Hatch detection failed: {e}")

    obj_count = 0

    # ── Heavy-page detection ──
    # When a page has a huge number of drawing groups, automatically engage
    # safe-mode behavior: larger compound batches, throttled progress updates,
    # and guarded arc fitting.  This keeps vector import fully intact but
    # stops FreeCAD from drowning in per-object GUI overhead.
    _is_heavy = (opts.heavy_page_threshold > 0
                 and n_drawings > opts.heavy_page_threshold)
    if _is_heavy and opts.verbose:
        _msg(f"Page {page_num}: heavy page detected ({n_drawings} groups > "
             f"{opts.heavy_page_threshold}) — engaging safe-mode batching")

    # ── Compound batching state ──
    # Collect shapes in memory and commit them as Part::Compound objects
    # instead of one Part::Feature per wire.  This reduces GDI handle count
    # by ~batch_size× while keeping every vector path in the document.
    _batch_size = opts.compound_batch_size if opts.compound_batch_size > 0 else 0
    # Heavy pages get a larger batch to further reduce object count
    if _is_heavy and _batch_size:
        _batch_size = max(_batch_size, 500)
    # Batch by (parent, color, width, dash_style) so styling is preserved
    _batch_shapes: Dict[str, List] = {}   # style_key → list of shapes
    _batch_parents: Dict[str, object] = {}  # style_key → parent object
    _batch_styles: Dict[str, Tuple] = {}   # style_key → (stroke_rgb, width, dashes)
    _batch_idx: Dict[str, int] = {}        # parent_key → compound index

    def _flush_batch(style_key: str = None, force: bool = False):
        """Flush accumulated shapes into Part::Compound objects."""
        nonlocal obj_count
        keys = [style_key] if style_key else list(_batch_shapes.keys())
        for key in keys:
            shapes = _batch_shapes.get(key, [])
            if not shapes:
                continue
            if not force and len(shapes) < _batch_size:
                continue
            parent = _batch_parents[key]
            parent_name = parent.Name if hasattr(parent, 'Name') else str(id(parent))
            idx = _batch_idx.get(parent_name, 0) + 1
            _batch_idx[parent_name] = idx
            stroke_rgb, width, dashes = _batch_styles.get(key, (None, None, None))
            try:
                compound = Part.makeCompound(shapes)
                obj = fc_doc.addObject("Part::Feature", f"Batch_{idx}")
                obj.Shape = compound
                _apply_style(obj, stroke_rgb, width, dashes, opts)
                parent.addObject(obj)
                obj_count += 1
            except (RuntimeError, ValueError, TypeError) as e:
                # Fallback: create individually if compound fails
                _warn(f"Compound batch failed ({len(shapes)} shapes): {e}")
                for shp in shapes:
                    try:
                        obj = fc_doc.addObject("Part::Feature", "Wire")
                        obj.Shape = shp
                        _apply_style(obj, stroke_rgb, width, dashes, opts)
                        parent.addObject(obj)
                        obj_count += 1
                    except (RuntimeError, ValueError, TypeError):
                        pass
            _batch_shapes[key] = []

    def _add_to_batch(shape, parent, stroke_rgb, width, dashes):
        """Add a shape to the batch or create immediately if batching disabled."""
        nonlocal obj_count
        if not _batch_size:
            # No batching — original behavior
            obj = fc_doc.addObject("Part::Feature", "Wire")
            obj.Shape = shape
            _apply_style(obj, stroke_rgb, width, dashes, opts)
            parent.addObject(obj)
            obj_count += 1
            return
        parent_name = parent.Name if hasattr(parent, 'Name') else str(id(parent))
        # Build a style key so shapes with different visual styles stay separate
        dash_key = tuple(dashes) if dashes else ()
        style_key = f"{parent_name}|{stroke_rgb}|{width}|{dash_key}"
        if style_key not in _batch_shapes:
            _batch_shapes[style_key] = []
            _batch_parents[style_key] = parent
            _batch_styles[style_key] = (stroke_rgb, width, dashes)
        _batch_shapes[style_key].append(shape)
        if len(_batch_shapes[style_key]) >= _batch_size:
            _flush_batch(style_key, force=True)

    # ── Progress update frequency ──
    # On heavy pages, throttle to every 500 paths instead of 100.
    # This alone prevents thousands of Qt timer allocations that cause
    # the GDI handle exhaustion.
    _progress_interval = 500 if _is_heavy else 100

    # Update progress range now that we know the geometry count.
    # Layout: 0-9 = pre-analysis, 10-79 = geometry, 80-89 = text,
    #         90-95 = batching/cleanup, 96-100 = final placement.
    if progress:
        progress.setMaximum(100)
    _progress_update(10, f"Processing geometry... 0/{n_drawings}")

    for pg_idx, path_group in enumerate(drawings):
        # Throttled progress updates — every 500 on heavy pages, 100 otherwise.
        # Each processEvents() call allocates Qt timers; doing it 19k× is
        # what exhausts Windows GDI handles.
        if progress and pg_idx % _progress_interval == 0:
            geo_pct = 10 + int(69 * pg_idx / max(n_drawings, 1))
            _progress_update(
                geo_pct,
                f"Processing geometry... {pg_idx}/{n_drawings}")
            if progress.wasCanceled():
                _warn("Import cancelled by user")
                # Flush any pending batches before returning
                if _batch_size:
                    _flush_batch(force=True)
                progress.close()
                fc_doc.recompute()
                return top_group

        items = path_group.get("items", [])
        if not items:
            continue

        # PyMuPDF may include clip/group container entries in drawing streams.
        # These are not visible edges and should never become CAD geometry.
        grp_type = str(path_group.get("type", "") or "").lower()
        if grp_type in {"clip", "group"}:
            continue

        stroke = path_group.get("color") or path_group.get("stroke")
        stroke_rgb = _norm_color(stroke)
        fill = path_group.get("fill")
        close_path = path_group.get("closePath", False)
        width = _as_float(path_group.get("width") or path_group.get("lineWidth"))
        dashes = _parse_dashes(path_group.get("dashes"))
        layer_name = path_group.get("oc") or path_group.get("layer")

        # ── Skip invisible / clipping paths ──
        # Paths with no stroke AND no fill are PDF clipping boundaries — they
        # define mask regions, not visible geometry.  Drawing them produces
        # large arcs/rectangles that extend beyond the page and clutter the view.
        if stroke is None and fill is None:
            continue

        # ── Skip page-sized background fills ──
        # Some PDFs include a full-page rectangle as a background fill.
        # These add no useful geometry and obscure the actual drawing content.
        grp_rect = path_group.get("rect")
        if grp_rect and _is_rect(grp_rect):
            grp_area = abs(grp_rect.width * grp_rect.height)
            page_area = page.rect.width * page.rect.height
            if grp_area > page_area * 0.95:
                continue

        parent = _parent_for(stroke_rgb, layer_name)

        # Build edges per sub-path
        current_pt: Optional[Vector] = None
        sub_edges: List = []
        wires_edges: List[List] = []

        def flush_sub(close_flag: bool, _wires=wires_edges):
            nonlocal sub_edges, current_pt
            if sub_edges:
                _wires.append((sub_edges[:], close_flag))
            sub_edges = []
            current_pt = None

        for item in items:
            kind = item[0]
            data = item[1:]

            if kind == "m":  # moveto
                flush_sub(False)
                x, y = _parse_point(data)
                current_pt = _to_fc((x, y), page_h, opts, scale)

            elif kind == "l":  # lineto
                # PyMuPDF may give ('l', start_pt, end_pt) with BOTH points,
                # or ('l', end_pt) with just the destination.
                if len(data) >= 2 and _is_point(data[0]) and _is_point(data[1]):
                    # Two-point format: self-contained line segment
                    x0, y0 = _xy(data[0])
                    x1, y1 = _xy(data[1])
                    p_start = _to_fc((x0, y0), page_h, opts, scale)
                    p_end   = _to_fc((x1, y1), page_h, opts, scale)
                    seg = _len2d(p_start, p_end)
                    if seg > max(ZERO_TOL, opts.min_seg_len):
                        e = _edge_line(p_start, p_end)
                        if e:
                            sub_edges.append(e)
                    current_pt = p_end
                else:
                    # Single-point format: line from current_pt to destination
                    if current_pt is None:
                        continue
                    x, y = _parse_point(data)
                    p = _to_fc((x, y), page_h, opts, scale)
                    seg = _len2d(current_pt, p)
                    if seg > max(ZERO_TOL, opts.min_seg_len):
                        e = _edge_line(current_pt, p)
                        if e:
                            sub_edges.append(e)
                    current_pt = p

            elif kind == "c":  # cubic Bezier
                # PyMuPDF may give ('c', P0, P1, P2, P3) with 4 points
                # or ('c', P1, P2, P3) with 3 control/end points + implicit start
                if len(data) == 4 and all(_is_point(d) for d in data):
                    # Four-point format: all points explicit
                    x0, y0 = _xy(data[0])
                    x1, y1 = _xy(data[1])
                    x2, y2 = _xy(data[2])
                    x3, y3 = _xy(data[3])
                    p0 = _to_fc((x0, y0), page_h, opts, scale)
                    p1 = _to_fc((x1, y1), page_h, opts, scale)
                    p2 = _to_fc((x2, y2), page_h, opts, scale)
                    p3 = _to_fc((x3, y3), page_h, opts, scale)
                    current_pt = p0  # set current in case it was None
                else:
                    if current_pt is None:
                        continue
                    try:
                        (x1, y1), (x2, y2), (x3, y3) = _parse_cubic(data)
                    except (TypeError, ValueError, IndexError):
                        continue
                    p0 = current_pt
                    p1 = _to_fc((x1, y1), page_h, opts, scale)
                    p2 = _to_fc((x2, y2), page_h, opts, scale)
                    p3 = _to_fc((x3, y3), page_h, opts, scale)

                # Try arc reconstruction first
                arc = _arc_from_cubic(p0, p1, p2, p3, opts)
                if arc is not None:
                    e = _edge_arc(*arc)
                    if e is not None:
                        sub_edges.append(e)
                        current_pt = p3
                        continue

                # Fallback: linearize the cubic
                chord = max(ZERO_TOL, _len2d(p0, p3))
                N = max(4, min(opts.max_bezier_segments,
                               int(math.ceil(chord / max(ZERO_TOL, opts.curve_step_mm)))))
                prev = p0
                for i in range(1, N + 1):
                    t = i / float(N)
                    q = _bezier_point(p0, p1, p2, p3, t)
                    if _len2d(prev, q) > max(ZERO_TOL, opts.min_seg_len):
                        e = _edge_line(prev, q)
                        if e:
                            sub_edges.append(e)
                    prev = q
                current_pt = p3

            elif kind == "v":  # quadratic Bezier  (PDF rare but possible)
                if current_pt is None:
                    continue
                try:
                    (cx, cy), (ex, ey) = _parse_quad(data)
                except (TypeError, ValueError, IndexError):
                    continue
                p0 = current_pt
                # Promote quadratic to cubic:  CP1 = P0 + 2/3*(C-P0),  CP2 = P + 2/3*(C-P)
                ctrl = _to_fc((cx, cy), page_h, opts, scale)
                end  = _to_fc((ex, ey), page_h, opts, scale)
                cp1 = p0 + (ctrl - p0) * (2.0 / 3.0)
                cp2 = end + (ctrl - end) * (2.0 / 3.0)
                # Reuse cubic logic
                chord = max(ZERO_TOL, _len2d(p0, end))
                N = max(4, min(opts.max_bezier_segments,
                               int(math.ceil(chord / max(ZERO_TOL, opts.curve_step_mm)))))
                prev = p0
                for i in range(1, N + 1):
                    t = i / float(N)
                    q = _bezier_point(p0, cp1, cp2, end, t)
                    if _len2d(prev, q) > max(ZERO_TOL, opts.min_seg_len):
                        e = _edge_line(prev, q)
                        if e:
                            sub_edges.append(e)
                    prev = q
                current_pt = end

            elif kind == "y":  # curveto with final point == control point 2
                if current_pt is None:
                    continue
                try:
                    (x1, y1), (x3, y3) = _parse_quad(data)
                except (TypeError, ValueError, IndexError):
                    continue
                p0 = current_pt
                p1 = _to_fc((x1, y1), page_h, opts, scale)
                p3 = _to_fc((x3, y3), page_h, opts, scale)
                p2 = p3  # control point 2 == endpoint for 'y' command
                chord = max(ZERO_TOL, _len2d(p0, p3))
                N = max(4, min(opts.max_bezier_segments,
                               int(math.ceil(chord / max(ZERO_TOL, opts.curve_step_mm)))))
                prev = p0
                for i in range(1, N + 1):
                    t = i / float(N)
                    q = _bezier_point(p0, p1, p2, p3, t)
                    if _len2d(prev, q) > max(ZERO_TOL, opts.min_seg_len):
                        e = _edge_line(prev, q)
                        if e:
                            sub_edges.append(e)
                    prev = q
                current_pt = p3

            elif kind == "re":  # rectangle
                flush_sub(False)
                x, y, w, h = _parse_rect(data)
                if abs(w) < ZERO_TOL or abs(h) < ZERO_TOL:
                    continue
                c1 = _to_fc((x, y), page_h, opts, scale)
                c2 = _to_fc((x + w, y), page_h, opts, scale)
                c3 = _to_fc((x + w, y + h), page_h, opts, scale)
                c4 = _to_fc((x, y + h), page_h, opts, scale)
                edges = [_edge_line(c1, c2), _edge_line(c2, c3),
                         _edge_line(c3, c4), _edge_line(c4, c1)]
                edges = [e for e in edges if e is not None]
                wires_edges.append((edges, True))

            elif kind == "h":  # closePath
                flush_sub(True)
            # else: unknown command — silently skip

        # Flush any remaining sub-path
        flush_sub(close_path)

        # Post-process: detect polyline arcs and replace with true Part::Arc.
        # On heavy pages, guard arc fitting — only attempt on candidate chains
        # with a reasonable edge count.  Giant polyline runs (>64 edges) on
        # monster PDFs are almost certainly contour lines or map features, not
        # arcs from a CAD exporter.  The arc fitter still runs; it just skips
        # chains that are obviously not arc candidates.
        if opts.detect_arcs:
            processed = []
            for edges, is_closed in wires_edges:
                if _is_heavy and len(edges) > 64:
                    # Heavy-page guard: skip arc fitting on very long chains
                    processed.append((edges, is_closed))
                else:
                    new_edges = _polyline_edges_to_arcs(edges, opts)
                    processed.append((new_edges, is_closed))
            wires_edges = processed

        # Create FreeCAD objects from collected edges
        for edges, is_closed in wires_edges:
            want_face = ((opts.hatch_to_faces and fill is not None)
                         or (opts.make_faces and is_closed))
            if _batch_size and not want_face:
                # Batch wires into compounds to reduce GDI handle count
                try:
                    wire = Part.Wire(edges)
                    if is_closed and not wire.isClosed():
                        if wire.Vertexes:
                            p0 = wire.Vertexes[0].Point
                            pN = wire.Vertexes[-1].Point
                            if _len2d(_v(p0.x, p0.y), _v(pN.x, pN.y)) > ZERO_TOL:
                                closer = Part.LineSegment(pN, p0).toShape()
                                wire = Part.Wire(edges + [closer])
                    _add_to_batch(wire, parent, stroke_rgb, width, dashes)
                except (RuntimeError, ValueError, TypeError, AttributeError):
                    pass
            else:
                # Faces and non-batchable shapes: create individually
                obj = _make_shape_obj(edges, is_closed, make_face=want_face, fc_doc=fc_doc)
                if obj is not None:
                    _apply_style(obj, stroke_rgb, width, dashes, opts)
                    parent.addObject(obj)
                    obj_count += 1

    # ── Flush remaining batched shapes ──
    if _batch_size:
        total_pending = sum(len(v) for v in _batch_shapes.values())
        n_style_keys = len([k for k, v in _batch_shapes.items() if v])
        if total_pending > 0:
            _progress_update(80, f"Building compound 1/{n_style_keys}...")
        _flush_idx = 0
        for _fk in list(_batch_shapes.keys()):
            if _batch_shapes.get(_fk):
                _flush_idx += 1
                if n_style_keys > 1:
                    _progress_update(
                        80 + int(5 * _flush_idx / max(n_style_keys, 1)),
                        f"Building compound {_flush_idx}/{n_style_keys}...")
                if _progress_check_cancel():
                    fc_doc.recompute()
                    return top_group
                _flush_batch(_fk, force=True)
        if opts.verbose:
            total_batches = sum(_batch_idx.values())
            _msg(f"Page {page_num}: geometry batched into {total_batches} "
                 f"compound(s) (batch_size={_batch_size})")

    # ── Text import ──
    if opts.import_text and opts.text_mode != "none":
        _progress_update(86, "Importing text...")

        if _progress_check_cancel():
            fc_doc.recompute()
            return top_group

        # Try pdftocairo vector text (Geometry mode)
        svg_text_done = False
        if opts.text_mode == "geometry":
            try:
                from PDFVectorImporter.src.PDFSvgTextRenderer import render_text
                text_parent = top_group or fc_doc
                _progress_update(87, "Rendering text glyphs via pdftocairo...")
                result = render_text(
                    pdf_path, page_num, page_h, scale, page.rect.width,
                    fc_doc=fc_doc, parent_group=text_parent, flip_y=opts.flip_y)
                if result and result.get("glyphs", 0) > 0:
                    svg_text_done = True
                    obj_count += 1
                    n_glyphs = result['glyphs']
                    _progress_update(
                        89,
                        f"Rendering text glyphs ({n_glyphs} items)...")
                    if opts.verbose:
                        _msg(f"  Text: {result['glyphs']} glyphs from "
                             f"{result['shapes']} unique shapes (pdftocairo)")
            except (RuntimeError, ValueError, TypeError, OSError, ImportError, AttributeError) as e:
                _warn(f"SVG text renderer failed, falling back to Draft text: {e}")

        # Fall back to Draft text (Labels mode, or if pdftocairo unavailable)
        if not svg_text_done:
          try:
            tdict = _preprocess_text_blocks(page.get_text("dict"))
            text_group = _make_group(top_group or fc_doc, "Text", fc_doc)

            # High-fidelity Labels path: render each PDF span at its exact origin.
            # This preserves stacked fractions and micro-positioning much closer
            # to the source PDF than reconstructed line text.
            prefer_exact_labels = bool(getattr(opts, "strict_text_fidelity", True))
            _env_exact = os.environ.get("BC_PDF_EXACT_LABELS", "").strip().lower()
            if _env_exact:
                prefer_exact_labels = _env_exact not in ("0", "false", "off", "no")
            exact_span_count = 0
            if prefer_exact_labels:
                exact_span_count = _render_text_spans_exact_labels(
                    tdict, text_group, page_h, opts, scale
                )
                if exact_span_count > 0:
                    obj_count += exact_span_count
                    _progress_update(
                        89,
                        f"Rendering text labels ({exact_span_count} spans)...")
                    if opts.verbose:
                        _msg(f"  Text: {exact_span_count} span labels (exact placement)")
                elif opts.verbose:
                    _warn("Strict text fidelity enabled, but exact span labels produced 0 items.")
                # In strict mode, never run legacy line reconstruction.
                tdict["blocks"] = []
            else:
                # Route rotated text through exact span placement even when
                # strict mode is off. Legacy reconstruction remains for
                # horizontal text only.
                prefer_rotated_exact = True
                _env_rot = os.environ.get("BC_PDF_ROTATED_EXACT_LABELS", "").strip().lower()
                if _env_rot:
                    prefer_rotated_exact = _env_rot not in ("0", "false", "off", "no")
                if prefer_rotated_exact:
                    rotated_span_count = _render_text_spans_exact_labels(
                        tdict, text_group, page_h, opts, scale, only_rotated=True
                    )
                    if rotated_span_count > 0 and opts.verbose:
                        _msg(f"  Text: {rotated_span_count} rotated span labels (exact placement)")
                    obj_count += rotated_span_count

            for block in tdict.get("blocks", []):
                if block.get("type") != 0:
                    continue

                # Group lines within this block by Y + X proximity, but ONLY
                # merge when at least one line is a fraction fragment (pure digits
                # or "/").  This prevents BOM table cells from merging while still
                # recombining split fractions with their main dimension text.
                block_lines = block.get("lines", [])
                if not prefer_exact_labels:
                    horizontal_lines = []
                    rotated_threshold = _rotated_text_threshold_deg()
                    for _ln in block_lines:
                        _ang = _line_angle_deg(_ln)
                        # Keep legacy reconstruction for horizontal-ish lines.
                        # Rotated/diagonal lines are handled via exact spans above.
                        if abs(_normalize_text_angle_deg(_ang)) < rotated_threshold:
                            horizontal_lines.append(_ln)
                    block_lines = horizontal_lines
                y_groups: List[List] = []

                def _is_frac_fragment(ln, main_sz=0) -> bool:
                    """Is this line a fraction part (small-font orphaned digits or slash)?"""
                    spans = ln.get("spans", [])
                    txt = "".join(s.get("text", "") for s in spans).strip()
                    if txt == "/":
                        return True
                    # Pure digits at SMALLER font size = fraction numerator/denominator
                    if txt.isdigit() and spans:
                        span_size = float(spans[0].get("size", 0))
                        if main_sz > 0 and span_size < main_sz * 0.95:
                            return True
                    return False

                # Find the dominant font size in this block for reference
                block_main_size = 0
                for ln in block_lines:
                    for s in ln.get("spans", []):
                        sz = float(s.get("size", 0))
                        if sz > block_main_size:
                            block_main_size = sz

                for line in block_lines:
                    spans = line.get("spans", [])
                    if not spans:
                        continue
                    origin = spans[0].get("origin")
                    ly = origin[1] if origin else line.get("bbox", (0, 0, 0, 0))[1]
                    lbbox = line.get("bbox", (0, 0, 0, 0))
                    lx_start = lbbox[0]
                    lx_end = lbbox[2]
                    line_is_frac = _is_frac_fragment(line, block_main_size)

                    placed = False
                    for grp in y_groups:
                        _ref_spans = grp[0].get("spans") or []
                        ref_origin = _ref_spans[0].get("origin") if _ref_spans else None
                        ref_y = ref_origin[1] if ref_origin else grp[0].get("bbox", (0, 0, 0, 0))[1]
                        if abs(ly - ref_y) < 2.0:  # same Y
                            grp_has_frac = any(_is_frac_fragment(g, block_main_size) for g in grp)
                            grp_has_nonfrac = any(not _is_frac_fragment(g, block_main_size) for g in grp)

                            # Only merge if at least one side is a fraction fragment.
                            # NEVER merge two non-fragment lines into the same group —
                            # that creates jumbled span sequences like "6'-9 15/16 (PIPE1-..."
                            can_merge = False
                            if line_is_frac:
                                can_merge = True  # fragments always welcome
                            elif grp_has_frac and not grp_has_nonfrac:
                                can_merge = True  # non-frag joining a frag-only group
                            # else: non-frag trying to join a group that already has a non-frag → refuse

                            if can_merge:
                                for existing in grp:
                                    eb = existing.get("bbox", (0, 0, 0, 0))
                                    gap = min(abs(lx_start - eb[2]), abs(eb[0] - lx_end))
                                    if gap < 20:
                                        grp.append(line)
                                        placed = True
                                        break
                            if placed:
                                break
                    if not placed:
                        y_groups.append([line])

                # Count sibling groups on the same Y level so short horizontal
                # text is not accidentally centered into neighboring runs.
                _grp_y_map: Dict[int, int] = {}
                for grp in y_groups:
                    if not grp:
                        continue
                    spans0 = grp[0].get("spans", []) or []
                    ref_o = spans0[0].get("origin") if spans0 else None
                    gy = round(ref_o[1] if ref_o else grp[0].get("bbox", (0,0,0,0))[1])
                    _grp_y_map[gy] = _grp_y_map.get(gy, 0) + 1

                # Build layout items first so we can resolve same-line overlap
                layout_items = []
                for grp in y_groups:
                    def _line_x(ln):
                        o = ln.get("spans", [{}])[0].get("origin")
                        return o[0] if o else ln.get("bbox", (0, 0, 0, 0))[0]
                    grp.sort(key=_line_x)

                    all_spans = []
                    for line in grp:
                        all_spans.extend(line.get("spans", []))
                    if not all_spans:
                        continue

                    content = _reconstruct_line_text(all_spans)
                    if not content.strip() or content.strip() == "/":
                        continue

                    all_x0 = min(ln.get("bbox", (9e9,0,0,0))[0] for ln in grp)
                    all_x1 = max(ln.get("bbox", (0,0,-9e9,0))[2] for ln in grp)
                    all_y1 = max(ln.get("bbox", (0,0,0,-9e9))[3] for ln in grp)
                    _stripped = content.strip()
                    is_short = len(_stripped) <= 40

                    # Use span origins to recover the PDF baseline. Some OCR /
                    # generated PDFs contain outlier span origins, so we use the
                    # median origin and sanity-check it against a bbox-derived
                    # baseline estimate.
                    _first_span = grp[0].get("spans", [{}])[0]
                    origin_xy = []
                    for _sp in all_spans:
                        _o = _sp.get("origin")
                        if _o and len(_o) >= 2:
                            try:
                                origin_xy.append((float(_o[0]), float(_o[1])))
                            except (TypeError, ValueError):
                                pass

                    size_pt = max(float(s.get("size", 3)) for s in all_spans)
                    _desc_abs = abs(float(_first_span.get("descender", 0.15)))
                    baseline_from_bbox = all_y1 - _desc_abs * size_pt

                    if origin_xy:
                        ys = sorted(p[1] for p in origin_xy)
                        mid = len(ys) // 2
                        if len(ys) % 2 == 1:
                            baseline_from_origin = ys[mid]
                        else:
                            baseline_from_origin = (ys[mid - 1] + ys[mid]) * 0.5

                        # If origin baseline disagrees strongly with bbox-based
                        # estimate, trust bbox. This prevents occasional low/high
                        # label drift in title blocks.
                        drift = abs(baseline_from_origin - baseline_from_bbox)
                        drift_tol = max(0.9, size_pt * 0.28)
                        baseline_from_origin_used = drift <= drift_tol
                        baseline_y = (
                            baseline_from_bbox
                            if drift > drift_tol
                            else baseline_from_origin
                        )
                    else:
                        baseline_from_origin_used = False
                        baseline_y = baseline_from_bbox

                    text_dir = grp[0].get("dir", (1.0, 0.0))
                    if text_dir and len(text_dir) >= 2:
                        dx, dy = float(text_dir[0]), float(text_dir[1])
                        is_horizontal = _is_near_horizontal(dx, dy)
                        angle_deg = -math.degrees(math.atan2(dy, dx))
                    else:
                        dx, dy = 1.0, 0.0
                        is_horizontal = True
                        angle_deg = 0.0

                    _spans0 = grp[0].get("spans", []) or []
                    _ref_o = _spans0[0].get("origin") if _spans0 else None
                    _gy = round(_ref_o[1] if _ref_o else grp[0].get("bbox", (0,0,0,0))[1])
                    has_siblings = _grp_y_map.get(_gy, 1) > 1

                    if is_short and is_horizontal and not has_siblings:
                        x_pdf = (all_x0 + all_x1) / 2.0
                        justification = "Center"
                    else:
                        # Left-anchored rows should start from the true left-most
                        # text origin, not whichever span happened to come first.
                        if (not is_horizontal) and origin_xy and baseline_from_origin_used:
                            dlen = math.hypot(dx, dy)
                            if dlen <= 1e-12:
                                ux, uy = 1.0, 0.0
                            else:
                                ux, uy = dx / dlen, dy / dlen
                            anchor = min(origin_xy, key=lambda p: (p[0] * ux + p[1] * uy))
                            x_pdf = float(anchor[0])
                            baseline_y = float(anchor[1])
                        else:
                            x_pdf = min((p[0] for p in origin_xy), default=all_x0)
                        justification = "Left"

                    font = _normalize_pdf_font_name(all_spans[0].get("font", ""))
                    # Grab PyMuPDF normalised font metrics for baseline offset
                    _asc = float(all_spans[0].get("ascender", 0.8))
                    _desc = float(all_spans[0].get("descender", -0.2))
                    if "/" in _stripped and _stripped.replace("/", "").isdigit():
                        size_pt *= 0.65
                    elif not is_horizontal and " " in _stripped and "/" in _stripped:
                        size_pt *= 0.85

                    font_size_fc = size_pt * scale
                    render_width_pdf = _estimate_text_width_mm(content, font_size_fc) / max(scale, 1e-12)
                    orig_width_pdf = max(0.0, all_x1 - all_x0)

                    layout_items.append({
                        "content": content,
                        "font": font,
                        "font_size_fc": font_size_fc,
                        "angle_deg": angle_deg,
                        "is_horizontal": is_horizontal,
                        "baseline_y_pdf": baseline_y,
                        "baseline_is_origin": bool(origin_xy and baseline_from_origin_used),
                        "x_pdf": x_pdf,
                        "orig_width_pdf": orig_width_pdf,
                        "render_width_pdf": render_width_pdf,
                        "justification": justification,
                        "eligible_for_nudge": bool(is_horizontal and justification == "Left" and has_siblings),
                        "line_key": _gy,
                        "ascender": _asc,
                        "descender": _desc,
                    })

                layout_items = _resolve_horizontal_run_overlaps(layout_items, scale)
                layout_items = _apply_vertical_mixed_fraction_compaction(layout_items, scale)

                for item in layout_items:
                    pos = _to_fc((item["x_pdf"], item["baseline_y_pdf"]), page_h, opts, scale)
                    # Draft.make_text anchors at the bottom-left of the text
                    # box, but we have the PDF baseline position.  Shift down
                    # (in FreeCAD Y-up space) by the descender so the glyph
                    # baseline lands where the PDF specified it.
                    # SKIP this correction when baseline came from span origins
                    # (which are already the true baseline — no descender needed).
                    if not item.get("baseline_is_origin", False):
                        _d = _effective_descender(
                            item["content"],
                            float(item.get("descender", -0.2)),
                        )
                        pos = _apply_text_local_y_offset(
                            pos,
                            float(item.get("angle_deg", 0.0)),
                            _d * float(item["font_size_fc"]),
                        )
                    try:
                        rot = Rotation(Vector(0, 0, 1), item["angle_deg"])
                        t = Draft.make_text([item["content"]], placement=Placement(pos, rot))
                        try:
                            t.ViewObject.FontSize = item["font_size_fc"]
                            if item["font"]:
                                t.ViewObject.FontName = item["font"]
                            t.ViewObject.Justification = item["justification"]
                        except (AttributeError, RuntimeError, TypeError, ValueError):
                            pass
                        text_group.addObject(t)
                        obj_count += 1
                    except (RuntimeError, ValueError, TypeError, AttributeError):
                        pass
          except (RuntimeError, ValueError, TypeError, AttributeError) as e:
            _warn(f"Text import failed: {e}")

    # ── Build hatch group (if group mode) ──
    if hatch_drawings and opts.hatch_mode == "group":
        try:
            hatch_group = _make_group(top_group or fc_doc, "Hatching", fc_doc)
            for _pg_idx, path_group in enumerate(hatch_drawings):
                items = path_group.get("items", [])
                if not items:
                    continue
                stroke = path_group.get("color") or path_group.get("stroke")
                stroke_rgb = _norm_color(stroke)
                current_pt = None
                sub_edges = []
                for item in items:
                    kind = item[0]
                    data = item[1:]
                    if kind == "m":
                        if sub_edges:
                            try:
                                wire = Part.Wire(sub_edges)
                                obj = fc_doc.addObject("Part::Feature", "Hatch")
                                obj.Shape = wire
                                hatch_group.addObject(obj)
                                if stroke_rgb:
                                    try:
                                        obj.ViewObject.LineColor = stroke_rgb
                                    except (AttributeError, RuntimeError, TypeError):
                                        pass
                                obj_count += 1
                            except (RuntimeError, ValueError, TypeError, AttributeError):
                                pass
                            sub_edges = []
                        pt = data[0] if data else None
                        if pt and hasattr(pt, 'x'):
                            current_pt = _to_fc((pt.x, pt.y), page_h, opts, scale)
                    elif kind == "l" and current_pt is not None:
                        if len(data) >= 2 and _is_point(data[0]) and _is_point(data[1]):
                            p_start = _to_fc((_xy(data[0])), page_h, opts, scale)
                            p_end = _to_fc((_xy(data[1])), page_h, opts, scale)
                        else:
                            pt = data[0] if data else None
                            if pt and hasattr(pt, 'x'):
                                p_start = current_pt
                                p_end = _to_fc((pt.x, pt.y), page_h, opts, scale)
                            else:
                                continue
                        seg = _len2d(p_start, p_end)
                        if seg > ZERO_TOL:
                            e = _edge_line(p_start, p_end)
                            if e:
                                sub_edges.append(e)
                        current_pt = p_end
                if sub_edges:
                    try:
                        wire = Part.Wire(sub_edges)
                        obj = fc_doc.addObject("Part::Feature", "Hatch")
                        obj.Shape = wire
                        hatch_group.addObject(obj)
                        obj_count += 1
                    except (RuntimeError, ValueError, TypeError):
                        pass
            # Default hatching to hidden
            try:
                if hasattr(hatch_group, "ViewObject"):
                    hatch_group.ViewObject.Visibility = False
            except (AttributeError, RuntimeError):
                pass
            if opts.verbose:
                _msg(f"Page {page_num}: {len(hatch_drawings)} hatch lines → "
                     f"Hatching group (hidden)")
        except (RuntimeError, ValueError, TypeError, AttributeError, IndexError) as e:
            _warn(f"Hatch group creation failed: {e}")

    # ── Embedded images ──
    if not opts.ignore_images:
        try:
            img_group = _make_group(top_group or fc_doc, "Images", fc_doc)
            imglist = page.get_images(full=True)
            seen_xrefs = set()
            for img_info in imglist:
                xref = img_info[0]
                if xref in seen_xrefs:
                    continue
                seen_xrefs.add(xref)
                rects = page.get_image_rects(xref)
                if not rects:
                    continue
                try:
                    pix = fitz.Pixmap(pdf_doc, xref)
                    # Convert any non-plain-RGB source to RGB before saving PNG.
                    # This handles CMYK / DeviceN / grayscale / alpha safely.
                    cs = getattr(pix, "colorspace", None)
                    cs_n = None
                    try:
                        cs_n = int(getattr(cs, "n", 0)) if cs is not None else None
                    except (TypeError, ValueError):
                        cs_n = None
                    needs_rgb = (
                        pix.alpha
                        or pix.n != 3
                        or (cs_n is not None and cs_n != 3)
                    )
                    if needs_rgb:
                        pix = fitz.Pixmap(fitz.csRGB, pix)
                    tmpdir = os.path.join(
                        FreeCAD.getUserAppDataDir(),
                        "Mod", "PDFVectorImporter", "temp")
                    os.makedirs(tmpdir, exist_ok=True)
                    img_path = os.path.join(tmpdir, f"img_p{page_num}_x{xref}.png")
                    pix.save(img_path)
                except (RuntimeError, OSError, ValueError, TypeError) as e:
                    _warn(f"Image xref {xref} extract failed: {e}")
                    continue
                for r in rects:
                    pt0 = _to_fc((r.x0, r.y0), page_h, opts, scale)
                    pt1 = _to_fc((r.x1, r.y1), page_h, opts, scale)
                    w = abs(pt1.x - pt0.x)
                    h = abs(pt1.y - pt0.y)
                    try:
                        ip = fc_doc.addObject(
                            "Image::ImagePlane", "Image")
                        ip.ImageFile = img_path
                        ip.XSize = w
                        ip.YSize = h
                        ip.Placement = Placement(
                            _v(min(pt0.x, pt1.x), min(pt0.y, pt1.y), 0),
                            Rotation())
                        img_group.addObject(ip)
                        obj_count += 1
                    except (RuntimeError, OSError, ValueError, TypeError, AttributeError) as e:
                        _warn(f"Image placement failed: {e}")
        except (RuntimeError, OSError, ValueError, TypeError, AttributeError) as e:
            _warn(f"Image import failed: {e}")

    # ── Final cleanup / placement ──
    _progress_update(96, "Placing objects in document...")

    # Clean up empty groups (Text, Images, Color groups with no content)
    if top_group and hasattr(top_group, "Group"):
        for child in top_group.Group[:]:
            if (child.isDerivedFrom("App::DocumentObjectGroup")
                    and hasattr(child, "Group") and not child.Group):
                top_group.removeObject(child)
                fc_doc.removeObject(child.Name)

    _progress_update(98, "Placing objects in document...")

    # Close progress
    if progress:
        progress.setValue(100)
        progress.close()

    fc_doc.recompute()
    elapsed_total = time.time() - _import_start
    _msg(f"Page {page_num}: {obj_count} objects created in {elapsed_total:.1f}s")
    return top_group


# ──────────────────────────────────────────────────────────────────────
# Multi-page entry point
# ──────────────────────────────────────────────────────────────────────
def import_pdf(pdf_path: str, opts: Optional[ImportOptions] = None):
    """Import one or more pages from a PDF file."""
    if opts is None:
        opts = ImportOptions(ignore_images=not IMAGE_WB)
    fc_doc = _ensure_doc()

    # Reset ID counter once at the start of a multi-page import
    try:
        from PDFPrimitives import reset_ids
        reset_ids()
    except ImportError:
        pass

    # Clean up temp raster images from previous imports
    cleanup_temp_files()

    # Open PDF once to gather page count and heights (avoids triple-open + handle leaks)
    _unit_scale = (MM_PER_PT if opts.scale_to_mm else 1.0) * opts.user_scale
    page_height_scaled = 792 * _unit_scale  # default: US Letter height in points
    pages = opts.pages or [1]
    page_heights_scaled: Dict[int, float] = {}
    try:
        with fitz.open(pdf_path) as pdoc:
            total_pages = len(pdoc)
            if total_pages > 0:
                page_height_scaled = pdoc.load_page(0).rect.height * _unit_scale
            for p in pages:
                if 1 <= p <= total_pages:
                    try:
                        page_heights_scaled[p] = pdoc.load_page(p - 1).rect.height * _unit_scale
                    except (ValueError, RuntimeError):
                        pass
    except (RuntimeError, OSError) as e:
        _err(f"Cannot open PDF: {e}")
        return

    # Wrap entire import in a FreeCAD transaction so Ctrl+Z undoes it in one step
    fc_doc.openTransaction("Import PDF")
    try:
        imported_count = 0
        running_stack_offset = 0.0
        last_page_height = page_height_scaled
        for p in pages:
            if p < 1 or p > total_pages:
                _warn(f"Skipping out-of-range page {p} (PDF has {total_pages} pages)")
                continue
            try:
                import_pdf_page(pdf_path, page_num=p, opts=opts)
                curr_page_height = page_heights_scaled.get(p, page_height_scaled)
                # Offset each page group downward so they don't overlap.
                # FreeCAD may rename the group (e.g., PDF_Page_2 → PDF_Page_2001)
                # so we search for the most recently created matching group.
                if len(pages) > 1 and imported_count > 0:
                    running_stack_offset += last_page_height * 1.3
                    y_shift = -running_stack_offset
                    grp = None
                    for obj in reversed(fc_doc.Objects):
                        if (obj.Name.startswith(f"PDF_Page_{p}") and
                                obj.isDerivedFrom("App::DocumentObjectGroup")):
                            grp = obj
                            break
                    if grp and hasattr(grp, "Group"):
                        _msg(f"Offsetting {grp.Name} by Y={y_shift:.1f}")
                        for child in grp.Group:
                            try:
                                if hasattr(child, "Placement"):
                                    child.Placement.Base.y += y_shift
                                if hasattr(child, "Group"):
                                    for sub in child.Group:
                                        if hasattr(sub, "Placement"):
                                            sub.Placement.Base.y += y_shift
                            except (AttributeError, RuntimeError):
                                pass
                last_page_height = curr_page_height
                imported_count += 1
            except (RuntimeError, OSError, ValueError, TypeError, AttributeError) as e:
                _err(f"Failed to import page {p}: {e}\n{traceback.format_exc()}")
        fc_doc.commitTransaction()
    except Exception:
        fc_doc.abortTransaction()
        raise

    fc_doc.recompute()

    # Auto fit-all with orthographic top-down view
    try:
        import FreeCADGui
        view = FreeCADGui.ActiveDocument.ActiveView
        if view:
            view.setCameraType("Orthographic")
            view.viewTop()
            view.fitAll()
    except (ImportError, AttributeError, RuntimeError):
        pass

    return True
~~~

### PDFVectorImporter/src/PDFPrimitiveExtractor.py

- Path: `PDFVectorImporter/src/PDFPrimitiveExtractor.py`
- Size: `12.50 KB`
- Modified: `2026-04-04 03:30:02`

```python
# -*- coding: utf-8 -*-
# PDFPrimitiveExtractor.py — PyMuPDF → normalized Primitives
# BlueCollar Systems — BUILT. NOT BOUGHT.
"""
THE SEAM: converts PyMuPDF page data into host-neutral Primitives.
Rule 1: Parser modules must not know about domain-specific logic.
"""
from __future__ import annotations
import math
import re
from typing import List, Tuple

from PDFPrimitives import (
    Primitive, NormalizedText, PageData, next_id
)

MM_PER_PT = 25.4 / 72.0


def _parse_dashes(raw):
    """Normalize PyMuPDF dash patterns into a list of floats or None.

    PyMuPDF returns dash patterns as strings like '[ 6 6 ] 0'.
    This converts them to [6.0, 6.0] for downstream consumers,
    and returns None for solid lines.
    """
    if raw is None:
        return None
    if isinstance(raw, str):
        s = raw.strip()
        if not s or s in ("[] 0", "() 0"):
            return None
        # Extract numbers between brackets: '[ 6 6 ] 0' -> [6.0, 6.0]
        m = re.search(r"[\[\(](.*?)[\]\)]", s)
        if m:
            nums = [float(v) for v in m.group(1).split() if v]
            return nums if nums else None
        return None
    if isinstance(raw, (list, tuple)):
        try:
            nums = [float(v) for v in raw]
            return nums if nums else None
        except (TypeError, ValueError):
            return None
    return None


def _xy(obj) -> Tuple[float, float]:
    if hasattr(obj, "x") and hasattr(obj, "y"):
        return float(obj.x), float(obj.y)
    if isinstance(obj, (tuple, list)) and len(obj) >= 2:
        return float(obj[0]), float(obj[1])
    return 0.0, 0.0


def _norm_color(col) -> Tuple[float, float, float]:
    if col is None:
        return (0.0, 0.0, 0.0)
    try:
        if isinstance(col, (int, float)):
            g = max(0.0, min(1.0, float(col)))
            return (g, g, g)
        vals = [max(0.0, min(1.0, float(c))) for c in col]
        if len(vals) >= 4:
            # CMYK -> RGB conversion for print-oriented PDFs.
            c, m, y, k = vals[0], vals[1], vals[2], vals[3]
            r = (1.0 - c) * (1.0 - k)
            g = (1.0 - m) * (1.0 - k)
            b = (1.0 - y) * (1.0 - k)
            return (
                max(0.0, min(1.0, r)),
                max(0.0, min(1.0, g)),
                max(0.0, min(1.0, b)),
            )
        while len(vals) < 3:
            vals.append(vals[-1] if vals else 0.0)
        return (vals[0], vals[1], vals[2])
    except (TypeError, ValueError, AttributeError):
        return (0.0, 0.0, 0.0)


def extract_page(page, page_num: int, scale: float = 1.0,
                 flip_y: bool = True) -> PageData:
    """Extract normalized primitives from a PyMuPDF page."""
    # NOTE: Do NOT reset_ids() here — IDs must be unique across all pages
    # in a multi-page import. reset_ids() is called once at import start.

    page_h = page.rect.height
    page_w_mm = page.rect.width * MM_PER_PT * scale
    page_h_mm = page.rect.height * MM_PER_PT * scale

    primitives = []
    drawings = page.get_drawings()

    for path_group in drawings:
        items = path_group.get("items", [])
        if not items:
            continue

        stroke = _norm_color(path_group.get("color") or path_group.get("stroke"))
        fill = _norm_color(path_group.get("fill"))
        width = path_group.get("width")
        dashes = _parse_dashes(path_group.get("dashes"))
        close_path = path_group.get("closePath", False)
        layer_name = path_group.get("oc") or path_group.get("layer")

        # Build point sequences per sub-path
        current_pts: List[Tuple[float, float]] = []
        sub_paths: List[Tuple[List[Tuple[float, float]], bool]] = []

        def flush(closed: bool, _sub_paths=sub_paths):
            nonlocal current_pts
            if len(current_pts) >= 2:
                _sub_paths.append((current_pts[:], closed))
            current_pts = []

        for item in items:
            kind = item[0]
            data = item[1:]

            if kind == "m":
                flush(False)
                x, y = _parse_point(data)
                px, py = _to_mm(x, y, page_h, flip_y, scale)
                current_pts = [(px, py)]

            elif kind == "l":
                if len(data) >= 2 and hasattr(data[0], "x") and hasattr(data[1], "x"):
                    x0, y0 = _xy(data[0])
                    x1, y1 = _xy(data[1])
                    p0 = _to_mm(x0, y0, page_h, flip_y, scale)
                    p1 = _to_mm(x1, y1, page_h, flip_y, scale)
                    if not current_pts:
                        current_pts.append(p0)
                    current_pts.append(p1)
                else:
                    x, y = _parse_point(data)
                    current_pts.append(_to_mm(x, y, page_h, flip_y, scale))

            elif kind == "c":
                if len(data) == 4 and all(hasattr(d, "x") for d in data):
                    pts = [_xy(d) for d in data]
                else:
                    pts = _parse_cubic(data)
                # Linearize cubic Bézier
                p0 = _to_mm(pts[0][0], pts[0][1], page_h, flip_y, scale)
                p1 = _to_mm(pts[1][0], pts[1][1], page_h, flip_y, scale)
                p2 = _to_mm(pts[2][0], pts[2][1], page_h, flip_y, scale)
                p3 = _to_mm(pts[3][0] if len(pts) > 3 else pts[2][0],
                            pts[3][1] if len(pts) > 3 else pts[2][1],
                            page_h, flip_y, scale)
                if not current_pts:
                    current_pts.append(p0)
                N = max(4, min(32, int(math.ceil(_dist(p0, p3) / 0.5))))
                for i in range(1, N + 1):
                    t = i / float(N)
                    q = _bezier_pt(p0, p1, p2, p3, t)
                    current_pts.append(q)

            elif kind == "re":
                flush(False)
                x, y, w, h = _parse_rect(data)
                c1 = _to_mm(x, y, page_h, flip_y, scale)
                c2 = _to_mm(x + w, y, page_h, flip_y, scale)
                c3 = _to_mm(x + w, y + h, page_h, flip_y, scale)
                c4 = _to_mm(x, y + h, page_h, flip_y, scale)
                sub_paths.append(([c1, c2, c3, c4, c1], True))

            elif kind == "h":
                flush(True)

            elif kind == "v":
                if len(data) >= 2:
                    cx, cy = _xy(data[0])
                    ex, ey = _xy(data[1])
                    ctrl = _to_mm(cx, cy, page_h, flip_y, scale)
                    end = _to_mm(ex, ey, page_h, flip_y, scale)
                    if current_pts:
                        p0 = current_pts[-1]
                        cp1 = (p0[0] + 2/3*(ctrl[0]-p0[0]), p0[1] + 2/3*(ctrl[1]-p0[1]))
                        cp2 = (end[0] + 2/3*(ctrl[0]-end[0]), end[1] + 2/3*(ctrl[1]-end[1]))
                        N = 8
                        for i in range(1, N + 1):
                            t = i / float(N)
                            current_pts.append(_bezier_pt(p0, cp1, cp2, end, t))

        flush(close_path)

        for pts, is_closed in sub_paths:
            if len(pts) < 2:
                continue
            # Dedup consecutive
            cleaned = [pts[0]]
            for p in pts[1:]:
                if _dist(p, cleaned[-1]) > 0.01:
                    cleaned.append(p)
            if len(cleaned) < 2:
                continue

            xs = [p[0] for p in cleaned]
            ys = [p[1] for p in cleaned]
            bbox = (min(xs), min(ys), max(xs), max(ys))

            area = None
            if is_closed and len(cleaned) >= 3:
                area = _polygon_area(cleaned)

            ptype = "line" if len(cleaned) == 2 else ("closed_loop" if is_closed else "polyline")

            primitives.append(Primitive(
                id=next_id(), type=ptype, points=cleaned,
                bbox=bbox, stroke_color=stroke, fill_color=fill,
                dash_pattern=dashes, line_width=width,
                layer_name=layer_name, closed=is_closed,
                area=area, page_number=page_num
            ))

    # Text extraction
    text_items = _extract_text(page, page_h, page_num, flip_y, scale)

    return PageData(
        page_number=page_num,
        width=page_w_mm, height=page_h_mm,
        primitives=primitives, text_items=text_items,
        layers=[], xobject_names=[]
    )


def _extract_text(page, page_h, page_num, flip_y, scale) -> List[NormalizedText]:
    items = []
    try:
        tdict = page.get_text("dict")
    except (RuntimeError, TypeError, ValueError):
        return items

    for block in tdict.get("blocks", []):
        if block.get("type") != 0:
            continue
        for line in block.get("lines", []):
            spans = line.get("spans", [])
            if not spans:
                continue
            text = "".join(s.get("text", "") for s in spans).strip()
            if not text:
                continue

            origin = spans[0].get("origin")
            if origin:
                x, y = float(origin[0]), float(origin[1])
            else:
                bb = line.get("bbox", (0, 0, 0, 0))
                x, y = float(bb[0]), float(bb[1])

            px, py = _to_mm(x, y, page_h, flip_y, scale)
            size = max(float(spans[0].get("size", 3)), 1.0) * MM_PER_PT * scale
            font = str(spans[0].get("font", ""))

            text_dir = line.get("dir", (1.0, 0.0))
            dx = float(text_dir[0]) if text_dir else 1.0
            dy = float(text_dir[1]) if text_dir else 0.0
            angle = -math.degrees(math.atan2(dy, dx))

            normalized = text.upper().replace("  ", " ").strip()
            generic_tags = _classify_generic(text)

            items.append(NormalizedText(
                id=next_id(), text=text, normalized=normalized,
                insertion=(px, py), font_size=size,
                rotation=angle, font_name=font,
                page_number=page_num, generic_tags=generic_tags
            ))
    return items


def _classify_generic(text: str) -> list:
    """Domain-neutral text tags — domain-neutral."""
    tags = []
    t = text.strip()
    tu = t.upper()

    if re.search(r"\d+['']\s*[-–]?\s*\d", t) or re.search(r"\d+\s*/\s*\d+", t):
        tags.append("dimension_like")
    if re.search(r'\d+\.?\d*\s*(?:"|mm|cm|in|ft)', t, re.I):
        tags.append("dimension_like")
    if re.search(r"SCALE[:\s]*\d", tu) or re.search(r"\d+\s*:\s*\d+", t):
        tags.append("scale_like")
    if re.search(r"\b(DRAWN|CHECKED|DATE|SCALE|REV|SHEET|PROJECT|DWG|TITLE)\b", tu):
        tags.append("titleblock_like")
    if re.search(r"Ø|\bDIA\b|\bRAD\b|\bR\d", t, re.I):
        tags.append("callout_like")
    if re.search(r"\b(DETAIL|SECTION|SEC|VIEW|ELEVATION)\s+[A-Z]", tu):
        tags.append("detail_reference")
    if len(t) > 1 and len(t) < 60 and re.search(r"[A-Z]{2,}", tu):
        tags.append("label_like")
    return tags


# ── Coordinate helpers ──

def _to_mm(x, y, page_h, flip_y, scale):
    if flip_y:
        y = page_h - y
    return x * MM_PER_PT * scale, y * MM_PER_PT * scale


def _parse_point(data):
    if len(data) >= 1 and hasattr(data[0], "x"):
        return _xy(data[0])
    if len(data) >= 2:
        return float(data[0]), float(data[1])
    return 0.0, 0.0


def _parse_cubic(data):
    if len(data) == 3 and all(hasattr(d, "x") for d in data):
        return [_xy(d) for d in data]
    if len(data) >= 6:
        return [(float(data[0]), float(data[1])),
                (float(data[2]), float(data[3])),
                (float(data[4]), float(data[5]))]
    if len(data) == 4:
        return [_xy(d) for d in data]
    return [(0, 0), (0, 0), (0, 0)]


def _parse_rect(data):
    if len(data) >= 1 and hasattr(data[0], "x0"):
        r = data[0]
        return float(r.x0), float(r.y0), float(r.x1) - float(r.x0), float(r.y1) - float(r.y0)
    if len(data) >= 4:
        return float(data[0]), float(data[1]), float(data[2]), float(data[3])
    return 0.0, 0.0, 0.0, 0.0


def _bezier_pt(p0, p1, p2, p3, t):
    u = 1.0 - t
    return (u**3*p0[0] + 3*u**2*t*p1[0] + 3*u*t**2*p2[0] + t**3*p3[0],
            u**3*p0[1] + 3*u**2*t*p1[1] + 3*u*t**2*p2[1] + t**3*p3[1])


def _dist(a, b):
    return math.hypot(a[0] - b[0], a[1] - b[1])


def _polygon_area(pts):
    n = len(pts)
    a = 0.0
    for i in range(n):
        j = (i + 1) % n
        a += pts[i][0] * pts[j][1] - pts[j][0] * pts[i][1]
    return abs(a) / 2.0
```

### PDFVectorImporter/src/PDFPrimitives.py

- Path: `PDFVectorImporter/src/PDFPrimitives.py`
- Size: `3.85 KB`
- Modified: `2026-03-23 16:42:08`

```python
# -*- coding: utf-8 -*-
# PDFPrimitives.py — Host-neutral intermediate data model for FreeCAD
# BlueCollar Systems — BUILT. NOT BOUGHT.
"""
All recognition modules operate on these structures, NOT on FreeCAD objects.
Rule 2: Recognizers must operate on normalized primitives, not host entities.
"""
from __future__ import annotations
from dataclasses import dataclass, field
from typing import Dict, List, Optional, Tuple

_next_id = 0
def next_id() -> int:
    global _next_id
    _next_id += 1
    return _next_id

def reset_ids():
    global _next_id
    _next_id = 0


@dataclass
class RecognitionConfig:
    vertex_merge_tol: float = 0.1        # mm
    min_segment_len: float = 0.05        # mm
    loop_close_tol: float = 0.5          # mm
    region_padding: float = 25.0         # mm
    text_assoc_radius: float = 50.0      # mm
    dimension_assoc_radius: float = 75.0 # mm
    circle_min_diameter: float = 5.0     # mm
    circle_max_diameter: float = 100.0   # mm
    circle_fit_tol: float = 0.25         # mm RMS
    closed_loop_min_aspect: float = 1.5
    closed_loop_min_area: float = 100.0  # sq mm
    confidence_threshold: float = 0.60


@dataclass
class Primitive:
    id: int
    type: str              # "line", "arc", "circle", "polyline", "closed_loop", "rect"
    points: List[Tuple[float, float]]
    center: Optional[Tuple[float, float]] = None
    radius: Optional[float] = None
    start_angle: Optional[float] = None
    end_angle: Optional[float] = None
    bbox: Optional[Tuple[float, float, float, float]] = None
    stroke_color: Optional[Tuple[float, float, float]] = None
    fill_color: Optional[Tuple[float, float, float]] = None
    dash_pattern: Optional[list] = None
    line_width: Optional[float] = None
    layer_name: Optional[str] = None
    closed: bool = False
    area: Optional[float] = None
    page_number: int = 0
    generic_tags: List[str] = field(default_factory=list)


@dataclass
class NormalizedText:
    id: int
    text: str
    normalized: str        # uppercased, cleaned
    insertion: Tuple[float, float] = (0.0, 0.0)
    bbox: Optional[Tuple[float, float, float, float]] = None
    font_size: float = 3.0 # mm
    rotation: float = 0.0  # degrees
    font_name: str = ""
    page_number: int = 0
    generic_tags: List[str] = field(default_factory=list)
    domain_tags: List[dict] = field(default_factory=list)


@dataclass
class PageData:
    page_number: int
    width: float           # mm
    height: float          # mm
    primitives: List[Primitive] = field(default_factory=list)
    text_items: List[NormalizedText] = field(default_factory=list)
    layers: List[str] = field(default_factory=list)
    xobject_names: List[str] = field(default_factory=list)


@dataclass
class ParsedDimension:
    raw_text: str
    kind: str = "unknown"  # linear, diameter, radius, slot, scale, unknown
    value: object = None   # float or dict
    units: Optional[str] = None
    quantity: Optional[int] = None
    normalized_text: str = ""
    confidence: float = 0.0
    warnings: List[str] = field(default_factory=list)


@dataclass
class Region:
    id: int = 0
    page_number: int = 0
    bbox: Optional[Tuple[float, float, float, float]] = None
    primitive_ids: List[int] = field(default_factory=list)
    text_ids: List[int] = field(default_factory=list)
    region_type: str = "unknown"
    label: str = ""
    is_titleblock: bool = False
    confidence: float = 0.0


@dataclass
class PageProfile:
    page_number: int = 0
    primary_type: str = "unknown"
    scores: Dict[str, float] = field(default_factory=dict)
    has_layers: bool = False
    has_text: bool = False
    has_dimensions: bool = False
    circle_count: int = 0
    closed_loop_count: int = 0
    line_count: int = 0
    text_count: int = 0
    titleblock_likely: bool = False
```

### PDFVectorImporter/src/PDFRecognition.py

- Path: `PDFVectorImporter/src/PDFRecognition.py`
- Size: `983.00 B`
- Modified: `2026-03-23 16:42:08`

```python
# -*- coding: utf-8 -*-
# PDFRecognition.py — Pipeline orchestrator
# BlueCollar Systems — BUILT. NOT BOUGHT.
"""
Modes: none, generic, auto
Generic recognition runs document profiling, circle/boundary detection,
table/title block detection, and dimension association.
"""
from __future__ import annotations
from PDFPrimitives import PageData, RecognitionConfig
import PDFGenericRecognizer as generic_rec
import PDFDocumentProfiler as profiler


def run(page_data: PageData, mode: str = "auto", config: RecognitionConfig = None):
    if config is None:
        config = RecognitionConfig()
    if mode == "none":
        return {"generic": None, "mode_used": "none"}

    generic = generic_rec.analyze(page_data, config)

    if mode == "auto":
        profile = profiler.profile(page_data)
        effective = profile.primary_type if profile else "generic"
    else:
        effective = mode

    return {"generic": generic, "mode_used": effective}
```

### PDFVectorImporter/src/PDFRegions.py

- Path: `PDFVectorImporter/src/PDFRegions.py`
- Size: `2.46 KB`
- Modified: `2026-03-24 15:20:38`

```python
# -*- coding: utf-8 -*-
# PDFRegions.py — Region segmentation
# BlueCollar Systems — BUILT. NOT BOUGHT.
from __future__ import annotations
from PDFPrimitives import Region, PageData, next_id


def segment(page_data: PageData, config=None) -> list:
    """Split page into logical detail regions using spatial clustering."""
    prims = page_data.primitives
    if not prims:
        return []

    gap = 50.0  # mm — cluster gap threshold
    cell = gap * 3

    # Grid-based clustering
    cells = {}
    for p in prims:
        if not p.bbox: continue
        cx = (p.bbox[0]+p.bbox[2])/2
        cy = (p.bbox[1]+p.bbox[3])/2
        key = (int(cx/cell), int(cy/cell))
        cells.setdefault(key, []).append(p)

    # Union-find
    parent = {k:k for k in cells}
    def find(x):
        while parent[x] != x: parent[x] = parent[parent[x]]; x = parent[x]
        return x
    def unite(a,b):
        ra,rb = find(a),find(b)
        if ra!=rb: parent[ra]=rb

    for key in cells:
        gx,gy = key
        for dx in range(-1,2):
            for dy in range(-1,2):
                nb = (gx+dx,gy+dy)
                if nb in cells: unite(key,nb)

    groups = {}
    for key, ps in cells.items():
        root = find(key)
        groups.setdefault(root,[]).extend(ps)

    regions = []
    for cluster in groups.values():
        if len(cluster) < 3: continue
        xs = [v for p in cluster for v in (p.bbox[0],p.bbox[2]) if p.bbox]
        ys = [v for p in cluster for v in (p.bbox[1],p.bbox[3]) if p.bbox]
        if not xs: continue
        bbox = (min(xs),min(ys),max(xs),max(ys))
        r = Region(id=next_id(), page_number=page_data.page_number,
            bbox=bbox, primitive_ids=[p.id for p in cluster],
            region_type="unknown", label=f"Region_{len(regions)}")
        regions.append(r)

    _classify(regions, page_data)
    return regions


def _classify(regions, page_data):
    ph = page_data.height
    for r in regions:
        if not r.bbox: continue
        # Title block: bottom of page, wide
        if r.bbox[1] < ph * 0.15 and r.bbox[3] < ph * 0.3:
            r.is_titleblock = True
            r.region_type = "title_block"
            r.label = "TitleBlock"
            r.confidence = 0.80
        elif len(r.primitive_ids) > 50:
            r.region_type = "assembly"
            r.label = "Assembly"
        else:
            r.region_type = "detail"
            r.label = f"Detail_{r.id}"
```

### PDFVectorImporter/src/PDFScaleTool.py

- Path: `PDFVectorImporter/src/PDFScaleTool.py`
- Size: `24.04 KB`
- Modified: `2026-03-27 17:30:39`

```python
# -*- coding: utf-8 -*-
# PDFScaleTool.py — SketchUp-style "Measure & Scale" tool
# BlueCollar Systems — BUILT. NOT BOUGHT.
"""
Scale imported PDF geometry by picking two reference points and typing the
known real-world dimension.  Works like SketchUp's tape-measure scale:

  Method 1 (Selection-based):
    1. Select two vertices or edge endpoints in the 3D view
    2. Click "Scale by Reference..."
    3. Dialog shows measured distance — type the real dimension
    4. Everything scales

  Method 2 (Dialog-based):
    1. Click "Scale by Reference..." with nothing selected
    2. Enter coordinates of two known points manually
    3. Type the real dimension
    4. Everything scales

Accepts unit suffixes: mm, cm, m, in, ft, ', "
Accepts compound: 5'-6" or 5' 6 1/2"
"""
from __future__ import annotations

import math
import re

try:
    import FreeCAD
    import FreeCADGui
    import Part
    from FreeCAD import Vector
except ImportError:
    FreeCAD = FreeCADGui = Part = Vector = None

try:
    from PySide6 import QtWidgets, QtCore, QtGui
except ImportError:
    try:
        from PySide2 import QtWidgets, QtCore, QtGui
    except ImportError:
        QtWidgets = QtCore = QtGui = None


# ──────────────────────────────────────────────────────────────────────
# Unit parsing — proper sequential parser, not one monster regex
# ──────────────────────────────────────────────────────────────────────
_UNIT_MM = {
    "mm": 1.0, "millimeter": 1.0, "millimeters": 1.0, "millimetre": 1.0,
    "cm": 10.0, "centimeter": 10.0, "centimeters": 10.0,
    "m": 1000.0, "meter": 1000.0, "meters": 1000.0, "metre": 1000.0, "metres": 1000.0,
    "in": 25.4, "inch": 25.4, "inches": 25.4,
    "ft": 304.8, "foot": 304.8, "feet": 304.8,
    "yd": 914.4, "yard": 914.4, "yards": 914.4,
}

# Step 1: Feet-inches compound patterns
_RE_FT_IN = re.compile(
    r"""^\s*(\d+(?:\.\d+)?)\s*(?:'|ft|feet)\s*[-–]?\s*
        (\d+(?:\.\d+)?)?\s*
        (?:(\d+)\s*/\s*(\d+))?\s*
        (?:"|in|inch|inches)?\s*$""",
    re.VERBOSE | re.IGNORECASE)

# Step 2: Mixed number + unit:  "1 1/2 in"  "3 3/4 ft"
_RE_MIXED = re.compile(
    r"""^\s*(\d+(?:\.\d+)?)\s+(\d+)\s*/\s*(\d+)\s*
        ([a-zA-Z"']+)?\s*$""",
    re.VERBOSE)

# Step 3: Fraction + unit:  "1/2 in"  "3/8"
_RE_FRAC = re.compile(
    r"""^\s*(\d+)\s*/\s*(\d+)\s*
        ([a-zA-Z"']+)?\s*$""",
    re.VERBOSE)

# Step 4: Decimal + unit:  "406.4 mm"  "4.92 in"  "120"
_RE_DECIMAL = re.compile(
    r"""^\s*(\d+(?:\.\d+)?)\s*
        ([a-zA-Z"']+)?\s*$""",
    re.VERBOSE)

# Step 5: Feet-inches with dash shorthand:  "1'-4"  "5'-6 1/2"
_RE_FT_DASH = re.compile(
    r"""^\s*(\d+(?:\.\d+)?)\s*'\s*-?\s*
        (\d+(?:\.\d+)?)\s*
        (?:(\d+)\s*/\s*(\d+))?\s*
        "?\s*$""",
    re.VERBOSE)


def parse_dimension_mm(text: str) -> float:
    """Parse a dimension string into millimeters.

    Parse order (most specific first):
      1. Feet-inches compound:  5'-6"  5' 6 1/2"  5ft 6in
      2. Feet-dash shorthand:   1'-4   5'-6 1/2
      3. Mixed number + unit:   1 1/2 in   3 3/4 ft
      4. Fraction + unit:       1/2 in   3/8
      5. Decimal + unit:        406.4 mm   4.92 in   120
      6. Bare number → mm
    """
    text = text.strip()
    if not text:
        raise ValueError("Empty dimension")

    # Normalize curly quotes and dashes
    text = text.replace('\u2019', "'").replace('\u201D', '"')
    text = text.replace('\u2013', '-').replace('\u2014', '-')

    # 1. Feet-inches compound:  5'-6"  5' 6 1/2"  5ft 6in
    m = _RE_FT_IN.match(text)
    if m:
        ft = float(m.group(1))
        inches = float(m.group(2) or 0)
        if m.group(3) and m.group(4):
            inches += int(m.group(3)) / int(m.group(4))
        return (ft * 12.0 + inches) * 25.4

    # 2. Feet-dash shorthand:  1'-4   5'-6 1/2
    m = _RE_FT_DASH.match(text)
    if m:
        ft = float(m.group(1))
        inches = float(m.group(2))
        if m.group(3) and m.group(4):
            inches += int(m.group(3)) / int(m.group(4))
        return (ft * 12.0 + inches) * 25.4

    # 3. Mixed number + unit:  1 1/2 in   3 3/4 ft
    m = _RE_MIXED.match(text)
    if m:
        whole = float(m.group(1))
        frac = int(m.group(2)) / int(m.group(3))
        unit = (m.group(4) or "").strip().strip("'\"").lower()
        factor = _UNIT_MM.get(unit, 1.0)
        return (whole + frac) * factor

    # 4. Fraction + unit:  1/2 in   3/8
    m = _RE_FRAC.match(text)
    if m:
        frac = int(m.group(1)) / int(m.group(2))
        unit = (m.group(3) or "").strip().strip("'\"").lower()
        factor = _UNIT_MM.get(unit, 1.0)
        return frac * factor

    # 5. Decimal + unit:  406.4 mm   4.92 in   120
    m = _RE_DECIMAL.match(text)
    if m:
        value = float(m.group(1))
        unit = (m.group(2) or "").strip().strip("'\"").lower()
        # Handle ' and " as unit suffixes directly from input
        raw_unit = (m.group(2) or "").strip()
        if raw_unit == "'":
            return value * 304.8
        if raw_unit == '"':
            return value * 25.4
        factor = _UNIT_MM.get(unit, 1.0)
        return value * factor

    # 6. Bare number fallback → mm
    try:
        return float(text)
    except ValueError:
        raise ValueError(f"Cannot parse dimension: '{text}'") from None


# ──────────────────────────────────────────────────────────────────────
# Get selected points from FreeCAD selection
# ──────────────────────────────────────────────────────────────────────
def _get_selected_points() -> list:
    """Extract 3D points from the current FreeCAD selection.
    
    Tries multiple strategies:
    1. Sub-element vertices (user clicked a specific vertex)
    2. Edge endpoints (user clicked a line/wire)
    3. Picked points on faces/edges (click position on geometry)
    4. Shape bounding box centers (user selected whole objects)
    """
    points = []
    sel = FreeCADGui.Selection.getSelectionEx()

    for selobj in sel:
        # Strategy 1 & 2: Sub-element selections
        for sub in selobj.SubObjects:
            if hasattr(sub, "Point"):
                points.append(sub.Point)
            elif hasattr(sub, "Vertexes") and sub.Vertexes:
                for v in sub.Vertexes:
                    points.append(v.Point)

        # Strategy 3: Picked points (where the user actually clicked)
        if hasattr(selobj, "PickedPoints") and selobj.PickedPoints:
            for pp in selobj.PickedPoints:
                points.append(pp)

        # Strategy 4: If we still have nothing, try the object's shape
        if not points and selobj.Object:
            obj = selobj.Object
            if hasattr(obj, "Shape") and hasattr(obj.Shape, "Vertexes"):
                verts = obj.Shape.Vertexes
                if verts:
                    # Use first and last vertex of the shape
                    points.append(verts[0].Point)
                    if len(verts) > 1:
                        points.append(verts[-1].Point)
            elif hasattr(obj, "Placement"):
                points.append(obj.Placement.Base)

    # Deduplicate very close points
    if len(points) > 2:
        unique = [points[0]]
        for p in points[1:]:
            if all(math.hypot(p.x - u.x, p.y - u.y) > 0.001 for u in unique):
                unique.append(p)
        points = unique

    return points



def _collect_scale_targets(objects):
    """Flatten groups and filter duplicate children so objects are only scaled once."""
    seen = set()
    out = []

    def walk(obj):
        if obj is None:
            return
        name = getattr(obj, "Name", None)
        if name and name in seen:
            return
        if name:
            seen.add(name)
        if hasattr(obj, "Group") and obj.isDerivedFrom("App::DocumentObjectGroup"):
            for child in obj.Group:
                walk(child)
            return
        out.append(obj)

    for obj in objects or []:
        walk(obj)
    return out


def _transform_shape_about_origin(shape, factor: float, origin: "Vector"):
    """Scale a FreeCAD shape about an arbitrary origin without double-moving it."""
    if shape is None or shape.isNull():
        return shape
    mat = FreeCAD.Matrix()
    mat.move(-origin)
    mat.scale(factor, factor, factor)
    mat.move(origin)
    return shape.transformGeometry(mat)


# ──────────────────────────────────────────────────────────────────────
# Scale Dialog
# ──────────────────────────────────────────────────────────────────────
class ScaleDialog(QtWidgets.QDialog):
    """Shows measured distance and asks for the real-world dimension."""

    def __init__(self, measured_mm: float, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Scale by Reference — BlueCollar Systems")
        self.setMinimumWidth(440)

        self._measured = measured_mm
        self._result_mm = None

        measured_in = measured_mm / 25.4

        lbl_info = QtWidgets.QLabel(
            f"Measured distance between your two picks:\n"
            f"  {measured_mm:.4f} mm   ({measured_in:.4f} in)")
        lbl_info.setStyleSheet("font-weight: bold; font-size: 11pt;")

        lbl_prompt = QtWidgets.QLabel(
            "Enter the REAL dimension this distance should be:\n"
            "  Examples:  120 mm  ·  4.92 in  ·  5'-6\"  ·  1/2 in  ·  3.5 ft")

        self.dim_edit = QtWidgets.QLineEdit()
        self.dim_edit.setPlaceholderText("e.g. 1'-4  or  16 in  or  406.4 mm")
        self.dim_edit.setStyleSheet("font-size: 14pt; padding: 4px;")
        self.dim_edit.setFocus()
        self.dim_edit.textChanged.connect(self._update_preview)

        self.preview_label = QtWidgets.QLabel("")

        # Target group selector
        self.group_combo = QtWidgets.QComboBox()
        self._populate_groups()

        btns = QtWidgets.QDialogButtonBox(
            QtWidgets.QDialogButtonBox.Ok | QtWidgets.QDialogButtonBox.Cancel)
        btns.accepted.connect(self._on_ok)
        btns.rejected.connect(self.reject)

        form = QtWidgets.QFormLayout()
        form.addRow(lbl_info)
        form.addRow(lbl_prompt)
        form.addRow("Real dimension:", self.dim_edit)
        form.addRow(self.preview_label)
        form.addRow("Scale target:", self.group_combo)

        layout = QtWidgets.QVBoxLayout(self)
        layout.addLayout(form)
        layout.addWidget(btns)

    def _populate_groups(self):
        self.group_combo.addItem("Entire document", None)
        doc = FreeCAD.ActiveDocument
        if doc:
            for obj in doc.Objects:
                if obj.isDerivedFrom("App::DocumentObjectGroup"):
                    self.group_combo.addItem(obj.Label, obj.Name)

    def _update_preview(self, text):
        try:
            real = parse_dimension_mm(text)
            ratio = real / self._measured
            self.preview_label.setText(
                f"Scale factor: {ratio:.6f}  ({real:.2f} mm)")
            self.preview_label.setStyleSheet("color: green; font-weight: bold;")
        except (ValueError, ZeroDivisionError):
            self.preview_label.setText("(enter a valid dimension)")
            self.preview_label.setStyleSheet("color: gray;")

    def _on_ok(self):
        try:
            self._result_mm = parse_dimension_mm(self.dim_edit.text())
            self.accept()
        except (ValueError, ZeroDivisionError) as e:
            QtWidgets.QMessageBox.warning(
                self, "Invalid Input", f"Cannot parse dimension:\n{e}")

    @property
    def real_mm(self) -> float:
        return self._result_mm or self._measured

    @property
    def target_group_name(self) -> str:
        return self.group_combo.currentData()


# ──────────────────────────────────────────────────────────────────────
# Manual Point Entry Dialog (fallback when nothing is selected)
# ──────────────────────────────────────────────────────────────────────
class PointEntryDialog(QtWidgets.QDialog):
    """Enter two reference point coordinates manually."""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Scale by Reference — Pick Two Points")
        self.setMinimumWidth(400)

        info = QtWidgets.QLabel(
            "Enter coordinates of two points on a known dimension.\n\n"
            "TIP: Hover over vertices in FreeCAD — the coordinates\n"
            "show in the status bar at the bottom of the window.\n"
            "Or select two vertices/edges BEFORE clicking this button.")
        info.setStyleSheet("font-size: 10pt;")

        self.x1 = self._spin(); self.y1 = self._spin()
        self.x2 = self._spin(); self.y2 = self._spin()

        btns = QtWidgets.QDialogButtonBox(
            QtWidgets.QDialogButtonBox.Ok | QtWidgets.QDialogButtonBox.Cancel)
        btns.accepted.connect(self.accept)
        btns.rejected.connect(self.reject)

        form = QtWidgets.QFormLayout()
        form.addRow(info)
        form.addRow("Point 1 — X:", self.x1)
        form.addRow("Point 1 — Y:", self.y1)
        form.addRow("", QtWidgets.QLabel(""))
        form.addRow("Point 2 — X:", self.x2)
        form.addRow("Point 2 — Y:", self.y2)

        layout = QtWidgets.QVBoxLayout(self)
        layout.addLayout(form)
        layout.addWidget(btns)

    def _spin(self):
        s = QtWidgets.QDoubleSpinBox()
        s.setRange(-1e9, 1e9)
        s.setDecimals(4)
        s.setSuffix(" mm")
        return s

    def get_points(self):
        return (Vector(self.x1.value(), self.y1.value(), 0),
                Vector(self.x2.value(), self.y2.value(), 0))


# ──────────────────────────────────────────────────────────────────────
# Scaling logic
# ──────────────────────────────────────────────────────────────────────
def _scale_objects(objects, factor: float, origin: "Vector"):
    """Scale a list of FreeCAD objects uniformly about an origin point.
    
    Uses direct shape transformation instead of Draft.scale() for speed.
    Draft.scale() copies/recreates each object individually — painfully slow
    for 6000+ objects. Direct transform modifies geometry in-place.
    """
    n = len(objects)
    progress = None

    if FreeCAD.GuiUp and QtWidgets and n > 20:
        try:
            progress = QtWidgets.QProgressDialog(
                "Scaling geometry...", "Cancel", 0, n)
            progress.setWindowTitle("Scale by Reference")
            progress.setMinimumDuration(300)
            progress.setWindowModality(QtCore.Qt.WindowModal)
        except (AttributeError, RuntimeError):
            progress = None

    # Build a scale matrix once when scaling about global zero
    mat = None
    if origin is None or (abs(origin.x) < 1e-12 and abs(origin.y) < 1e-12 and abs(origin.z) < 1e-12):
        mat = FreeCAD.Matrix()
        mat.scale(factor, factor, factor)

    scaled = 0
    for i, obj in enumerate(objects):
        if progress and i % 200 == 0:
            progress.setValue(i)
            progress.setLabelText(f"Scaling... {i}/{n}")
            if progress.wasCanceled():
                FreeCAD.Console.PrintWarning("Scale cancelled.\n")
                break
            try:
                QtWidgets.QApplication.processEvents()
            except (AttributeError, RuntimeError):
                pass

        try:
            has_shape = hasattr(obj, "Shape") and not obj.Shape.isNull()
            has_font = (hasattr(obj, "ViewObject") 
                        and hasattr(obj.ViewObject, "FontSize"))

            if has_shape:
                # Shape objects: transformGeometry handles all coordinates
                # Do NOT also move Placement — that would double-move
                obj.Shape = _transform_shape_about_origin(obj.Shape, factor, origin) if mat is None else obj.Shape.transformGeometry(mat)
                scaled += 1
            elif has_font:
                # Text/annotation objects: scale position + font size
                if hasattr(obj, "Placement"):
                    pos = obj.Placement.Base
                    obj.Placement.Base = origin + (pos - origin) * factor
                try:
                    obj.ViewObject.FontSize = obj.ViewObject.FontSize * factor
                except (AttributeError, TypeError):
                    pass
                scaled += 1
            else:
                # Other objects (groups, etc.): just scale placement
                if hasattr(obj, "Placement"):
                    pos = obj.Placement.Base
                    obj.Placement.Base = origin + (pos - origin) * factor
        except (AttributeError, TypeError, ValueError, RuntimeError):
            pass

    if progress:
        progress.setValue(n)
        progress.close()

    FreeCAD.Console.PrintMessage(f"Transformed {scaled} shapes.\n")


def apply_scale(measured_mm: float, real_mm: float, target_group_name=None, origin=None):
    """Scale geometry by ratio real/measured about the picked origin."""
    if measured_mm <= 0:
        return
    factor = real_mm / measured_mm
    doc = FreeCAD.ActiveDocument
    if not doc:
        return

    if target_group_name:
        grp = doc.getObject(target_group_name)
        if grp and hasattr(grp, "Group"):
            objects = _collect_scale_targets(grp.Group[:])
        else:
            objects = _collect_scale_targets(doc.Objects[:])
    else:
        objects = _collect_scale_targets(doc.Objects[:])

    FreeCAD.Console.PrintMessage(
        f"Scaling {len(objects)} objects by {factor:.6f}...\n")

    # Wrap in undo transaction so the user can Ctrl+Z to undo the scale
    doc.openTransaction("Scale by Reference")

    if origin is None:
        origin = Vector(0, 0, 0)
    _scale_objects(objects, factor, origin)
    doc.recompute()
    doc.commitTransaction()

    # Fit view to new extents
    try:
        FreeCADGui.ActiveDocument.ActiveView.fitAll()
    except (AttributeError, RuntimeError):
        pass

    FreeCAD.Console.PrintMessage(
        f"Scaled by {factor:.6f}  ({real_mm:.2f} mm / {measured_mm:.2f} mm)\n")


# ──────────────────────────────────────────────────────────────────────
# FreeCAD Commands
# ──────────────────────────────────────────────────────────────────────
class ScaleByReferenceCommand:
    """Scale by picking two reference points on a known dimension."""

    def GetResources(self):
        return {
            "Pixmap": "",
            "MenuText": "Scale by Reference…",
            "ToolTip": ("Select two vertices or an edge, then click this.\n"
                        "Type the real-world measurement and everything scales.\n"
                        "Like SketchUp's tape-measure scale."),
        }

    def IsActive(self):
        return FreeCAD.ActiveDocument is not None

    def Activated(self):
        # Try to get points from the current selection first
        points = _get_selected_points()

        if len(points) >= 2:
            p1, p2 = points[0], points[1]
            measured = math.hypot(p2.x - p1.x, p2.y - p1.y)
            if measured < 1e-9:
                QtWidgets.QMessageBox.warning(
                    None, "Scale Tool",
                    "Selected points are identical — cannot measure distance.")
                return
            FreeCAD.Console.PrintMessage(
                f"Scale Tool: measured {measured:.4f} mm between selected points\n")
            self._show_scale_dialog(measured, points[0])
        else:
            # Nothing useful selected — guide the user
            reply = QtWidgets.QMessageBox.question(
                None, "Scale by Reference",
                "No geometry selected.\n\n"
                "To use this tool:\n"
                "  1. Click on a LINE (wire edge) with a known length\n"
                "  2. Then click 'Scale by Reference' again\n\n"
                "Or click 'Yes' to enter coordinates manually.",
                QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
                QtWidgets.QMessageBox.No)

            if reply == QtWidgets.QMessageBox.Yes:
                dlg = PointEntryDialog()
                exec_fn = getattr(dlg, "exec", None) or getattr(dlg, "exec_", None)
                if exec_fn and exec_fn() == QtWidgets.QDialog.Accepted:
                    p1, p2 = dlg.get_points()
                    measured = math.hypot(p2.x - p1.x, p2.y - p1.y)
                    if measured < 1e-9:
                        QtWidgets.QMessageBox.warning(
                            None, "Scale Tool", "Points are identical.")
                        return
                    self._show_scale_dialog(measured, p1)

    def _show_scale_dialog(self, measured_mm: float, origin=None):
        dlg = ScaleDialog(measured_mm)
        exec_fn = getattr(dlg, "exec", None) or getattr(dlg, "exec_", None)
        if exec_fn and exec_fn() == QtWidgets.QDialog.Accepted:
            apply_scale(measured_mm, dlg.real_mm, dlg.target_group_name, origin=origin)


class QuickScaleCommand:
    """Scale by a typed factor or ratio."""

    def GetResources(self):
        return {
            "Pixmap": "",
            "MenuText": "Quick Scale Factor…",
            "ToolTip": "Enter a scale factor (2.0 = double) or ratio (1:50).",
        }

    def IsActive(self):
        return FreeCAD.ActiveDocument is not None

    def Activated(self):
        text, ok = QtWidgets.QInputDialog.getText(
            None, "Quick Scale",
            "Enter scale factor (e.g. 2.0) or ratio (e.g. 1:50):",
            text="1.0")
        if not ok or not text.strip():
            return
        try:
            t = text.strip()
            if ":" in t:
                a, b = t.split(":", 1)
                factor = float(a) / float(b)
            else:
                factor = float(t)
        except (ValueError, ZeroDivisionError):
            QtWidgets.QMessageBox.warning(
                None, "Invalid", f"Cannot parse '{text}' as a scale factor.")
            return

        doc = FreeCAD.ActiveDocument
        sel = FreeCADGui.Selection.getSelection()
        objects = sel if sel else doc.Objects
        _scale_objects(_collect_scale_targets(list(objects)), factor, Vector(0, 0, 0))
        doc.recompute()

        try:
            FreeCADGui.ActiveDocument.ActiveView.fitAll()
        except (AttributeError, RuntimeError):
            pass

        FreeCAD.Console.PrintMessage(f"Quick scaled by {factor:.6f}\n")
```

### PDFVectorImporter/src/PDFSvgTextRenderer.py

- Path: `PDFVectorImporter/src/PDFSvgTextRenderer.py`
- Size: `18.45 KB`
- Modified: `2026-04-03 16:28:34`

```python
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
        candidates = []
        for pattern_base in [
            os.path.join(os.environ.get("LOCALAPPDATA", ""),
                         "Programs", "MiKTeX", "miktex", "bin", "x64"),
            r"C:\Program Files\MiKTeX\miktex\bin\x64",
            r"C:\Program Files\FreeCAD 1.1\bin",
            r"C:\Program Files\poppler\Library\bin",
            r"C:\Program Files\poppler\bin",
            r"C:\poppler\bin",
            r"C:\tools\poppler\bin",
        ]:
            candidates.append(os.path.join(pattern_base, "pdftocairo.exe"))
        # Common FreeCAD installs (portable / multiple versions)
        for cand in (
            list(_glob_paths(r"C:\Program Files\FreeCAD*\bin\pdftocairo.exe")) +
            list(_glob_paths(r"C:\Program Files\FreeCAD *\bin\pdftocairo.exe"))
        ):
            candidates.append(cand)
        for candidate in candidates:
            if os.path.isfile(candidate):
                return candidate

    return None


def _glob_paths(pattern: str):
    try:
        import glob
        return glob.glob(pattern)
    except Exception:
        return []


def render_text(pdf_path: str, page_num: int, page_h: float,
                scale: float, page_w: Optional[float] = None,
                fc_doc=None, parent_group=None,
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

        cmd_variants = [
            # Preferred: crop to page crop box (best fidelity when supported).
            [exe, "-svg", "-cropbox", "-f", str(page_num), "-l", str(page_num),
             "--", pdf_path, svg_path],
            # Compatibility fallback: some pdftocairo builds reject -cropbox with -svg.
            [exe, "-svg", "-f", str(page_num), "-l", str(page_num),
             "--", pdf_path, svg_path],
        ]
        last_err = None
        for cmd in cmd_variants:
            try:
                if os.path.isfile(svg_path):
                    os.remove(svg_path)
                subprocess.run(cmd, check=True, timeout=90, capture_output=True, **kw)
                if os.path.isfile(svg_path):
                    with open(svg_path, "r", encoding="utf-8") as f:
                        svg = f.read()
                    if svg:
                        break
            except subprocess.TimeoutExpired:
                # Timeout is unlikely to improve by retrying variants.
                raise
            except (subprocess.SubprocessError, OSError, ValueError, UnicodeError) as e:
                last_err = e
                continue

        if not svg:
            if last_err:
                raise last_err
            return None

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

    # Parse SVG dimensions / viewBox
    vb_min_x, vb_min_y, vb_w, vb_h = _parse_viewbox(svg)
    if vb_w <= 0 or vb_h <= 0:
        svg_w = _parse_svg_dim(svg, "width", page_w if page_w and page_w > 0 else page_h)
        svg_h = _parse_svg_dim(svg, "height", page_h)
        vb_min_x, vb_min_y, vb_w, vb_h = 0.0, 0.0, float(svg_w), float(svg_h)

    page_w_eff = float(page_w) if page_w and page_w > 0 else float(vb_w)
    page_h_eff = float(page_h) if page_h and page_h > 0 else float(vb_h)
    x_unit_to_mm = (page_w_eff * scale) / max(vb_w, 1e-12)
    y_unit_to_mm = (page_h_eff * scale) / max(vb_h, 1e-12)

    # Parse glyph definitions
    glyph_defs = {}
    for gid, path_d in re.findall(
            r'<g id="(glyph-\d+-\d+)">\s*<path d="([^"]*)"', svg, re.DOTALL):
        if path_d.strip():
            glyph_defs[gid] = path_d

    # Parse use placements
    placements = _parse_use_placements(svg)

    if not placements:
        return {"shapes": 0, "glyphs": 0}

    # Build Part.Shape for each unique glyph
    glyph_shapes: Dict[str, Part.Shape] = {}
    for gid, path_d in glyph_defs.items():
        edges = _svg_path_to_edges(path_d, x_unit_to_mm, y_unit_to_mm)
        if edges:
            try:
                compound = Part.makeCompound(edges)
                glyph_shapes[gid] = compound
            except (RuntimeError, ValueError, TypeError):
                pass

    # Place all glyphs
    all_shapes = []
    glyph_count = 0

    for gid, use_x, use_y, matrix in placements:
        shape = glyph_shapes.get(gid)
        if shape is None:
            continue

        # SVG coords → FreeCAD coords
        # Glyph use positions are in viewBox coordinates.
        placed = None
        if matrix and len(matrix) >= 6:
            a, b, c, d, e, f = [float(v) for v in matrix[:6]]
            e += float(use_x)
            f += float(use_y)
            tx = (e - vb_min_x) * x_unit_to_mm
            ty = (vb_h + vb_min_y - f) * y_unit_to_mm if flip_y else (f - vb_min_y) * y_unit_to_mm

            ratio_xy = (x_unit_to_mm / y_unit_to_mm) if abs(y_unit_to_mm) > 1e-12 else 1.0
            ratio_yx = (y_unit_to_mm / x_unit_to_mm) if abs(x_unit_to_mm) > 1e-12 else 1.0
            a11 = a
            a12 = -c * ratio_xy
            a21 = -b * ratio_yx
            a22 = d
            placed = _shape_affine_2d(shape, a11, a12, a21, a22, tx, ty)
        else:
            tx = (float(use_x) - vb_min_x) * x_unit_to_mm
            ty = ((vb_h + vb_min_y - float(use_y)) * y_unit_to_mm) if flip_y else ((float(use_y) - vb_min_y) * y_unit_to_mm)
            try:
                placed = shape.translated(Vector(tx, ty, 0.0))
            except (AttributeError, RuntimeError, TypeError):
                placed = None

        try:
            if placed is not None:
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


def _parse_svg_dim(svg: str, attr: str, fallback: float) -> float:
    m = re.search(rf'{attr}="([^"]+)"', svg)
    if not m:
        return float(fallback)
    raw = m.group(1)
    m_num = re.match(r'\s*([-+]?\d*\.?\d+(?:[eE][-+]?\d+)?)', raw)
    if not m_num:
        return float(fallback)
    try:
        return float(m_num.group(1))
    except (TypeError, ValueError):
        return float(fallback)


def _parse_viewbox(svg: str):
    m = re.search(r'viewBox="([^"]+)"', svg, re.IGNORECASE)
    if not m:
        return (0.0, 0.0, 0.0, 0.0)
    try:
        vals = [float(v) for v in re.split(r"[\s,]+", m.group(1).strip()) if v]
        if len(vals) >= 4:
            return (vals[0], vals[1], vals[2], vals[3])
    except (TypeError, ValueError):
        pass
    return (0.0, 0.0, 0.0, 0.0)


def _parse_use_placements(svg: str):
    placements = []
    for m in re.finditer(r'<use\b[^>]*>', svg, re.IGNORECASE | re.DOTALL):
        tag = m.group(0)
        href_m = re.search(r'(?:xlink:href|href)="([^"]+)"', tag, re.IGNORECASE)
        if not href_m:
            continue
        href = href_m.group(1).strip()
        if not href.startswith("#glyph-"):
            continue
        gid = href[1:]
        x = _attr_float(tag, "x", 0.0)
        y = _attr_float(tag, "y", 0.0)
        matrix = None
        tr_m = re.search(r'transform="([^"]+)"', tag, re.IGNORECASE)
        if tr_m:
            mm = re.search(r'matrix\(([^)]*)\)', tr_m.group(1), re.IGNORECASE)
            if mm:
                parts = [p for p in re.split(r'[\s,]+', mm.group(1).strip()) if p]
                if len(parts) >= 6:
                    try:
                        matrix = [float(v) for v in parts[:6]]
                    except (TypeError, ValueError):
                        matrix = None
        placements.append((gid, x, y, matrix))
    return placements


def _attr_float(tag: str, name: str, default: float = 0.0) -> float:
    m = re.search(rf'\b{name}="([^"]+)"', tag, re.IGNORECASE)
    if not m:
        return float(default)
    try:
        return float(m.group(1))
    except (TypeError, ValueError):
        return float(default)


def _shape_affine_2d(shape, a11: float, a12: float, a21: float, a22: float,
                     tx: float, ty: float):
    try:
        m = FreeCAD.Matrix()
        m.A11 = float(a11); m.A12 = float(a12); m.A13 = 0.0; m.A14 = float(tx)
        m.A21 = float(a21); m.A22 = float(a22); m.A23 = 0.0; m.A24 = float(ty)
        m.A31 = 0.0; m.A32 = 0.0; m.A33 = 1.0; m.A34 = 0.0
        m.A41 = 0.0; m.A42 = 0.0; m.A43 = 0.0; m.A44 = 1.0
        try:
            transformed = shape.transformGeometry(m)
            if transformed is not None:
                return transformed
        except (AttributeError, RuntimeError, TypeError, ValueError):
            pass
        cp = shape.copy()
        cp.transformShape(m, True, False)
        return cp
    except (AttributeError, RuntimeError, TypeError, ValueError):
        return None


def _svg_path_to_edges(d: str, scale_x: float, scale_y: Optional[float] = None) -> List:
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

    if scale_y is None:
        scale_y = scale_x

    def mk(gx: float, gy: float) -> Vector:
        return Vector(gx * scale_x, -gy * scale_y, 0.0)

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
```

### PDFVectorImporter/src/PDFValidation.py

- Path: `PDFVectorImporter/src/PDFValidation.py`
- Size: `1.40 KB`
- Modified: `2026-03-23 16:42:08`

```python
# -*- coding: utf-8 -*-
# PDFValidation.py — Confidence and validation layer
# BlueCollar Systems — BUILT. NOT BOUGHT.
from __future__ import annotations


def validate_recognition(recognition_result: dict) -> dict:
    """Post-process recognition results with final validation pass."""
    if not recognition_result or not recognition_result.get("domain"):
        return recognition_result

    domain = recognition_result["domain"]
    plates = domain.get("plates", [])
    holes = domain.get("holes", [])

    # Cross-validate plates vs dimensions
    for plate in plates:
        if plate.thickness_note and plate.width_geom and plate.height_geom:
            plate.evidence.append(
                f"Dimensions: {plate.width_geom:.1f} x {plate.height_geom:.1f}mm, "
                f"thickness={plate.thickness_note}")

    # Flag orphaned holes (not inside any plate)
    for hole in holes:
        if hole.inside_plate_id is None and hole.confidence > 0.5:
            hole.warnings.append("Hole not inside any detected plate")

    return recognition_result


CONFIDENCE_THRESHOLDS = {
    "trusted":    0.85,
    "build_warn": 0.75,
    "candidate":  0.60,
    "report_only": 0.0,
}

def action_for_confidence(score: float) -> str:
    if score >= 0.85: return "trusted"
    if score >= 0.75: return "build_warn"
    if score >= 0.60: return "candidate"
    return "report_only"
```

### PDFVectorImporter/su_manual_verification_checklist.md

- Path: `PDFVectorImporter/su_manual_verification_checklist.md`
- Size: `3.57 KB`
- Modified: `2026-03-18 15:31:36`

~~~markdown
# SketchUp Manual Verification Checklist (Blocked AUTO Tests)

Generated from `qa_results_auto_local_full_combined.json` + workbook `SketchUp Tests`.

## Run Setup
1. Open SketchUp Make 2017.
2. Confirm extension `bc_pdf_vector_importer` is enabled.
3. Use input PDF indicated per test.
4. Record result/evidence in `su_manual_verification_report.csv`.

## Blocked Tests
- SU-T001 | P0 | Install | Fresh install via Extension Manager
  Input: bc_pdf_vector_importer_v350.rbz
  Steps: Extensions > Extension Manager > Install > select .rbz
  Expected: No errors in Ruby Console. Menu appears under Plugins > PDF Vector Importer.
  Metrics: 

- SU-T019 | P0 | Geometry | Lines import correctly
  Input: 1071 - Rev 0.pdf
  Steps: Import with Full preset
  Expected: Straight lines present matching PDF
  Metrics: Edge count > 1000

- SU-T020 | P0 | Geometry | Arcs reconstructed from polyline segments
  Input: 1071 - Rev 0.pdf
  Steps: Import with Full preset. Zoom to pipe bends.
  Expected: Smooth arcs, not faceted polylines
  Metrics: Arc count > 10. Radius deviation < 2% RMS

- SU-T026 | P0 | Geometry | Color preservation
  Input: PDF with colored geometry
  Steps: Import with group_by_color=Yes
  Expected: Color groups created matching PDF stroke colors
  Metrics: 

- SU-T027 | P0 | Geometry | Faces created from closed paths
  Input: 1071 - Rev 0.pdf
  Steps: Import with Full preset (import_fills=Yes)
  Expected: Faces present on closed filled paths
  Metrics: Face count > 0

- SU-T028 | P0 | Text | Labels mode — text as SketchUp text entities
  Input: 1071 - Rev 0.pdf
  Steps: Import with Text=Labels
  Expected: Text objects placed near geometry. Readable.
  Metrics: Text count > 50

- SU-T041 | P1 | Preset | Fast preset — edges only, no text, fast
  Input: 1071 - Rev 0.pdf
  Steps: Import with Fast preset
  Expected: Edges only. No faces. No text. Fast import.
  Metrics: Import time < 5s

- SU-T044 | P0 | Core-1071 | Complete shop drawing import
  Input: 1071 - Rev 0.pdf
  Steps: Import with Full preset
  Expected: Geometry complete. Dimensions readable. Part marks visible.
  Metrics: Edges>1000, Arcs>10, Text>50

- SU-T047 | P0 | Core-1071 | Import time
  Input: 1071 - Rev 0.pdf
  Steps: Time the import
  Expected: < 15 seconds on modern hardware
  Metrics: Record actual time

- SU-T049 | P0 | Core-Topo | P0: All 27 OCG layers created
  Input: TX_Alvord topo
  Steps: Check Layers panel after import
  Expected: 27 PDF::Layer::* tags present
  Metrics: Count layers

- SU-T053 | P0 | Core-Topo | PNG predictor decoding works
  Input: TX_Alvord topo
  Steps: Import (test passes if import succeeds at all)
  Expected: Parser finds >300 objects from compressed xref
  Metrics: 

- SU-T054 | P0 | Core-Topo | Import time
  Input: TX_Alvord topo
  Steps: Time the import
  Expected: < 120 seconds
  Metrics: Record actual time

- SU-T057 | P0 | Layers | OCG layers detected from PDF
  Input: TX_Alvord topo
  Steps: Import. Check layer count.
  Expected: Layer count matches PDF OCG count (27)
  Metrics: 

- SU-T067 | P0 | Perf | Shop drawing runtime
  Input: 1071 - Rev 0.pdf
  Steps: Time Full preset import
  Expected: < 15 seconds
  Metrics: Record time

- SU-T068 | P0 | Perf | Topo map runtime
  Input: TX_Alvord topo
  Steps: Time Full preset import
  Expected: < 120 seconds
  Metrics: Record time

- SU-T078 | P0 | Undo | Re-import produces identical result
  Input: 1071 - Rev 0.pdf
  Steps: Import twice with same settings. Compare edge counts.
  Expected: Edge count identical both times.
  Metrics: 
~~~

### PDFVectorImporter/THIRD_PARTY_NOTICES.md

- Path: `PDFVectorImporter/THIRD_PARTY_NOTICES.md`
- Size: `620.00 B`
- Modified: `2026-03-23 16:42:08`

~~~markdown
# Third-Party Notices

This package includes third-party components in `src/lib`, including PyMuPDF and MuPDF runtime files.

## PyMuPDF / MuPDF

- Project: PyMuPDF
- Upstream: https://github.com/pymupdf/PyMuPDF
- License model: AGPL-3.0-or-later or commercial licensing (Artifex)
- Notes: This package bundles runtime files for convenience. If you redistribute this package, preserve upstream notices and comply with applicable third-party license terms.

For complete third-party metadata in this package, see:

- `src/lib/pymupdf-1.27.2.dist-info/METADATA`
- `src/lib/pymupdf-1.27.2.dist-info/COPYING`
~~~

## Test Files

Included files: `1`

### tests/test_pdf_primitive_extractor.py

- Path: `tests/test_pdf_primitive_extractor.py`
- Size: `765.00 B`
- Modified: `2026-04-03 18:12:57`

```python
from __future__ import annotations

import sys
import unittest
from pathlib import Path


SRC_DIR = Path(__file__).resolve().parents[1] / "PDFVectorImporter" / "src"
sys.path.insert(0, str(SRC_DIR))

from PDFPrimitiveExtractor import _norm_color  # noqa: E402


class TestPdfPrimitiveExtractor(unittest.TestCase):
    def test_cmyk_converts_to_rgb(self) -> None:
        rgb = _norm_color((0.0, 1.0, 1.0, 0.0))
        self.assertAlmostEqual(rgb[0], 1.0, places=3)
        self.assertAlmostEqual(rgb[1], 0.0, places=3)
        self.assertAlmostEqual(rgb[2], 0.0, places=3)

    def test_grayscale_scalar_expands(self) -> None:
        rgb = _norm_color(0.5)
        self.assertEqual(rgb, (0.5, 0.5, 0.5))


if __name__ == "__main__":
    unittest.main(verbosity=2)
```

## Project Scripts

### build_release.py

- Path: `build_release.py`
- Size: `3.25 KB`
- Modified: `2026-04-01 17:16:06`

```python
#!/usr/bin/env python3
"""build_release.py — BlueCollar Systems
Produces a clean PDFVectorImporter release zip suitable for FreeCAD Addon Manager
distribution and manual install.

Excluded:
  - __pycache__/ and *.pyc
  - .ruff_cache/
  - .github/
  - .git/
  - test PDFs, QA configs, and internal harness files
  - this script itself

Usage:
  python build_release.py
  python build_release.py --out /path/to/output_dir

Output:
  PDFVectorImporter_v<VERSION>.zip  (next to this script, or --out dir)
"""

import argparse
import re
import zipfile
from pathlib import Path

# ---------------------------------------------------------------------------
# Config
# ---------------------------------------------------------------------------

REPO_ROOT = Path(__file__).parent.resolve()
ADDON_DIR = REPO_ROOT / "PDFVectorImporter"

# Files / dirs to always exclude (matched against each path component)
EXCLUDE_DIRS = {
    "__pycache__",
    ".ruff_cache",
    ".github",
    ".git",
    "qa_runs",
    "adapters",  # CLI test harnesses — not needed at FreeCAD runtime
}

EXCLUDE_FILES = {
    ".gitignore",
    ".gitattributes",
    "build_release.py",
    "qa_config_example.json",
    "qa_config_template.json",
    "fc_smoke_payload.json",
    "fc_check_fitz.py",
    "run_pdf_vector_importer_tests.py",
    "su_manual_verification_checklist.md",
    "qa_config_local_live.json",
}

EXCLUDE_SUFFIXES = {
    ".pyc",
    ".pyo",
    ".pdf",       # test PDFs should not ship
    ".bak",
    ".swp",
}


def _should_exclude(rel: Path) -> bool:
    for part in rel.parts:
        if part in EXCLUDE_DIRS:
            return True
    if rel.name in EXCLUDE_FILES:
        return True
    if rel.suffix.lower() in EXCLUDE_SUFFIXES:
        return True
    return False


def _read_version() -> str:
    pkg_xml = ADDON_DIR / "package.xml"
    if pkg_xml.exists():
        text = pkg_xml.read_text(encoding="utf-8")
        m = re.search(r"<version>(.*?)</version>", text)
        if m:
            return m.group(1).strip()
    return "0.0.0"


def build(out_dir: Path) -> Path:
    version = _read_version()
    zip_name = f"PDFVectorImporter_v{version}.zip"
    zip_path = out_dir / zip_name

    out_dir.mkdir(parents=True, exist_ok=True)

    file_count = 0
    skipped = 0

    with zipfile.ZipFile(zip_path, "w", compression=zipfile.ZIP_DEFLATED) as zf:
        for abs_path in sorted(ADDON_DIR.rglob("*")):
            if not abs_path.is_file():
                continue
            rel = abs_path.relative_to(ADDON_DIR)
            if _should_exclude(rel):
                skipped += 1
                continue
            # Archive path: PDFVectorImporter/<rel>
            arc_name = Path("PDFVectorImporter") / rel
            zf.write(abs_path, arc_name)
            file_count += 1

    print(f"Built: {zip_path}")
    print(f"  {file_count} files included, {skipped} excluded")
    return zip_path


def main() -> None:
    parser = argparse.ArgumentParser(description="Build PDFVectorImporter release zip")
    parser.add_argument(
        "--out", default=str(REPO_ROOT),
        help="Output directory (default: repo root)"
    )
    args = parser.parse_args()

    out_dir = Path(args.out).resolve()
    zip_path = build(out_dir)
    print(f"\nRelease ready: {zip_path}")


if __name__ == "__main__":
    main()
```

### build_windows_installer.py

- Path: `build_windows_installer.py`
- Size: `3.71 KB`
- Modified: `2026-03-31 16:09:42`

```python
#!/usr/bin/env python3
"""Build a Windows Setup.exe installer for PDFVectorImporter using Inno Setup."""

from __future__ import annotations

import argparse
import os
import re
import shutil
import subprocess
import sys
import zipfile
from pathlib import Path

import build_release


REPO_ROOT = Path(__file__).parent.resolve()
ADDON_DIR = REPO_ROOT / "PDFVectorImporter"
DIST_DIR = REPO_ROOT / "dist"
STAGE_DIR = DIST_DIR / "installer_stage"
INNO_SCRIPT = REPO_ROOT / "installer" / "PDFVectorImporter.iss"


def read_version() -> str:
    package_xml = ADDON_DIR / "package.xml"
    if not package_xml.exists():
        raise FileNotFoundError(f"Missing package metadata: {package_xml}")

    text = package_xml.read_text(encoding="utf-8")
    match = re.search(r"<version>(.*?)</version>", text)
    if not match:
        raise RuntimeError("Could not determine version from package.xml")
    return match.group(1).strip()


def find_iscc(explicit_path: str | None) -> Path:
    candidates: list[Path] = []

    if explicit_path:
        candidates.append(Path(explicit_path))

    for name in ("iscc", "ISCC.exe"):
        on_path = shutil.which(name)
        if on_path:
            candidates.append(Path(on_path))

    for env_var in ("ProgramFiles", "ProgramFiles(x86)"):
        root = os.environ.get(env_var)
        if not root:
            continue
        base = Path(root)
        candidates.append(base / "Inno Setup 6" / "ISCC.exe")
        candidates.append(base / "Inno Setup 5" / "ISCC.exe")

    for candidate in candidates:
        if candidate.exists():
            return candidate.resolve()

    raise FileNotFoundError(
        "Inno Setup compiler (ISCC.exe) was not found.\n"
        "Install Inno Setup 6 from https://jrsoftware.org/isinfo.php "
        "or pass --iscc C:\\path\\to\\ISCC.exe."
    )


def stage_release() -> tuple[str, Path, Path]:
    version = read_version()
    DIST_DIR.mkdir(parents=True, exist_ok=True)

    zip_path = build_release.build(DIST_DIR)

    if STAGE_DIR.exists():
        shutil.rmtree(STAGE_DIR)
    STAGE_DIR.mkdir(parents=True, exist_ok=True)

    with zipfile.ZipFile(zip_path, "r") as zf:
        zf.extractall(STAGE_DIR)

    source_dir = STAGE_DIR / "PDFVectorImporter"
    if not source_dir.is_dir():
        raise RuntimeError(f"Expected staged addon folder at {source_dir}")

    return version, source_dir, zip_path


def compile_installer(iscc: Path, version: str, source_dir: Path) -> Path:
    cmd = [
        str(iscc),
        str(INNO_SCRIPT),
        f"/DMyAppVersion={version}",
        f"/DSourceDir={source_dir}",
    ]
    print("Running:", " ".join(cmd))
    subprocess.run(cmd, check=True, cwd=REPO_ROOT)

    installer_exe = DIST_DIR / f"PDFVectorImporter_Setup_v{version}.exe"
    if not installer_exe.exists():
        raise RuntimeError(
            "Inno Setup completed but installer was not found at "
            f"{installer_exe}"
        )
    return installer_exe


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Build PDFVectorImporter Windows installer (.exe)"
    )
    parser.add_argument(
        "--iscc",
        default=None,
        help="Path to ISCC.exe (Inno Setup compiler). Optional if ISCC is on PATH.",
    )
    args = parser.parse_args()

    version, source_dir, zip_path = stage_release()
    iscc = find_iscc(args.iscc)
    installer_exe = compile_installer(iscc, version, source_dir)

    print("")
    print(f"Release zip: {zip_path}")
    print(f"Installer:   {installer_exe}")
    print(f"Stage dir:   {source_dir}")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:  # pragma: no cover - entrypoint safety
        print(f"ERROR: {exc}", file=sys.stderr)
        raise SystemExit(1)
```

## Navigation Call-Site Inventory

```text
PDFVectorImporter/InitGui.py:88: FreeCADGui.addCommand("ImportPDFVector", ImportPDFVectorCommand())
PDFVectorImporter/InitGui.py:94: FreeCADGui.addCommand("PDF_ScaleByReference", ScaleByReferenceCommand())
PDFVectorImporter/InitGui.py:95: FreeCADGui.addCommand("PDF_QuickScale", QuickScaleCommand())
PDFVectorImporter/InitGui.py:106: FreeCADGui.addCommand("PDF_CheckEnv", CheckEnvironmentCommand())
PDFVectorImporter/InitGui.py:107: FreeCADGui.addCommand("PDF_ImportViaConsole", ImportViaConsoleCommand())
PDFVectorImporter/InitGui.py:108: FreeCADGui.addCommand("PDF_BatchImport", BatchImportCommand())
PDFVectorImporter/InitGui.py:109: FreeCADGui.addCommand("PDF_InstallPyMuPDF", InstallPyMuPDFCommand())
```

## Optional Checks

Checks were not run. Use `--run-checks` to capture configured command output.

## Exclusion / Skip Report

### Excluded Directory

- Count: 5

```text
PDFVectorImporter/__pycache__
PDFVectorImporter/adapters/__pycache__
PDFVectorImporter/pdfcadcore/__pycache__
PDFVectorImporter/src/__pycache__
tests/__pycache__
```

### Non Text Or Unlisted Extension

- Count: 10

```text
PDFVectorImporter/.gitignore
PDFVectorImporter/LICENSE
PDFVectorImporter/PDF with embedded images.pdf
PDFVectorImporter/qa_results.csv
PDFVectorImporter/qa_runs/cross_platform_20260403/bl_results.csv
PDFVectorImporter/qa_runs/cross_platform_20260403/lc_results.csv
PDFVectorImporter/qa_runs/cross_platform_20260403/qa_cross_platform.xlsx
PDFVectorImporter/qa_runs/cross_platform_20260403/qa_cross_platform_bl.xlsx
PDFVectorImporter/qa_runs/cross_platform_20260403/qa_cross_platform_lc.xlsx
installer/PDFVectorImporter.iss
```

## End of Pack

Context pack completed.
