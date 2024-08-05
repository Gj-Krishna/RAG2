import fitz  # PyMuPDF
import pdfplumber

def extract_text_from_pdf(file_path):
    text = ""
    with fitz.open(file_path) as doc:
        for page in doc:
            text += page.get_text()
    return text

def extract_tables_from_pdf(file_path):
    tables = []
    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            tables.extend(page.extract_tables())
    return tables

def combine_text_and_tables(text, tables):
    combined = text
    for table in tables:
        for row in table:
            combined += "\n" + ", ".join(row)
    return combined
