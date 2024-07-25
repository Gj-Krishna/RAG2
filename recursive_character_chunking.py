from langchain.text_splitter import RecursiveCharacterTextSplitter

def recursive_character_chunks(text, chunk_size=1000, overlap=100):
    splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=overlap)
    return splitter.split_text(text)

if __name__ == "__main__":
    with open("extracted_text.txt", "r") as file:
        text_data = file.read()
    chunks = recursive_character_chunks(text_data)
    with open("recursive_character_chunks.txt", "w") as file:
        file.write("\n\n".join(chunks))
