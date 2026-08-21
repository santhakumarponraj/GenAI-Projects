import streamlit as st
from groq import Groq
from langchain_groq import ChatGroq

# --- Page setup ---
st.set_page_config(page_title="Langchain", layout="centered")

st.title("Langchain using Groq Demo")

# --- Sidebar controls ---
st.sidebar.header("Controls")

api_key = st.sidebar.text_input("Groq API Key", type="password")

# --- Prompt ---
prompt = st.text_area("Enter your prompt:")


LLAMA_MODEL_KEY='llama-3.3-70b-versatile'

llm = ChatGroq(model=LLAMA_MODEL_KEY, groq_api_key=api_key)

def groq_chat(message):
  response=llm.invoke(message)
  return response.content

if st.button("Generate"):
    if not api_key:
        st.error("Please enter your Groq API key.")
    else:
        response1=groq_chat(prompt)
        st.write(response1)