# import google.generativeai as genai

# key = fr"AQ.Ab8RN6LwymhCyDeyqXU7NRFskY1rYQBpOub9JSiDjUxcmilehwsantha"

import google.generativeai as genai

# Add your Gemini API key
genai.configure(api_key=key)
model = genai.GenerativeModel("models/gemini-3.6-flash")


question = ''

while True:

    question = input("Ask your question: ")

    if question.lower() in ["exit",'cancel','quit']:
        break


    response = model.generate_content(question)

    print("AI Answer:", response.text)