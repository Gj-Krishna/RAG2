from qdrant_client import QdrantClient
from qdrant_client.http.models import Distance, VectorParams
import numpy as np

def save_embeddings(embeddings):
    client = QdrantClient(":memory:")
    client.create_collection(
        collection_name="demo_collection",
        vectors_config=VectorParams(size=1024, distance=Distance.COSINE),
    )

    # Prepare data for insertion
    for strategy, vectors in embeddings.items():
        points = [
            {
                "id": str(i),  # Unique ID for each vector
                "vector": vector
            }
            for i, vector in enumerate(vectors)
        ]
        client.upsert(
            collection_name="demo_collection",
            points=points
        )
