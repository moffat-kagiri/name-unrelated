FROM python:3.11-slim
RUN apt-get update && apt-get install -y \
    tesseract-ocr \
    poppler-utils \
    build-essential \
    python3-dev \
    && rm -rf /var/lib/apt/lists/*
COPY requirements.txt .
RUN pip install --no-cache-dir cython
RUN pip install --no-cache-dir -r requirements.txt
COPY . /app
WORKDIR /app
CMD ["python", "src/pipeline.py"]