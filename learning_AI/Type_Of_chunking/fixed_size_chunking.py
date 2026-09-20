## Fixed-Size Chunking

text = """
Spark ERP is a billing software.
It manages invoices and inventory.
It manages customers and payments.
"""

chunk_size = 50

chunks = []

for i in range(0, len(text), chunk_size):
    chunks.append(text[i:i + chunk_size])

for index, chunk in enumerate(chunks, 1):
    print(f"\nChunk {index}:")
    print(chunk)