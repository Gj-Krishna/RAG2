from extraction import extract_text_from_pdf, combine_text_and_tables
from character_text_splitter import character_splitter
from sentence_splitter import sentence_splitter
from paragraph_splitter import paragraph_splitter
from recursive_character_splitter import recursive_splitter
from markdown_text_splitter import markdown_splitter
from semantic_text_splitter import semantic_splitter

from create_embeddings import create_embeddings
from save_embeddings import save_embeddings
from evaluate_chunks import evaluate_chunks

pdf_path = "Policies/Text/Relocation Policy.pdf"
extracted_text = extract_text_from_pdf(pdf_path)
combined_data = combine_text_and_tables(pdf_path)

# Chunking strategies
chunking_strategies = {
    "character": character_splitter(combined_data),
    "sentence": sentence_splitter(combined_data),
    "paragraph": paragraph_splitter(combined_data),
    "recursive": recursive_splitter(combined_data),
    "markdown": markdown_splitter(combined_data),
    "semantic": semantic_splitter(combined_data)
}

# Create embeddings
embeddings = create_embeddings(chunking_strategies)

# Save embeddings to Qdrant
save_embeddings(embeddings)

# Query for evaluation
query = "Your query here"
results = evaluate_chunks(query)

# Print evaluation results
print("Evaluation Results:")
for doc, score in results:
    print(f"Score: {score:.4f}")
    print(f"Text: {doc.page_content}")
    print("---")
