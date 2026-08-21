import os
import streamlit as st
from groq import Groq


# ==============================
# GROQ API KEY
# ==============================

api_key = "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"

if not api_key:
    st.error("GROQ_API_KEY is not set.")
    st.stop()


# ==============================
# GROQ CLIENT
# ==============================

client = Groq(api_key=api_key)


# ==============================
# GENERATE FUNCTION
# ==============================

def generate(client, prompt, temperature, top_p):

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=temperature,
        top_p=top_p
    )

    return response.choices[0].message.content


# ==============================
# STREAMLIT UI
# ==============================

st.title("Groq AI - Temperature & Top-P")

st.write("Experiment with Temperature and Top-P parameters.")


# Prompt
prompt = st.text_area(
    "Enter your prompt:",
    placeholder="Explain Artificial Intelligence in simple words."
)


# Temperature
temperature = st.slider(
    "Temperature",
    min_value=0.0,
    max_value=2.0,
    value=0.7,
    step=0.1
)


# Top-P
top_p = st.slider(
    "Top-P",
    min_value=0.0,
    max_value=1.0,
    value=0.9,
    step=0.05
)


# ==============================
# GENERATE BUTTON
# ==============================

if st.button("Generate"):

    if not prompt.strip():

        st.warning("Please enter a prompt.")

    else:

        with st.spinner("Generating..."):

            try:

                output = generate(
                    client,
                    prompt,
                    temperature,
                    top_p
                )

                st.success("Generated successfully!")

                st.write(output)

            except Exception as e:

                st.error("Groq API Error:")
                st.exception(e)


# import streamlit as st
# from groq import Groq

# # --- Page setup ---
# st.set_page_config(page_title="LLM Sampling Playground", layout="centered")

# st.title("🎛️ LLM Sampling Playground")
# st.caption("Explore how Temperature, Top-P affect generation (top_k is not supported in Groq's chat.completions.create() API)")

# # --- Sidebar controls ---
# st.sidebar.header("⚙️ Controls")

# api_key = "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"

# temperature = st.sidebar.slider("Temperature", 0.0, 1.0, 0.7, 0.1)
# top_p = st.sidebar.slider("Top-P (nucleus)", 0.1, 1.0, 0.9, 0.05)
# top_k = st.sidebar.slider("Top-K", 1, 100, 50, 1)

# mode = st.sidebar.radio(
#     "Mode",
#     ["Single Output", "Compare (3 runs)"]
# )

# # --- Prompt ---
# prompt = st.text_area(
#     "Enter your prompt:",
#     "Write a one-line story about a robot learning emotions."
# )

# # --- Generate function ---
# # -- top_k is not supported in Groq’s chat.completions.create() API.

# def generate(client, prompt, temperature, top_p):
#     response = client.chat.completions.create(
#         model="llama-3.3-70b-versatile",
#         messages=[{"role": "user", "content": prompt}],
#         temperature=temperature,
#         top_p=top_p,
#         max_tokens=100
#     )
#     return response.choices[0].message.content
# # --- Run ---
# if st.button("🚀 Generate"):
#     if not api_key:
#         st.warning("Please enter your API key")
#         st.stop()

#     client = Groq(api_key=api_key)

#     st.subheader("🧠 Output")

#     if mode == "Single Output":
#         with st.spinner("Generating..."):
#             output = generate(client, prompt, temperature, top_p)
#         st.success(output)

#     else:
#         cols = st.columns(3)
#         for i in range(3):
#             with cols[i]:
#                 with st.spinner(f"Run {i+1}..."):
#                     output = generate(client, prompt, temperature, top_p, top_k)
#                 st.success(output)

# # --- Explanation Panel ---
# st.divider()
# st.subheader("📊 How to Read This")

# col1, col2, col3 = st.columns(3)

# with col1:
#     st.markdown("### 🔥 Temperature")
#     st.write("""
#     - Low → safe, predictable  
#     - High → creative, diverse  
#     """)

# with col2:
#     st.markdown("### 🔢 Top-K")
#     st.write(f"""
#     Limits choices to top **{top_k}** words  
#     Smaller → safer  
#     Larger → more variety  
#     """)

# with col3:
#     st.markdown("### 🌊 Top-P")
#     st.write(f"""
#     Chooses words covering **{int(top_p*100)}% probability**  
#     Dynamic and more natural  
#     """)

# # --- Visual intuition ---
# st.divider()
# st.subheader("🎨 Intuition")

# st.info("""
# Think of it like this:

# • Temperature → "How adventurous?"  
# • Top-K → "How many options?"  
# • Top-P → "How much probability mass?"  
# """)