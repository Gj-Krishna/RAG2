def paragraph_splitter(text):
    paragraphs = text.split('\n\n\n')
    return paragraphs

if __name__ == "__main__":
    with open('extracted_data.txt', 'r') as file:
        text = file.read()
    chunks = paragraph_splitter(text)

    if not chunks:
        print("No sentence chunks were created.")
    else:
        with open('paragraph.txt', 'w') as file:
            for i, chunk in enumerate(chunks, start=1):
                file.write(f"Chunk {i}:\n\n{chunk}\n\n")