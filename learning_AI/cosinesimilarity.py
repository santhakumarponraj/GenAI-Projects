from sentence_transformers import SentenceTransformer
import numpy as np

# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Documents
documents = [
    "Employees receive 20 days of annual leave.",
    "The company provides health insurance.",
    "Working hours are from 9 AM to 6 PM."
]

# Create document embeddings
document_embeddings = model.encode(documents)

# User question
query = "How many vacation days do employees get?"

# Create query embedding
query_embedding = model.encode(query)


# Cosine similarity
def cosine_similarity(a, b):

    return np.dot(a, b) / (
        np.linalg.norm(a) * np.linalg.norm(b)
    )


# Calculate similarity
scores = []

for embedding in document_embeddings:

    score = cosine_similarity(
        query_embedding,
        embedding
    )

    scores.append(score)


# Find most relevant document
best_index = np.argmax(scores)

print("Most relevant document:")
print(documents[best_index])