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



