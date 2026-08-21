import numpy as np
import os
import pdfplumber
from sentence_transformers import SentenceTransformer
import docx


cocFile = fr"C:\Users\SanthakumarPonraj\Downloads\All complaint\All complaint\CoC_JST Sales America Inc_ASSHSSH28K51_canadapfas.docx"


def read_docx(file_path):
    text = ""
    doc = docx.Document(file_path)
    for paragraph in doc.paragraphs:
        text += paragraph.text

    return text

    
def read_pdf(file_path):
    text = ""

    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:

            pdftxt = page.extract_text()

            text += pdftxt

    return text


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


def embedding_text(text):

    model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

    chunks = [
    chunk
    for document in text
    for chunk in document]

    embeddings = model.encode(
            chunks,
            convert_to_numpy=True
        ).astype(np.float32)

    vector_db = {
    "documents": np.array(chunks),
    "embeddings": embeddings}

    return vector_db,model




if __name__ == "__main__":

    if cocFile.lower().endswith(".pdf"):
        text = read_pdf(cocFile)
    elif cocFile.lower().endswith(".docx"):
        text = read_docx(cocFile)

    chunks = chunk_text(text)

    embeddings,model = embedding_text(text)

    question = "In which regulation the document falls"



    query_embedding = model.encode(
        question,
        convert_to_numpy=True
    ).astype(np.float32)

    





