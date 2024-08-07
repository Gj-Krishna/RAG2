from langchain_huggingface import HuggingFaceEmbeddings
from langchain_qdrant import Qdrant

def create_embeddings(chunks, model_name="BAAI/bge-large-en-v1.5"):
    embedding_model = HuggingFaceEmbeddings(model_name=model_name)
    qdrant = Qdrant()

    # Create embeddings for each chunk
    embeddings = [embedding_model.embed(chunk) for chunk in chunks]
    
    # Store embeddings in Qdrant
    for i, emb in enumerate(embeddings):
        qdrant.add_document(id=i, embedding=emb)
    
    return qdrant
