import argparse
import os
from glob import glob
from pipeline.batch_processor import process_batch

from itertools import islice

def batched(iterable, batch_size=10):
    """Split PDFs into chunks to avoid overloading memory."""
    it = iter(iterable)
    while batch := list(islice(it, batch_size)):
        yield batch

def main():
    parser = argparse.ArgumentParser(description="Batch PDF Processor")
    parser.add_argument("--input", required=True, help="PDF files or directory")
    parser.add_argument("--output", default="./data/processed", help="Output directory")
    parser.add_argument("--workers", type=int, help="Number of parallel processes")
    args = parser.parse_args()

    # Resolve input paths
    if os.path.isdir(args.input):
        pdf_paths = glob(os.path.join(args.input, "*.pdf"))
    else:
        pdf_paths = glob(args.input)  # Supports wildcards (e.g., /data/*.pdf)


    # Usage:
    for batch in batched(pdf_paths, batch_size=20):
        process_batch(batch, args.output, args.workers)
        # Process each batch of PDFs

if __name__ == "__main__":
    main()