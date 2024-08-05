import nltk
from langchain.text_splitter import SentenceTextSplitter
import argparse
import fitz  # PyMuPDF

nltk.download('punkt')

def extract_text_from_pdf(file_path):
    text = ""
    with fitz.open(file_path) as doc:
        for page in doc:
            text += page.get_text()
    return text

def sentence_splitter(text):
    splitter = SentenceTextSplitter()
    return splitter.split_text(text)

def main():
    parser = argparse.ArgumentParser(description="Sentence-based chunking from PDF")
    parser.add_argument("pdf_file", type=str, help="Path to the PDF file to chunk")
    args = parser.parse_args()

    text = extract_text_from_pdf(args.pdf_file)
    chunks = sentence_splitter(text)
    
    for i, chunk in enumerate(chunks):
        print(f"Chunk {i + 1}:")
        print(chunk)
        print("-" * 20)

if __name__ == "__main__":
    main()
