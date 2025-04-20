# This script provides functions to analyze the layout of a document image and extract text using OCR.
# It uses the LayoutParser library for layout analysis and Tesseract for OCR.
from pdf2image import convert_from_path
import layoutparser as lp

def analyze_layout(image):
    model = lp.Detectron2LayoutModel("lp://PubLayNet/faster_rcnn_R_50_FPN_3x/config")
    layout = model.detect(image)
    return layout

def extract_text_with_ocr(image):
    import pytesseract
    return pytesseract.image_to_string(image)