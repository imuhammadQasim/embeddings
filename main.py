# from sentence_transformers import SentenceTransformer

# # Ek chota aur fast model load karo
# model = SentenceTransformer('all-MiniLM-L6-v2')

# # Apne text ko vector mein convert karo
# sentences = ["AI bohot mazaidar cheez hai", "Machine learning seekhna asan hai"]
# sentences1 = ["Mujhe coding pasand hai Mera programming mein interest hai"]
# embeddings = model.encode(sentences)
# embeddings2 = model.encode(sentences)

# print(embeddings[0])


from sentence_transformers.util import cos_sim
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

sentences = [
    "I love programming in Python",
    "Python is my favorite programming language",
    "I bought a football yesterday"
]

embeddings = model.encode(sentences)
similarity = cos_sim(
    embeddings[0],
    embeddings[2]
)

print(similarity)
print(embeddings.shape)