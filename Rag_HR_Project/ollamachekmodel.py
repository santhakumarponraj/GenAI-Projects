import ollama

response = ollama.list()

# Iterate and print each model's name
for model in response.get('models', []):
    print(model.get('model'))