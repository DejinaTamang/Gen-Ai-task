from sentence_transformers import SentenceTransformer

# Load the embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Some example sentences
sentences = [
    "Python is used for machine learning.",
    "Neural networks can learn complex patterns.",
    "The weather is sunny today.",
    "I enjoy eating pizza.",
    "Deep learning is a part of artificial intelligence."
]

# Generate embeddings
embeddings = model.encode(sentences)

print("Number of sentences:", len(sentences))
print("Embedding shape:", embeddings.shape)