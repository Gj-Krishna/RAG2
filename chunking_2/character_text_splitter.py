from langchain.text_splitter import CharacterTextSplitter
from extraction import extract_text_from_pdf, combine_text_and_tables

def character_splitter(text):
    splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=100, separator="")
    chunks = splitter.split_text(text)
    return chunks

if __name__ == "__main__":
    pdf_path = "Policies/Text/Relocation Policy.pdf" 
    
    extracted_text = extract_text_from_pdf(pdf_path)
    combined_data = combine_text_and_tables(extracted_text)

    chunks = character_splitter(combined_data)

    with open('character_chunks.txt', 'w') as file:
        for i, chunk in enumerate(chunks, start=1):
            file.write(f"Chunk {i}:\n\n{chunk}\n\n")