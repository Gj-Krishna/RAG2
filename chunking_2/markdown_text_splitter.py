from langchain.text_splitter import MarkdownTextSplitter

def markdown_splitter(text):
    splitter = MarkdownTextSplitter(chunk_size=1000, chunk_overlap=0)
    documents = splitter.create_documents([text])
    chunks = [doc.page_content for doc in documents]
    return chunks

if __name__ == "__main__":
    with open('extracted_data.txt', 'r') as file:
        text = file.read()
    
    chunks = markdown_splitter(text)

    with open('markdown_chunks.txt', 'w') as file:
        for i, chunk in enumerate(chunks, start=1):
            file.write(f"Chunk {i}:\n\n{chunk}\n\n")
