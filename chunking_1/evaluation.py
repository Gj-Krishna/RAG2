from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import Qdrant
import numpy as np

def evaluate_strategy(strategy_name, strategy_function, text, hf, vector_store, query_text, top_k):
    # Chunk the text using the given strategy
    chunks = strategy_function(text)
    
    # Get embeddings for the chunks
    chunk_embeddings = hf.embed_documents(chunks)
    
    # Add chunks and their embeddings to Qdrant
    vector_store.add_documents(chunks, chunk_embeddings)
    
    # Get embedding for the query
    query_embedding = hf.embed_query(query_text)
    
    # Retrieve the top_k relevant chunks from Qdrant
    results = vector_store.similarity_search(query_embedding, k=top_k)
    
    print(f"Strategy: {strategy_name}")
    print(f"Query: {query_text}\n")
    
    # Print top_k results with similarity scores
    for i, (chunk, score) in enumerate(results):
        print(f"Rank {i + 1}:")
        print(f"Chunk: {chunk}")
        print(f"Similarity Score: {score:.4f}")
        print("-" * 20)
