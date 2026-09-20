text = """
Spark ERP is a billing software.
It manages invoices and inventory.
It manages customers and payments.
"""

chunk_size = 50
chunk_overlap = 10

chunks = []

start = 0

while start < len(text):

    end = start + chunk_size

    chunk = text[start:end]

    chunks.append(chunk)

    start = end - chunk_overlap


for index, chunk in enumerate(chunks, 1):
    print(f"\nChunk {index}:")
    print(chunk)