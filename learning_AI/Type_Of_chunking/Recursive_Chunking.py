###Recursive Chunking

from langchain_text_splitters import RecursiveCharacterTextSplitter

text = """
Spark ERP is a billing software used by retail stores.

It manages invoices and customers.

It manages inventory and products.

The software also supports payment tracking.
"""

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=100,
    chunk_overlap=20,
    separators=[
        "\n\n","\n","."," ",""])

chunks = text_splitter.split_text(text)

for index, chunk in enumerate(chunks, 1):

    print(f"\nChunk {index}")
    print(chunk)