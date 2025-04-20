
def run_pipeline(pdf_path: str, output_format: str = "excel"):
    pdf_type, content = preprocess(pdf_path)
    structured_data = extract(content, pdf_type)
    export(structured_data, output_format)