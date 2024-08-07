from langchain_huggingface import HuggingFaceEmbeddings
from langchain_qdrant import Qdrant
import numpy as np

def evaluate_similarity(query_text, qdrant, top_n=5):
    model_name = "BAAI/bge-large-en-v1.5"
    embedding_model = HuggingFaceEmbeddings(model_name=model_name)
    
    # Embed the query
    query_embedding = embedding_model.embed(query_text)
    
    # Retrieve and rank documents based on similarity
    results = qdrant.search(query_embedding, top_n=top_n)
    top_chunks = results['documents']
    top_scores = results['scores']
    
    return top_chunks, top_scores
