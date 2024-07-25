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
    query = "text extraction and chunking strategies"

    with open("evaluation_results.txt", "w") as eval_file:
        eval_file.write(f"Query: {query}\n\n")

        for strategy in ["fixed_size_chunks.txt", "semantic_chunks.txt", "sentence_chunks.txt", "paragraph_chunks.txt", "recursive_character_chunks.txt"]:
            with open(strategy, "r") as file:
                chunks = file.read().split("Chunk:\n")[1:]
                similarities = [(chunk, get_similarity(query, chunk.strip())) for chunk in chunks]
                best_chunk, best_score = max(similarities, key=lambda x: x[1])

                eval_file.write(f"Evaluation for {strategy}:\n")
                eval_file.write(f"Best Score: {best_score}\nBest Chunk:\n{best_chunk}\n\n")
