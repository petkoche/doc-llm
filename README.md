# doc-llm
doc-llm is a small python tool that allows you to interact wtih your documents.

# How it works?
It dowloads a text document and then splits it into chunks. chunk_size=1000 it shouldn't be higher than your models max_input tokens.
These chunks are then converted to embeddings. [What are embeddings.](https://towardsdatascience.com/neural-network-embeddings-explained-4d028e6f0526)
We then store these embeddings into a vactor db ( FAISS ). This allows us at query time to embed the unstructured query and retrieve the embedding vectors that are 'most similar' to the embedded query. A vector store takes care of storing embedded data and performing vector search for you.
We'll then get a ranked response which we'll feed into a generative language model to get a structured reponse to BOB the user.

## Architecture

![App Screenshot](https://raw.githubusercontent.com/petkoche/doc-llm/main/static/ARCH_DIAGRAM.jpg)
