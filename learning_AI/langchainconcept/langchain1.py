from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_chroma import Chroma

text = """
Python is a programming language.
Python is widely used for data analysis.
Python is also used for machine learning.
"""

splitter = RecursiveCharacterTextSplitter(
    chunk_size=100,
    chunk_overlap=20
)

chunks = splitter.create_documents([text])

embeddings = OpenAIEmbeddings(
    model="text-embedding-3-small"
)

db = Chroma.from_documents(
    chunks,
    embedding=embeddings
)

results = db.similarity_search(
    "What is Python used for?",
    k=2
)

for doc in results:
    print(doc.page_content)