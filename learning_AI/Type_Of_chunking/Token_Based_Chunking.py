from langchain_text_splitters import TokenTextSplitter

text = """
Spark ERP is billing software.

It manages invoices, customers,
products and inventory.

It also manages payments.
"""

text_splitter = TokenTextSplitter(

    chunk_size=20,
    chunk_overlap=5
)

chunks = text_splitter.split_text(text)

for index, chunk in enumerate(chunks, 1):

    print(f"\nChunk {index}:")
    print(chunk)