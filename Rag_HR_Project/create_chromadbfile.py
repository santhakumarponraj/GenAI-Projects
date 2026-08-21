from ingest import chunks  ,metadata
import chromadb
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

client = chromadb.PersistentClient(
    path= r"./Rag_HR_Project\chroma_db"
)

collection = client.get_or_create_collection("pdf_docs")

# Store PDF chunks
for i, chunk in enumerate(chunks):
    collection.add(
        ids=[str(i)],
        documents=[chunk],
        embeddings=[model.encode(chunk).tolist()],
        metadatas= metadata
    )

# User question

question = "what is arun"


results = collection.query(
    query_embeddings= [model.encode(question).tolist()],
    n_results=3
)

for document,metadata in zip(results["documents"][0],results['metadatas'][0]):
    print(document,"doc")
    print(metadata,"metadata")


