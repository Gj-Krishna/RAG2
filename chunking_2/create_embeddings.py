from langchain_community.embeddings import HuggingFaceBgeEmbeddings

def create_embeddings(chunking_strategies):
    model_name = "BAAI/bge-large-en-v1.5"
    hf_embeddings = HuggingFaceBgeEmbeddings(
        model_name=model_name,
        model_kwargs={"device": "cpu"},
        encode_kwargs={"normalize_embeddings": True}
    )

    embeddings = {}
    for strategy, chunks in chunking_strategies.items():
        embeddings[strategy] = hf_embeddings.embed_documents(chunks)

    return embeddings
