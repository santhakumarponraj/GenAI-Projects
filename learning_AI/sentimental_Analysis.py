
from transformers import pipeline

classifier = pipeline("sentiment-analysis")

result = classifier("I hate learning Generative AI!")

print(result)