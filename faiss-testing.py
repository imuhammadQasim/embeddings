from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

model = SentenceTransformer("all-MiniLM-L6-v2")

documents = [
    "Python is a programming language",
    "FastAPI is a Python web framework",
    "React is a JavaScript frontend library",
    "PostgreSQL is a relational database",
    "Docker is used for containerization"
]

embeddings = model.encode(documents)

embeddings = np.array(embeddings).astype("float32")

print(embeddings.shape)

dimension = embeddings.shape[1]

index = faiss.IndexFlatL2(dimension)
index.add(embeddings)
print(index.ntotal)

query = "Python backend framework"

query_embedding = model.encode([query])

query_embedding = np.array(query_embedding).astype("float32")

distances, indices = index.search(query_embedding, k=2)

for distance, idx in zip(distances[0], indices[0]):
    print(documents[idx], distance)