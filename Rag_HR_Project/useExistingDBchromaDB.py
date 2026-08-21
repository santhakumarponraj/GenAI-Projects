import chromadb

client = chromadb.PersistentClient(path= r"./Rag_HR_Project\chroma_db")

collection = client.get_collection("pdf_docs")

# print(collection.count())



