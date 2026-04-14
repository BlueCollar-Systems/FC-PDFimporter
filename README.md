# PDF Vector Importer for FreeCAD

**BUILT. NOT BOUGHT.**

![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)
![Version: 4.0.8](https://img.shields.io/badge/Version-4.0.8-blue.svg)
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
   pip install "PyMuPDF>=1.24,<2.0"
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

## Compatibility

| FreeCAD Version | Python | PyMuPDF | Status |
|----------------|--------|---------|--------|
| 0.21.x | 3.10+ | >=1.24,<2.0 | ⚠️ Expected |
| 1.0.x | 3.11+ | >=1.24,<2.0 | ⚠️ Expected |
| 1.1.x | 3.11+ | >=1.24,<2.0 | ⚠️ Expected |
| 0.19–0.20 | 3.8–3.9 | legacy pin | ⚠️ Expected only after legacy branch testing |
| 0.18 and earlier | | | ❌ Not supported |

Evidence levels:
- `✅ Verified`: host-run validation evidence captured.
- `⚠️ Expected`: syntax/runtime compatible but no host-run evidence yet.
- `❌ Not supported`: outside maintained/tested compatibility scope.

## Requirements

- **FreeCAD** 0.21 or later
- **Python** 3.10+ (adapters use PEP 604 union types)
- **PyMuPDF** (automatically installed via Addon Manager)

## Known Limitations

| Limitation | Details |
|-----------|---------|
| Encrypted PDFs | Password-protected PDFs must be unlocked before import |
| Compression filters | Decoding is delegated to PyMuPDF. Malformed or non-standard compressed object streams may fail to parse |
| Raster-only scans | Pure raster PDFs produce no vector geometry |
| Clipped/XObject-heavy PDFs | Complex clip stacks and deeply nested form XObjects can produce partial geometry |
| Very large PDFs | Documents with >10,000 primitives may slow the import process |
| Embedded subset fonts | Text using embedded subset fonts may not render correctly |
| OCG layer assignment | Extractor-level OCG mapping is validated on corpus `layered_ocg.pdf`; FreeCAD host-run grouping verification is still required in target runtime |
| Legacy hosts | FreeCAD versions older than 0.21 are not part of current validation coverage |

## License

MIT License — see [LICENSE](LICENSE) for details.

Copyright (c) 2024-2026 BlueCollar Systems
