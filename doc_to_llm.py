from qa_chain import create_qa_chain
from file_downloader import text_splitter
from embeddings import create_embeddings
import os
os.environ["HUGGINGFACEHUB_API_TOKEN"] = "HUGGINGFACEHUB_API_TOKEN"

url = "https://raw.githubusercontent.com/hwchase17/chat-your-data/master/state_of_the_union.txt"
doc_name = "state_of_the_union.txt"
query = "What did the president say about the Supreme Court"

db = create_embeddings
docs = text_splitter(url, doc_name)
create_qa_chain(db, query)
