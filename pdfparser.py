import fitz  # PyMuPDF

def extract_text_from_pdf(pdf_file):
    """
    Extract text from a PDF file uploaded as a BytesIO stream (e.g., Streamlit uploader).

    Args:
        pdf_file: file-like object (BytesIO) representing the PDF file.

    Returns:
        Extracted text as a string.
    """
    try:
        doc = fitz.open(stream=pdf_file.read(), filetype="pdf")
        text = ""
        for page in doc:
            text += page.get_text()
        return text.strip()
    except Exception as e:
        # You can log the error or return a friendly message
        return ""
