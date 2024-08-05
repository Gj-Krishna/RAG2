from langchain.text_splitter import SemanticTextSplitter
import argparse
import fitz  # PyMuPDF

def extract_text_from_pdf(file_path):
    text = ""
    with fitz.open(file_path) as doc:
        for page in doc:
            text += page.get_text()
    return text

def semantic_splitter(text, chunk_size=500):
    splitter = SemanticTextSplitter(chunk_size=chunk_size)
    return splitter.split_text(text)

def main():
    parser = argparse.ArgumentParser(description="Semantic chunking from PDF")
    parser.add_argument("pdf_file", type=str, help="Path to the PDF file to chunk")
    args = parser.parse_args()

    text = extract_text_from_pdf(args.pdf_file)
    chunks = semantic_splitter(text)
    
    for i, chunk in enumerate(chunks):
        print(f"Chunk {i + 1}:")
        print(chunk)
        print("-" * 20)

if __name__ == "__main__":
    main()
