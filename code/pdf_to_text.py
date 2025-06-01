import fitz  # PyMuPDF

def extract_text_from_pdf(pdf_path):
    """Converts text from pdf to a string

    Args:
        pdf_path (str): path to the pdf

    Returns:
        str: string of the pdf contents
    """
    text = ""
    with fitz.open(pdf_path) as doc:
        for page in doc:
            text += page.get_text()
    return text