from transformers import AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained(
    "bert-base-uncased"
)

text = "Generative AI is powerful"

tokens = tokenizer.tokenize(text)

print(tokens)