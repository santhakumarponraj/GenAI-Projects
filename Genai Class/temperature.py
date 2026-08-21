# pip install groq
import streamlit as st
from groq import Groq

# --- Setup ---
st.set_page_config(page_title="LLM Temperature Demo", layout="centered")

st.title("🔥 LLM Temperature Demo")
st.write("Control how creative the AI becomes!")

# --- API Key Input ---
api_key = st.text_input("Enter your Groq API Key", type="password")

# --- Prompt Input ---
prompt = st.text_area(
    "Enter your prompt:",
    "Write a one-line story about a robot learning emotions."
)

# --- Temperature Slider ---
temperature = st.slider(
    "Temperature (Creativity)",
    min_value=0.0,
    max_value=1.0,
    value=0.7,
    step=0.1
)

# --- Generate Button ---
if st.button("Generate"):
    if not api_key:
        st.warning("Please enter your API key")
    else:
        client = Groq(api_key=api_key)

        with st.spinner("Generating..."):
            response = client.chat.completions.create(
                model="llama-3.1-8b-instant",
                messages=[
                    {"role": "user", "content": prompt}
                ],
                temperature=temperature,
                max_tokens=100
            )

            output = response.choices[0].message.content

        # --- Output ---
        st.subheader("Output:")
        st.success(output)

        # --- Explanation ---
        if temperature < 0.3:
            st.info("🔵 Low temperature → More predictable, factual")
        elif temperature < 0.7:
            st.info("🟡 Medium temperature → Balanced creativity")
        else:
            st.info("🔴 High temperature → More creative, diverse")