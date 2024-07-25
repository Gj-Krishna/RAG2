from transformers import pipeline
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

def get_similarity(query, chunk):
    model_name = "bert-base-uncased"
    similarity_model = pipeline("feature-extraction", model=model_name)

    query_embedding = np.mean(similarity_model(query), axis=0)
    chunk_embedding = np.mean(similarity_model(chunk), axis=0)

    similarity_score = cosine_similarity([query_embedding], [chunk_embedding])
    return similarity_score[0][0]

if __name__ == "__main__":
    query = "Your query here"

    # Example usage with fixed size chunks
    with open("fixed_size_chunks.txt", "r") as file:
        chunks = file.read().split("\n\n")

    similarities = [(chunk, get_similarity(query, chunk)) for chunk in chunks]
    similarities.sort(key=lambda x: x[1], reverse=True)

    with open("evaluation_results.txt", "w") as file:
        for chunk, score in similarities[:5]:
            file.write(f"Score: {score}\nChunk:\n{chunk}\n\n")
