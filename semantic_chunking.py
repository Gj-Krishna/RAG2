from langchain.text_splitter import SemanticTextSplitter

def semantic_chunks(text):
    splitter = SemanticTextSplitter()
    return splitter.split_text(text)

if __name__ == "__main__":
    with open("extracted_text.txt", "r") as file:
        text_data = file.read()
    chunks = semantic_chunks(text_data)
    with open("semantic_chunks.txt", "w") as file:
        file.write("\n\n".join(chunks))
