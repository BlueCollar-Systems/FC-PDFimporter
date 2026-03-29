import sys
sys.path.insert(0, r"C:\Users\Rowdy Payton\AppData\Roaming\FreeCAD\Mod\PDFVectorImporter\src")
sys.path.insert(0, r"C:\Users\Rowdy Payton\AppData\Roaming\FreeCAD\Mod\PDFVectorImporter\src\lib")
import PDFImporterCore as core
opts = core.ImportOptions(pages=[1,2,3,4], import_mode='auto', verbose=True, import_text=True, text_mode='labels', ignore_images=True)
core.import_pdf(r"C:\Users\Rowdy Payton\Downloads\alvord_garden_map_PRINT.pdf", opts)
print('done')
