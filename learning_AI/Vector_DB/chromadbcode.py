import chromadb

client = chromadb.PersistentClient(path=fr"C:\Users\Santhakumar\Desktop\Python Projects\GenAI-Projects\learning_AI\Vector_DB/chroma_db")

# --- Create the DB --------
collection = client.get_or_create_collection(name="documents")

# collection = client.get_collection(name="documents") # ------use the existing DB ----

collection.add(documents=[
        "Python is used for AI.",
        "Java is popular for enterprise applications."],
    ids=["1", "2"])

results = collection.query(
    query_texts=["Which language is useful for artificial intelligence?"],
    n_results=1)

print(results)