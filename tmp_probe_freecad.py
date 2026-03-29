import sys
sys.path.insert(0, r"C:\Users\Rowdy Payton\AppData\Roaming\FreeCAD\Mod\PDFVectorImporter\src")
sys.path.insert(0, r"C:\Users\Rowdy Payton\AppData\Roaming\FreeCAD\Mod\PDFVectorImporter\src\lib")
import PDFImporterCore as core
print('CORE_OK', core.AUTO_FILL_PURE_MIN_GROUPS, core.AUTO_FILL_PURE_RATIO)
print('DESC_TEST', core._effective_descender('TOTAL WEIGHT THIS DRAWING', -0.209))
