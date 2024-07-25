def fixed_size_chunks(text, chunk_size=1000):
    return [text[i:i + chunk_size] for i in range(0, len(text), chunk_size)]

if __name__ == "__main__":
    with open("extracted_text.txt", "r") as file:
        text_data = file.read()
    chunks = fixed_size_chunks(text_data)
    with open("fixed_size_chunks.txt", "w") as file:
        file.write("\n\n".join(chunks))
