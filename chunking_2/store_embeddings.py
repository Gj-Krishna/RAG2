from embedding_creation import create_embeddings
from extraction import extract_text_from_pdf, combine_text_and_tables
from character_text_splitter import character_splitter
from sentence_splitter import sentence_splitter
from paragraph_splitter import paragraph_splitter
from recursive_character_splitter import recursive_splitter
from markdown_text_splitter import markdown_splitter
from semantic_text_splitter import semantic_splitter

def store_all_embeddings(pdf_path):
    extracted_text = extract_text_from_pdf(pdf_path)
    combined_data = combine_text_and_tables(extracted_text)

    # Create and store embeddings for each strategy
    strategies = {
        "Character Splitter": character_splitter,
        "Sentence Splitter": sentence_splitter,
        "Paragraph Splitter": paragraph_splitter,
        "Recursive Splitter": recursive_splitter,
        "Markdown Splitter": markdown_splitter,
        "Semantic Splitter": semantic_splitter
    }

    for strategy_name, strategy_function in strategies.items():
        chunks = strategy_function(combined_data)
        create_embeddings(chunks)

if __name__ == "__main__":
    pdf_path = "Policies/Text/Relocation Policy.pdf"
    store_all_embeddings(pdf_path)
