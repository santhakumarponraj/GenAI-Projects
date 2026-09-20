#Sentence-Based Chunking

import re

text = """
Spark ERP is a billing software.
It manages invoices.
It manages inventory.
It manages customers.
It handles payments.
"""

sentences = re.split(r'(?<=[.!?])\s+', text.strip())

for index, sentence in enumerate(sentences, 1):

    print(f"Chunk {index}:")
    print(sentence)
    print()