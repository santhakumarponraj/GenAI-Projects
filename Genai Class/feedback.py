import streamlit as st

from transformers import pipeline

# ----------------------------
# Load Models (Pretrained)
# ----------------------------

def load_models():
    sentiment_model = pipeline("sentiment-analysis")
#    generator_model = pipeline("text-generation", model="gpt2")
    generator_model = pipeline("text-generation", model="Qwen/Qwen3-0.6B")
    return sentiment_model, generator_model

sentiment_model, generator_model = load_models()

# ----------------------------
# UI
# ----------------------------
st.title("AI Customer Feedback Analyzer")

st.write("Analyze sentiment and generate AI responses")

user_input = st.text_area("Enter your review:")

# ----------------------------
# Sentiment Analysis (BERT)
# ----------------------------
if st.button("Analyze Sentiment"):
    if user_input.strip():
        result = sentiment_model(user_input)[0]

        label = result['label']
        score = result['score']

        if label == "POSITIVE":
            st.success(f"✅ Positive ({score:.2f})")
        else:
            st.error(f"❌ Negative ({score:.2f})")
    else:
        st.warning("Please enter text")

# ----------------------------
# Text Generation (GPT)
# ----------------------------
if st.button("Generate Response"):
    if user_input.strip():
        prompt = f"Customer review: {user_input}\nResponse:"

        output = generator_model(
            prompt,
            max_length=80,
            do_sample=True,
            top_p=0.9,
            pad_token_id=50256
        )

        #generated_text = output[0]['generated_text']

        generated_text = output[0]['generated_text']
        # Extract only response after "Response:"
        response = generated_text.split("Response:")[-1].strip()
        
        st.subheader("AI Response:")
        st.write(response)
        #st.write(generated_text)

        
    else:
        st.warning("Please enter text")

# Examples - good review

# Absolutely loved our meal here
# Fresh, high-quality ingredients and highly recommend!
# Hands down, some of the best food I've had recently
# Delicious, well-cooked food with a lovely presentation
# Cooked to perfection
# Worth every penny
# Best Dish I've ever had

# Examples - Bad Review
# Food is frequently described as cold, bland, greasy, overcooked, or undercooked.
# Dirty, sticky tables and unhygienic conditions are common in this restaurant.
# Long waiting times and unprofessional,rude staff
# High prices for food and poor service
# Worst Taste
    