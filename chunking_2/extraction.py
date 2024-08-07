import fitz  # PyMuPDF

def extract_text_from_pdf(pdf_path):
    all_text = ""
    
    with fitz.open(pdf_path) as pdf:
        for page_num in range(len(pdf)):
            page = pdf.load_page(page_num)
            all_text += page.get_text()
    
    return all_text

# def extract_tables_from_pdf(pdf_path):
#     # Using pdfplumber for table extraction
#     import pdfplumber
#     all_tables = []
    
#     with pdfplumber.open(pdf_path) as pdf:
#         for page in pdf.pages:
#             tables = page.extract_tables()
#             for table in tables:
#                 all_tables.append(table)
    
#     return all_tables

# def combine_text_and_tables(text, tables):
#     combined_data = text
#     for table in tables:
#         combined_data += "\nTable:\n"
#         for row in table:
#             combined_data += "\t".join(row) + "\n"
#     return combined_data

def combine_text_and_tables(text):
    return text

if __name__ == "__main__":
    pdf_path = "Policies\Text\Relocation Policy.pdf"  # Hardcoded path to PDF file
    text = extract_text_from_pdf(pdf_path)
    combined_data = combine_text_and_tables(text)
    
    # Write the combined data to a text file
    with open('extracted_data.txt', 'w') as file:
        file.write(combined_data)