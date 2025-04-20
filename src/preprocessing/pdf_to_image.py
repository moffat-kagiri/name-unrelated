# This script processes a PDF file to determine if it is text-based or scanned.
# It uses pdfplumber to check for text and pdf2image to convert scanned pages to images.
import pdfplumber
from pdf2image import convert_from_path

def process_pdf(pdf_path):
    # Check if PDF is text-based or scanned
    try:
        with pdfplumber.open(pdf_path) as pdf:
            text = pdf.pages[0].extract_text()
        if not text.strip():
            raise ValueError("Scanned PDF")
        return "text", [page.extract_text() for page in pdf.pages]
    except:
        # Convert scanned PDF to images
        images = convert_from_path(pdf_path)
        return "scanned", images