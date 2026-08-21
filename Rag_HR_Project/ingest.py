import os
import pdfplumber
from sentence_transformers import SentenceTransformer
from transformers import GPT2Tokenizer

folderpath = fr"Rag_HR_Project\pdf"

def extract_text_From_Pdf(folderpath):
    metadatas = []
    text = ""
    for fileName in os.listdir(folderpath):
        with pdfplumber.open(os.path.join(folderpath,fileName)) as pdf:
            for pageNumber , page in enumerate(pdf.pages):
                
                text += page.extract_text()
            metadatas.append({
                "source" : fileName,
                "pages" : pageNumber
                })

    return text,metadatas

def chunk_text(pdf_text):

    chunks = []
    startpnt = 0
    endpnt = 0
    overlap = 0

    while startpnt + 500 <= len(pdf_text):
        if startpnt == 0:
            startpnt = 0
            endpnt = startpnt + 500
            overlap = endpnt - 100
            # print(startpnt,endpnt,overlap)
            chunks.append(pdf_text[startpnt:endpnt])
            startpnt = overlap
            
        else:
            startpnt = overlap
            endpnt = startpnt +500
            overlap = endpnt - 100
            # print(startpnt,endpnt,overlap)
            # print(chunks)
            # print(pdf_text[startpnt:endpnt])
            chunks.append(pdf_text[startpnt:endpnt])
            startpnt = overlap

    endpnt = len(pdf_text)
    chunks.append(pdf_text[startpnt:endpnt])
    # print(chunks)

    return chunks

# def Embedding_Text(chunks):

#     embed = []

#     model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

#     # model = SentenceTransformer(
#     # r"D:\Power Bi Project\GenAI\Rag_HR_Project\models\all-MiniLM-L6-v2")


#     for text in chunks:

#         embedding = model.encode(text)

#         embed.append(embedding)

#     return embed



pdf_text,metadata = extract_text_From_Pdf(folderpath) 

chunks = chunk_text(pdf_text)

# print(metadatas)

# embed = Embedding_Text(chunks)


# print(embed)




