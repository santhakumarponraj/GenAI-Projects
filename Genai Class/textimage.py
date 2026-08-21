# pip install diffusers transformers accelerate torch safetensors
import streamlit as st
import torch
from transformers import pipeline
from diffusers import StableDiffusionPipeline

st.set_page_config(page_title="GenAI Chat + Image (CPU)")

# ---------------------------
# 1) Session state
# ---------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

# ---------------------------
# 2) Load models (CPU)
# ---------------------------
@st.cache_resource
def load_llm():
    return pipeline(
        "text-generation",
        model="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
        device=-1  # CPU
    )

@st.cache_resource
def load_image_model():
    pipe = StableDiffusionPipeline.from_pretrained(
        "runwayml/stable-diffusion-v1-5"
    )
    return pipe.to("cpu")

llm = load_llm()
img_pipe = load_image_model()

# ---------------------------
# 3) Generate chat reply
# ---------------------------
def generate_reply(messages):
    prompt = ""

    for msg in messages:
        if msg["role"] == "user":
            prompt += f"User: {msg['content']}\n"
        else:
            prompt += f"Assistant: {msg['content']}\n"

    prompt += "Assistant:"

    output = llm(
        prompt,
        max_new_tokens=120,
        temperature=0.7
    )[0]["generated_text"]

    return output.split("Assistant:")[-1].strip()

# ---------------------------
# 4) Display chat history
# ---------------------------
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        if "image" in msg:
            st.image(msg["image"], caption=msg["content"])
        else:
            st.markdown(msg["content"])

# ---------------------------
# 5) User input
# ---------------------------
user_input = st.chat_input("Ask or request an image...")

if user_input:
    # Save user message
    st.session_state.messages.append({
        "role": "user",
        "content": user_input
    })

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):

            # ---- Rule-based image trigger (more reliable on CPU) ----
            if "image" in user_input.lower() or "draw" in user_input.lower():

                prompt = user_input.replace("draw", "").replace("image", "")

                image = img_pipe(prompt).images[0]

                st.image(image, caption=prompt)

                st.session_state.messages.append({
                    "role": "assistant",
                    "content": prompt,
                    "image": image
                })

            else:
                reply = generate_reply(st.session_state.messages)

                st.markdown(reply)

                st.session_state.messages.append({
                    "role": "assistant",
                    "content": reply
                })