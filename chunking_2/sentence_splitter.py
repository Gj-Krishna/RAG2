import nltk
from nltk.tokenize import sent_tokenize

nltk.download('punkt')


def sentence_splitter(text):
    chunks = sent_tokenize(text)
    return chunks

if __name__ == "__main__":
    with open('extracted_data.txt', 'r') as file:
        text = file.read()
    chunks = sentence_splitter(text)

    if not chunks:
        print("No sentence chunks were created.")
    else:
        with open('sentence_chunks.txt', 'w') as file:
            for i, chunk in enumerate(chunks, start=1):
                file.write(f"Chunk {i}:\n\n{chunk}\n\n")