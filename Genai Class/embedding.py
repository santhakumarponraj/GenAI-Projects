# pip install spacy
# python -m spacy download en_core_web_sm
# pip install sentence-transformers

import spacy
import streamlit as st

nlp = spacy.load('en_core_web_sm')

text1 = nlp("A red apple")
text2 = nlp("A ripe apple")

st.write(f"Vector for 'A red apple':\n{text1.vector}\n")
st.write(f"Vector for 'A ripe apple':\n{text2.vector}\n")

similarity = text1.similarity(text2)
st.write(f"Similarity score: {similarity}")

from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer('all-MiniLM-L6-v2')

sentence1 = "The sun is shining brightly."
sentence2 = "It is a beautiful sunny day."

embedding1 = model.encode(sentence1)
embedding2 = model.encode(sentence2)

similarity_score = util.cos_sim(embedding1, embedding2)
st.write(f"Cosine Similarity: {similarity_score.item()}")