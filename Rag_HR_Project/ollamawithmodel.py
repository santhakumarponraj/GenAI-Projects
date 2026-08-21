from ollama import chat
import chromadb

client = chromadb.PersistentClient(path= r"./Rag_HR_Project\chroma_db")

collection = client.get_collection("pdf_docs")


question = ""

while question not in ['quit','bye','cancel','end','close','exit']:

    question = input("Enter the Question : [To End : 'quit','bye','cancel','end','close' ] : ")

    if question in ['quit','bye','cancel','end','close','exit']:
        break



    results = collection.query(
        query_texts= [question],
        n_results=3
    )

    context = ""
    for document,metadata in zip(results["documents"][0],results['metadatas'][0]):
        context += f"""Source : {metadata["source"]} Page : {metadata["pages"]} {document}"""

    prompt = fr"""You are a helpful Document Chatbot

    Answe the user's question using ONLY the information provided in the context

    if the answer cannot be fount in the context, Say : 'This information is not available in the Document'

    do not invert information.

    Context : {context}

    userQuestion : {question}
    """

    response = chat(
        model='qwen2.5vl:3b',
        messages=[
            {'role': 'user', 'content': prompt}
        ]
    )

    print(response['message']['content'])












# response = chat(
#     model='qwen2.5vl:3b',
#     messages=[
#         {'role': 'user', 'content': 'What is Power BI?'}
#     ]
# )

# print(response['message']['content'])