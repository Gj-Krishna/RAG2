import re
from langchain.text_splitter import CharacterTextSplitter
import argparse
import fitz  # PyMuPDF

def extract_text_from_pdf(file_path):
    text = ""
    with fitz.open(file_path) as doc:
        for page in doc:
            text += page.get_text()
    return text

def markdown_splitter(text):
    # Split text based on Markdown headers
    chunks = re.split(r'\n##+ ', text)
    # Remove empty chunks and any trailing newlines
    chunks = [chunk.strip() for chunk in chunks if chunk.strip()]
    return chunks

def main():
    parser = argparse.ArgumentParser(description="Specialized Markdown chunking from PDF")
    parser.add_argument("pdf_file", type=str, help="Path to the PDF file to chunk")
    args = parser.parse_args()

    text = extract_text_from_pdf(args.pdf_file)
    chunks = markdown_splitter(text)
    
    for i, chunk in enumerate(chunks):
        print(f"Chunk {i + 1}:")
        print(chunk)
        print("-" * 20)

if __name__ == "__main__":
    main()
