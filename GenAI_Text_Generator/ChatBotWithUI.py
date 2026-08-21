import streamlit as st
import google.generativeai as genai

st.title("GenAI Text Generation - Chat App")
# key = fr"AQ.Ab8RN6LwymhCyDeyqXU7NRFskY1rYQBpOub9JSiDjUxcmilehwsantha"

genai.configure(api_key="key")
model = genai.GenerativeModel("models/gemini-3.6-flash")


if "data" not in st.session_state:
    st.session_state.data = {}

for key,val in st.session_state.data.items():
    with st.chat_message("user"):
        st.write(key)
    with st.chat_message("assistant"):
        st.write(val) 

prompt = st.chat_input("Enter your message...")

if prompt : 

    response = model.generate_content(prompt)

    st.session_state.data[prompt] = response.text

    with st.chat_message("user"):
        st.write(prompt)

    with st.chat_message("assistant"):
        st.write(response.text)
