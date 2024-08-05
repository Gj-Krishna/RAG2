from langchain.vectorstores import Qdrant

def setup_qdrant_collection(collection_name, embedding_dim):
    # Initialize Qdrant client
    client = Qdrant(collection_name=collection_name, embedding_dim=embedding_dim)
    return client

def get_vector_store(client, collection_name, embeddings):
    # Get the vector store
    return client
