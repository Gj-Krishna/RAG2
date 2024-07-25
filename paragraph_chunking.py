from langchain.text_splitter import ParagraphTextSplitter

def paragraph_chunks(text):
    splitter = ParagraphTextSplitter()
    return splitter.split_text(text)

if __name__ == "__main__":
    with open("extracted_text.txt", "r") as file:
        text_data = file.read()
    chunks = paragraph_chunks(text_data)
    with open("paragraph_chunks.txt", "w") as file:
        file.write("\n\n".join(chunks))
