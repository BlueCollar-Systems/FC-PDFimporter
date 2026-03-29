import sys
sys.path.insert(0, r"C:\Users\Rowdy Payton\AppData\Roaming\FreeCAD\Mod\PDFVectorImporter\src")
sys.path.insert(0, r"C:\Users\Rowdy Payton\AppData\Roaming\FreeCAD\Mod\PDFVectorImporter\src\lib")
import fitz
import PDFImporterCore as core
print('fitz_version=', (getattr(fitz,'__doc__','').splitlines()[0] if getattr(fitz,'__doc__',None) else 'unknown'))
doc = fitz.open(r"C:\Users\Rowdy Payton\Downloads\Alvord TX — Garden Plan · Final.pdf")
for p in [5,6,7]:
    pg = doc.load_page(p-1)
    d = pg.get_drawings()
    stats = core._vector_group_stats(d, page_area=pg.rect.width*pg.rect.height)
    print('page', p, 'n', len(d), 'fill_only_ratio', round(stats['fill_only_ratio'],3), 'stroke_ratio', round(stats['stroke_ratio'],3), 'max_rect_ratio', round(stats['max_rect_ratio'],4), 'fill_art=', core._looks_like_fill_art_flood(len(d), stats))
