from langchain.text_splitter import SentenceTextSplitter

def sentence_chunks(text):
    splitter = SentenceTextSplitter()
    return splitter.split_text(text)

if __name__ == "__main__":
    with open("extracted_text.txt", "r") as file:
        text_data = file.read()
    chunks = sentence_chunks(text_data)
    with open("sentence_chunks.txt", "w") as file:
        file.write("\n\n".join(chunks))
