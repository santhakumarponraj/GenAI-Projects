# pip install -q transformers
import streamlit as st
from transformers import pipeline
from PIL import Image

st.set_page_config(page_title="Hugging Face Demo", layout="centered")

st.title("🤗 Hugging Face Pipeline Demo")

# Load pipelines (cached)
@st.cache_resource
def load_models():
    sentiment = pipeline("sentiment-analysis")
    text_gen = pipeline("text-generation", model="gpt2")
    doc_qa = pipeline("document-question-answering", model="naver-clova-ix/donut-base-finetuned-docvqa")
    return sentiment, text_gen, doc_qa

sentiment, text_gen, doc_qa = load_models()

# -------- TABS --------
tab1, tab2, tab3 = st.tabs([
    "😊 Sentiment Analysis",
    "✍️ Text Generation",
    "📄 Document QA"
])

# -------- TAB 1: SENTIMENT --------
with tab1:
    st.subheader("Sentiment Analysis")

    user_input = st.text_area("Enter text:", height=120)

    if st.button("Analyze", key="sentiment_btn"):
        if user_input:
            with st.spinner("Analyzing..."):
                result = sentiment(user_input)

                label = result[0]['label']
                score = result[0]['score']

                col1, col2 = st.columns(2)
                col1.metric("Sentiment", label)
                col2.metric("Confidence", f"{score:.2f}")

                if label == "POSITIVE":
                    st.success("✅ Positive sentiment detected")
                else:
                    st.error("❌ Negative sentiment detected")
        else:
            st.warning("Please enter some text.")

# -------- TAB 2: TEXT GENERATION --------
with tab2:
    st.subheader("Generate Text")

    prompt = st.text_area("Enter prompt:", height=120)

    col1, col2 = st.columns(2)
    max_len = col1.slider("Max Length", 20, 200, 50)
    generate_btn = col2.button("Generate")

    if generate_btn:
        if prompt:
            with st.spinner("Generating text..."):
                result = text_gen(prompt, max_length=max_len)
                generated_text = result[0]['generated_text']

                st.text_area("Generated Output:", generated_text, height=200)
        else:
            st.warning("Please enter a prompt.")

# -------- TAB 3: DOCUMENT QA --------
with tab3:
    st.subheader("Ask Questions from Document")

    uploaded_file = st.file_uploader(
        "Upload an image (invoice, receipt, etc.)",
        type=["png", "jpg", "jpeg"]
    )

    question = st.text_input("Your question:")

    if st.button("Get Answer", key="docqa_btn"):
        if uploaded_file and question:
            with st.spinner("Reading document..."):
                image = Image.open(uploaded_file)
                result = doc_qa(image=image, question=question)

                if isinstance(result, list):
                    result = result[0]

                st.success(f"📌 Answer: {result.get('answer', 'Not found')}")
        else:
            st.warning("Please upload a file and enter a question.")