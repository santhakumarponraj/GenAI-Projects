from transformers import GPT2Tokenizer

# Load the pre-trained GPT-2 tokenizer
tokenizer = GPT2Tokenizer.from_pretrained("gpt2")

# Test text
text = "Hello, how are you doing today?"

#tokenize the Input

tokens = tokenizer(text)

tokens_id = tokens["input_ids"]

tokens_text = tokenizer.convert_ids_to_tokens(tokens_id)

print("Tokens:", tokens)
print("Token IDs:", tokens_id)
print("Token Text:", tokens_text)


# Encode the text into token IDs
encoded_input = tokenizer(text)
print("Token IDs:", encoded_input["input_ids"])

# Decode the IDs back into words
decoded_output = tokenizer.decode(encoded_input["input_ids"])
print("Decoded Text:", decoded_output)
