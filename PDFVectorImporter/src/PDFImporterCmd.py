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
        "Fast Preview":     dict(curve_step=2.0, join_tol=0.5,  detect_arcs=False, map_dashes=False, make_faces=False, text="No text",  hatch_mode="skip",   import_mode="auto",   cleanup_level="conservative"),
        "General Vector":   dict(curve_step=1.0, join_tol=0.2,  detect_arcs=False, map_dashes=False, make_faces=True,  text="Labels",   hatch_mode="import", import_mode="auto",   cleanup_level="balanced"),
        "Technical Drawing":dict(curve_step=0.5, join_tol=0.1,  detect_arcs=True,  map_dashes=True,  make_faces=True,  text="Labels",   hatch_mode="group",  import_mode="auto",   cleanup_level="balanced"),
        "Shop Drawing":     dict(curve_step=0.5, join_tol=0.1,  detect_arcs=True,  map_dashes=True,  make_faces=True,  text="Geometry", hatch_mode="group",  import_mode="auto",   cleanup_level="balanced"),
        "Raster + Vectors": dict(curve_step=0.5, join_tol=0.1,  detect_arcs=True,  map_dashes=True,  make_faces=True,  text="Labels",   hatch_mode="skip",   import_mode="hybrid", cleanup_level="balanced",      raster_dpi=200),
        "Raster Only":      dict(curve_step=1.0, join_tol=0.5,  detect_arcs=False, map_dashes=False, make_faces=False, text="No text",  hatch_mode="skip",   import_mode="raster", cleanup_level="conservative",  raster_dpi=300),
        "Max Fidelity":     dict(curve_step=0.2, join_tol=0.05, detect_arcs=True,  map_dashes=True,  make_faces=True,  text="Geometry", hatch_mode="import", import_mode="auto",   cleanup_level="aggressive"),
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
        form.addRow("Hatching:", self.hatch_combo)

        btns = QtWidgets.QDialogButtonBox(
            QtWidgets.QDialogButtonBox.Ok | QtWidgets.QDialogButtonBox.Cancel)
        btns.accepted.connect(self._validate_and_accept)
        btns.rejected.connect(self.reject)

        layout = QtWidgets.QVBoxLayout(self)
        layout.addLayout(form)
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
            scale = grp.GetFloat("LastScale", 0.0)
            if scale > 0:
                self.scale_spin.setValue(scale)
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
            grp.SetFloat("LastScale", self.scale_spin.value())
        except (AttributeError, RuntimeError, ValueError):
            pass

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

        return core.ImportOptions(
            pages=self._parse_pages(),
            scale_to_mm=False,
            user_scale=float(self.scale_spin.value()),
            flip_y=True,
            join_tol=preset["join_tol"],
            curve_step_mm=preset["curve_step"],
            make_faces=preset["make_faces"],
            import_text=import_text,
            text_mode=text_mode,
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
            # cleanup_level is a Phase 2 option — not yet in ImportOptions
        )


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



