def chunk_text(text, chunk_size=150):
    words = text.split()
    chunks = []
    current_chunk = ""
    
    for word in words:
        if len(current_chunk) + len(word) + 1 <= chunk_size:
            current_chunk += word + " "
        else:
            chunks.append(current_chunk.strip())
            current_chunk = word + " "
    
    if current_chunk:
        chunks.append(current_chunk.strip())

    return chunks


with open("week6/document.txt", "r", encoding="utf-8") as file:
    text = file.read()

chunks = chunk_text(text)

for i, chunk in enumerate(chunks):
    print(f"\nChunk {i}:")
    print(chunk)