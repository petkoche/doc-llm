from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS

embeddings = HuggingFaceEmbeddings()


def create_embeddings(docs):
    db = FAISS.from_documents(docs, embeddings)
    return db
