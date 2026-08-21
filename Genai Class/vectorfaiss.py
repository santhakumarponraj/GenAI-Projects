# pip install streamlit faiss-cpu sentence-transformers
import streamlit as st
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

st.title("FAISS(Vector) Demo")

# Step 1: Sample data
sentences = [
    "FAISS-Facebook AI Similarity Search",
    "Transformers are the core neural network architecture behind modern large language models (LLMs) like GPT, Claude, and Gemini.",
    "Streamlit makes web apps easy",
    "Temperature is a parameter for adjusting the output of large language models (LLMs). "
]

# Step 2: Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Step 3: Convert sentences to vectors
embeddings = model.encode(sentences)

# Step 4: Create FAISS index
dim = embeddings.shape[1]
index = faiss.IndexFlatL2(dim)
index.add(np.array(embeddings))

# Step 5: User input
query = st.text_input("Enter your query:")

if query:
    # Convert query to vector
    query_vec = model.encode([query])

    # Search in FAISS
    distances, indices = index.search(np.array(query_vec), k=1)

    # Show result
    result = sentences[indices[0][0]]

    st.subheader("✅ Most Similar Sentence:")
    st.write(result)