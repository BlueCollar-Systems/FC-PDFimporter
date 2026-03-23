# PDF Vector Importer for FreeCAD

**BUILT. NOT BOUGHT.**

![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)
![Version: 3.5.0](https://img.shields.io/badge/Version-3.5.0-blue.svg)
![Platform: FreeCAD 0.20+](https://img.shields.io/badge/Platform-FreeCAD%200.20%2B-orange.svg)

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

- **FreeCAD** 0.20 or later
- **Python** 3.8+
- **PyMuPDF** (automatically installed via Addon Manager)

## License

MIT License — see [LICENSE](LICENSE) for details.

Copyright (c) 2024-2026 BlueCollar Systems
