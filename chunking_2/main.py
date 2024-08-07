from extraction import extract_text_from_pdf,combine_text_and_tables
from character_text_splitter import character_splitter
from sentence_splitter import sentence_splitter
from paragraph_splitter import paragraph_splitter
from recursive_character_splitter import recursive_splitter
from markdown_text_splitter import markdown_splitter
from semantic_splitter import semantic_splitter



pdf_path = "Policies\Text\Relocation Policy.pdf"
extracted_text = extract_text_from_pdf(pdf_path)
combined_data = combine_text_and_tables(pdf_path)

character_chunks = character_splitter(combined_data)
sentence_chunks = sentence_splitter(combined_data)
paragraph_chunks = paragraph_splitter(combined_data)
recursive_chunks = recursive_splitter(combined_data)
markdown_chunks = markdown_splitter(combined_data)
semantic_chunks = semantic_splitter(combined_data)
