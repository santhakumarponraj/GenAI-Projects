from langchain_experimental.text_splitter import SemanticChunker
from langchain_openai import OpenAIEmbeddings

text = """
Spark ERP manages billing and invoices.

The application also manages customer payments.

Inventory management helps track available stock.

Stock levels can automatically be updated after sales.

Artificial intelligence can predict future sales.
"""

embeddings = OpenAIEmbeddings()

text_splitter = SemanticChunker(
    embeddings
)

chunks = text_splitter.split_text(text)

for index, chunk in enumerate(chunks, 1):

    print(f"\nChunk {index}:")
    print(chunk)