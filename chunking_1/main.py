from extraction import extract_text_from_pdf
from chunking_fixed_size import fixed_size_splitter
from chunking_sentence import sentence_splitter
from chunking_paragraph import paragraph_splitter
from chunking_recursive_character import recursive_character_splitter
from chunking_semantic import semantic_splitter
from chunking_markdown import markdown_splitter
from embeddings import get_embeddings
from storage import setup_qdrant_collection, get_vector_store
from evaluation import evaluate_strategy

pdf_path = "sample.pdf"
query_text = "subject matter details"
top_k = 3  # Adjust based on your needs

# Extract text from PDF
pdf_text = extract_text_from_pdf(pdf_path)

# Set up Qdrant collection
collection_name = "pdf_chunks"
embedding_dim = 384  # for the 'sentence-transformers/all-MiniLM-L6-v2' model
client = setup_qdrant_collection(collection_name, embedding_dim)

# Get embeddings
hf = get_embeddings()

# Get vector store
vector_store = get_vector_store(client, collection_name, hf)

# Apply chunking strategies and evaluate
strategies = {
    "Fixed-size Chunking": fixed_size_splitter,
    "Sentence-based Chunking": sentence_splitter,
    "Paragraph-based Chunking": paragraph_splitter,
    "Recursive Character Chunking": recursive_character_splitter,
    "Semantic Chunking": semantic_splitter,
    "Specialized Markdown Chunking": markdown_splitter
}

for strategy_name, strategy_function in strategies.items():
    print(f"Evaluating {strategy_name}...\n")
    evaluate_strategy(strategy_name, strategy_function, pdf_text, hf, vector_store, query_text, top_k)
    print("=" * 40)
