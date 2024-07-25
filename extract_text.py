import fitz  # PyMuPDF

def extract_text_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    text = ""
    for page in doc:
        text += page.get_text()
    return text

if __name__ == "__main__":
    pdf_path = "your_pdf_path.pdf"
    text_data = extract_text_from_pdf(pdf_path)
    with open("extracted_text.txt", "w") as file:
        file.write(text_data)
