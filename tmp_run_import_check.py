import sys
sys.path.insert(0, r"C:\Users\Rowdy Payton\AppData\Roaming\FreeCAD\Mod\PDFVectorImporter\src")
sys.path.insert(0, r"C:\Users\Rowdy Payton\AppData\Roaming\FreeCAD\Mod\PDFVectorImporter\src\lib")
import PDFImporterCore as core
opts = core.ImportOptions(pages=[1], import_mode='auto', verbose=True, import_text=True, text_mode='geometry', ignore_images=False)
core.import_pdf(r"C:\Users\Rowdy Payton\Downloads\Welding-Symbol-Chart OCR.pdf", opts)
print('done')
