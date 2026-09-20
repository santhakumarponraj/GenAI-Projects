# import faiss
# import numpy as np

# vectors = np.array([
#     [0.1, 0.2, 0.3],
#     [0.4, 0.5, 0.6],
#     [0.7, 0.8, 0.9]
# ]).astype("float32")

# index = faiss.IndexFlatL2(3)

# index.add(vectors)

# query = np.array([
#     [0.1, 0.2, 0.4]
# ]).astype("float32")

# distances, indexes = index.search(query, 2)

# print(indexes)



######## store locally and use

from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
##or
from sentence_transformers import SentenceTransformer

# 1. Prepare text documents
texts = [
    "FAISS is an open-source library for efficient similarity search.",
    "It was developed by Facebook AI Research.",
    "FAISS can store vector indexes directly on the local disk."
]

# 2. Initialize a free embedding model
embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

# model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")
# embeddings = model.encode(texts)

# 3. Create the FAISS database from texts
db = FAISS.from_texts(texts, embeddings)

# 4. SAVE the database locally (creates a folder with index and metadata)
folder_path = fr"C:\Users\Santhakumar\Desktop\Python Projects\GenAI-Projects\learning_AI\Vector_DB/my_local_faiss_db"
db.save_local(folder_path)
print(f"Database successfully saved to folder: '{folder_path}/'")

# 5. LOAD the database back from local disk
# Note: allow_dangerous_deserialization=True is required to load local pickle files
loaded_db = FAISS.load_local(
    folder_path, 
    embeddings, 
    allow_dangerous_deserialization=True
)

# 6. Test a quick similarity search
query = "Who built FAISS?"
docs = loaded_db.similarity_search(query, k=1)
print(f"\nSearch Result:\n{docs[0].page_content}")




# ####################################
# import numpy as np
# from sentence_transformers import SentenceTransformer
# from langchain_community.vectorstores import FAISS

# # 1. Initialize your specific SentenceTransformer model
# model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

# # 2. Define text data
# texts = [
#     "FAISS is an open-source library for efficient similarity search.",
#     "It was developed by Facebook AI Research.",
#     "FAISS can store vector indexes directly on the local disk."
# ]

# # 3. Generate raw vectors using your model
# embeddings = model.encode(texts)

# # 4. Pair texts with your generated embeddings
# text_embedding_pairs = list(zip(texts, embeddings))

# # 5. Create FAISS db using an inline dummy object instead of writing a class
# # (This tells LangChain how to encode future text queries during search)
# db = FAISS.from_embeddings(
#     text_embeddings=text_embedding_pairs,
#     embedding=type("DummyEmbed", (), {"embed_query": lambda text: model.encode(text).tolist()})()
# )

# # 6. Save the database to local disk
# folder_path = "my_local_faiss_db"
# db.save_local(folder_path)
# print(f"Database successfully saved to folder: '{folder_path}/'")

