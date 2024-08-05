from langchain.embeddings import HuggingFaceEmbeddings

def get_embeddings():
    model_name = "sentence-transformers/all-MiniLM-L6-v2"  # Example model
    return HuggingFaceEmbeddings(model_name=model_name)
