from langchain.text_splitter import RecursiveCharacterTextSplitter

def recursive_splitter(text):
    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100, separators="")
    chunks = splitter.split_text(text)
    return chunks


if __name__ == "__main__":
    with open('extracted_data.txt', 'r') as file:
        text = file.read()
    chunks = recursive_splitter(text)

    with open('recursive_chunks.txt', 'w') as file:
        for i, chunk in enumerate(chunks, start=1):
            file.write(f"Chunk {i}:\n\n{chunk}\n\n")