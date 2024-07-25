import os
from extract_text import extract_text_from_pdf

def main():
    pdf_path = "your_pdf_path.pdf"
    text_data = extract_text_from_pdf(pdf_path)

    with open("extracted_text.txt", "w") as file:
        file.write(text_data)

    # Run chunking strategies
    os.system("python fixed_size_chunking.py")
    os.system("python semantic_chunking.py")
    os.system("python sentence_chunking.py")
    os.system("python paragraph_chunking.py")
    os.system("python recursive_character_chunking.py")

    # Run model evaluation
    os.system("python model_evaluation.py")

if __name__ == "__main__":
    main()
