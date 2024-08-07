from langchain_huggingface import HuggingFaceEmbeddings
from langchain_experimental.text_splitter import SemanticChunker

def semantic_splitter(text, model_name="BAAI/bge-large-en-v1.5"):
    embeddings = HuggingFaceEmbeddings(model_name=model_name)
    chunker = SemanticChunker(embeddings)
    documents = chunker.create_documents([text])
    chunks = [doc.page_content for doc in documents]
    return chunks

if __name__ == "__main__":
    with open('extracted_data.txt', 'r') as file:
        text = file.read()
    
    chunks = semantic_splitter(text)

    with open('semantic_chunks.txt', 'w') as file:
        for i, chunk in enumerate(chunks, start=1):
            file.write(f"Chunk {i}:\n\n{chunk}\n\n")
