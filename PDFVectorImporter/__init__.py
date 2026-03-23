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

for _p in (_src, _lib):
    if os.path.isdir(_p) and _p not in sys.path:
        sys.path.insert(0, _p)



