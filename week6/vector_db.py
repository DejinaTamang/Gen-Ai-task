from sentence_transformers import SentenceTransformer
import faiss

model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

dimension = model.get_sentence_embedding_dimension()

print("Embedding dimension:", dimension)

index = faiss.IndexFlatL2(dimension)

print("FAISS index created successfully")