import streamlit as st
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableWithMessageHistory
from langchain_community.chat_message_histories import ChatMessageHistory

# --- Page config ---
st.set_page_config(page_title="AI Chat App", layout="centered")
st.header("💬 AI Chat Langchain using Groq :sparkles:",text_alignment="center")
st.header("Using Session :memo: and Memory :brain:", text_alignment="center", divider=True)

# --- Sidebar ---
st.sidebar.header("Settings")
api_key = st.sidebar.text_input("Groq API Key", type="password")
session_id = st.sidebar.text_input("Session ID", value="user1")

# ✅ FIX 1: Persistent memory store
if "store" not in st.session_state:
    st.session_state.store = {}

# --- Session state for UI messages ---
if "messages" not in st.session_state:
    st.session_state.messages = []

# --- Display chat history (UI) ---
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# --- User input ---
user_input = st.chat_input("Type your message...")

# --- Model setup ---
if api_key:
    llm = ChatGroq(model="llama-3.3-70b-versatile", groq_api_key=api_key)

    prompt_template = ChatPromptTemplate.from_messages([
        ("system", "You are a helpful AI assistant"),
        ("placeholder", "{chat_history}"),
        ("human", "{message}")
    ])

    chain = prompt_template | llm

    # ✅ FIX 2: Use session_state store
    def get_history(session_id: str):
        store = st.session_state.store
        if session_id not in store:
            store[session_id] = ChatMessageHistory()
        return store[session_id]

    chat_with_memory = RunnableWithMessageHistory(
        runnable=chain,
        get_session_history=get_history,
        input_messages_key="message",
        history_messages_key="chat_history"
    )

# --- When user sends message ---
if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})

    with st.chat_message("user"):
        st.markdown(user_input)

    if not api_key:
        st.error("Enter API key in sidebar")
    else:
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):

                # ✅ FIX 3: stable session id
                response = chat_with_memory.invoke(
                    {"message": user_input},
                    {"configurable": {"session_id": session_id}}
                )

                reply = response.content
                st.markdown(reply)

        st.session_state.messages.append({"role": "assistant", "content": reply})

# --- Clear chat ---
if st.sidebar.button("🗑️ Clear Chat"):
    st.session_state.messages = []

    # ✅ FIX 4 (IMPORTANT): also clear memory
    if session_id in st.session_state.store:
        del st.session_state.store[session_id]