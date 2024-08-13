from langchain_qdrant import QdrantVectorStore
from qdrant_client import QdrantClient
from langchain_community.embeddings import HuggingFaceBgeEmbeddings

def evaluate_chunks(query):
    client = QdrantClient(":memory:")
    vector_store = QdrantVectorStore(
        client=client,
        collection_name="demo_collection",
        embedding=None  # We are directly storing embeddings
    )

    results = vector_store.similarity_search_with_score(query, k=3)
    
    return results
