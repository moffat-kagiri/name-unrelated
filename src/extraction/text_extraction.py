# -*- coding: utf-8 -*-
# This module extracts text from images using Tesseract or EasyOCR.
import pytesseract
from configs import load_ocr_config

def extract_text(image: np.ndarray, engine: str = "tesseract") -> str:
    """Extract text using Tesseract/EasyOCR."""
    config = load_ocr_config()
    if engine == "tesseract":
        return pytesseract.image_to_string(
            image, 
            lang=config["tesseract"]["languages"], 
            config=f'--psm {config["tesseract"]["psm"]}'
        )