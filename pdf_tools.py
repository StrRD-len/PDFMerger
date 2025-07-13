# pdf_tools.py

import fitz  # PyMuPDF

def unlock_pdf(input_path, output_path):
    """
    Unlocks a PDF file by re-saving it without restrictions.
    """
    try:
        doc = fitz.open(input_path)
        doc.save(output_path)
        doc.close()
        return True, f"Entsperrt: {output_path}"
    except Exception as e:
        return False, str(e)

def merge_pdfs(pdf_paths, output_path):
    """
    Merges multiple PDF files into a single PDF.
    """
    try:
        merged_doc = fitz.open()
        for path in pdf_paths:
            doc = fitz.open(path)
            merged_doc.insert_pdf(doc)
            doc.close()
        merged_doc.save(output_path)
        merged_doc.close()
        return True, f"Zusammengeführt: {output_path}"
    except Exception as e:
        return False, str(e)