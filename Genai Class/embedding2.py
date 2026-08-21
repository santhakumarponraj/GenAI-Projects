import streamlit as st
from sentence_transformers import SentenceTransformer, util

# -----------------------------
# Load model (cached)
# -----------------------------
@st.cache_resource
def load_model():
    return SentenceTransformer('all-MiniLM-L6-v2')

model = load_model()

# -----------------------------
# Sample documents
# -----------------------------
documents = [
    "Python is a programming language",
    "Dogs are great pets",
    "I love machine learning",
    "Artificial intelligence is the future",
    "Cats are independent animals",
    "Deep learning is a subset of machine learning",
    "AI is transforming industries",
    "Pandas is used for data analysis"
]

# -----------------------------
# Encode documents (cached)
# -----------------------------
@st.cache_data
def encode_docs(docs):
    return model.encode(docs)

doc_embeddings = encode_docs(documents)

# -----------------------------
# UI
# -----------------------------
st.title("🔍 Semantic Search Demo")
st.write("Search using meaning, not exact keywords!")

query = st.text_input("Enter your search query:")

# -----------------------------
# Search logic
# -----------------------------
if query:
    query_embedding = model.encode(query)

    # Compute similarity (returns PyTorch tensor)
    scores = util.cos_sim(query_embedding, doc_embeddings)

    # Slider for number of results
    top_k = st.slider("Number of results", 1, len(documents), 3)

    # Use PyTorch topk (clean & efficient)
    top_results = scores[0].topk(top_k)

    st.subheader("Top Results:")

    for score, idx in zip(top_results.values, top_results.indices):
        st.write(f"👉 {documents[idx]}")
        st.caption(f"Score: {score:.4f}")