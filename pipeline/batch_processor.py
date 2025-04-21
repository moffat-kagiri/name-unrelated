import os
from multiprocessing import Pool, cpu_count
from typing import List
from src.preprocessing.pdf_to_image import convert_pdf_to_images
from src.extraction.layout_analysis import detect_layout_elements
from src.postprocessing.structure_data import to_structured_table
from src.utils.logger import setup_logger
import pandas as pd
import numpy as np
from tqdm import tqdm

logger = setup_logger("batch_processor")

def process_single_pdf(pdf_path: str, output_dir: str) -> None:
    """Process one PDF and save results to output_dir."""
    try:
        # 1. Convert PDF to images (handles scanned/handwritten)
        images = convert_pdf_to_images(pdf_path)
        
        # 2. Extract and structure data
        all_data = []
        for img in images:
            img_np = np.array(img)  # Convert PIL to OpenCV format
            del img  # Free memory immediately
            layout = detect_layout_elements(img_np)
            structured_data = to_structured_table(layout)
            all_data.append(structured_data)
        
        # 3. Save output
        output_path = os.path.join(output_dir, f"{os.path.basename(pdf_path)}_output.xlsx")
        pd.concat(all_data).to_excel(output_path, index=False)
        logger.info(f"Processed {pdf_path} -> {output_path}")

    except Exception as e:
        logger.error(f"Failed to process {pdf_path}: {str(e)}")

def process_batch(pdf_paths: List[str], output_dir: str, workers: int = None) -> None:
    """Parallel processing of multiple PDFs."""
    workers = workers or max(1, cpu_count() - 1)  # Leave 1 core free
    os.makedirs(output_dir, exist_ok=True)
    with Pool(processes=workers) as pool:
        list(tqdm(
            pool.imap_unordered(
                lambda x: process_single_pdf(*x),
                [(pdf, output_dir) for pdf in pdf_paths]
            ),
            total=len(pdf_paths),
            desc="Processing PDFs"
        ))