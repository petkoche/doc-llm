from langchain.chains.question_answering import load_qa_chain
from langchain import HuggingFaceHub


def create_qa_chain(db, query):
    llm = HuggingFaceHub(repo_id="google/flan-t5-xxl",
                         model_kwargs={"temperature": 0.15, "max_length": 512})

    chain = load_qa_chain(llm, chain_type="mydoc")
    docs = db.similarity_search(query)
    chain.run(input_documents=docs, question=query)
    # https://python.langchain.com/docs/modules/chains/additional/question_answering
