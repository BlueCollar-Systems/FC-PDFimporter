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
    import pymupdf as fitz  # PyMuPDF >= 1.24 preferred name
except ImportError:
    try:
        import fitz  # Legacy fallback
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

        self.page_arrangement_combo = QtWidgets.QComboBox()
        self.page_arrangement_combo.addItems([
            "Spread (20% gap)",
            "Compact gap",
            "Touching pages",
            "Overlay pages",
        ])
        self.page_arrangement_combo.setCurrentText("Spread (20% gap)")
        self.page_arrangement_combo.setToolTip(
            "How multi-page imports are laid out in model space.\n"
            "Spread (20% gap) keeps pages readable by default."
        )

        self.page_gap_spin = QtWidgets.QDoubleSpinBox()
        self.page_gap_spin.setDecimals(2)
        self.page_gap_spin.setSingleStep(0.05)
        self.page_gap_spin.setRange(0.0, 1.0)
        self.page_gap_spin.setValue(0.20)
        self.page_gap_spin.setToolTip(
            "Gap ratio used for Compact gap mode (0.20 = 20% page break)."
        )

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
        adv_form.addRow("Page Layout:", self.page_arrangement_combo)
        adv_form.addRow("Compact Gap Ratio:", self.page_gap_spin)
        adv_group.setLayout(adv_form)

        # Hide/show advanced widgets when group is toggled
        adv_group.toggled.connect(lambda on: [
            w.setVisible(on) for w in (
                self.arc_mode_combo, self.cleanup_combo,
                self.lineweight_combo, self.grouping_combo,
                self.page_arrangement_combo, self.page_gap_spin)])
        # Start collapsed — hide the inner widgets
        for w in (self.arc_mode_combo, self.cleanup_combo,
                  self.lineweight_combo, self.grouping_combo,
                  self.page_arrangement_combo, self.page_gap_spin):
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
            page_arrangement = grp.GetString("LastPageArrangement", "")
            if page_arrangement:
                self.page_arrangement_combo.setCurrentText(page_arrangement)
            page_gap = grp.GetFloat("LastPageGapRatio", -1.0)
            if page_gap >= 0.0:
                self.page_gap_spin.setValue(page_gap)
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
            grp.SetString("LastPageArrangement", self.page_arrangement_combo.currentText())
            grp.SetFloat("LastPageGapRatio", self.page_gap_spin.value())
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
    _PAGE_ARRANGEMENT_MAP = {
        "spread": "Spread (20% gap)",
        "compact": "Compact gap",
        "touch": "Touching pages",
        "overlay": "Overlay pages",
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
            if "page_arrangement" in preset:
                self.page_arrangement_combo.setCurrentText(
                    self._PAGE_ARRANGEMENT_MAP.get(preset["page_arrangement"], "Spread (20% gap)"))
            if "page_gap_ratio" in preset:
                try:
                    self.page_gap_spin.setValue(float(preset["page_gap_ratio"]))
                except (TypeError, ValueError):
                    self.page_gap_spin.setValue(0.20)

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
        _arr_rev = {v: k for k, v in self._PAGE_ARRANGEMENT_MAP.items()}

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
            page_arrangement=_arr_rev.get(self.page_arrangement_combo.currentText(), "spread"),
            page_gap_ratio=float(self.page_gap_spin.value()),
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
            try:
                import pymupdf as fitz  # noqa: F811, F401  # PyMuPDF >= 1.24 preferred name
            except ImportError:
                import fitz  # noqa: F811, F401  # Legacy fallback
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



