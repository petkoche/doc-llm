from qa_chain import create_qa_chain
from file_downloader import text_splitter
from embeddings import create_embeddings
from dotenv import load_dotenv
import os
load_dotenv()

query = "What did the president say about the Supreme Court"

docs = text_splitter(os.getenv("URL"), os.getenv("DOC_NAME"))
db = create_embeddings(docs)
create_qa_chain(db, query)
