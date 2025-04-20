# -*- coding: utf-8 -*-
import argparse
from src.preprocessing.pdf_to_image import convert_pdf
from src.extraction.layout_analysis import detect_layout
from src.postprocessing.structure_data import to_excel

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=str, required=True)
    parser.add_argument("--output", type=str, default="output.xlsx")
    args = parser.parse_args()

    # Pipeline
    images = convert_pdf(args.input)
    structured_data = detect_layout(images)
    to_excel(structured_data, args.output)

if __name__ == "__main__":
    main()