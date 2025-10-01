from langchain_community.vectorstores import Chroma

class VectorDB:
    def __init__(self, persist_directory, collection_name, embedding_function):
        self.vectorstore = Chroma(
            collection_name=collection_name,
            embedding_function=embedding_function,
            persist_directory=persist_directory
        )

    def add_texts(self, texts, metadatas, ids):
        self.vectorstore.add_texts(texts=texts, metadatas=metadatas, ids=ids)
        self.vectorstore.persist()

    def similarity_search(self, query, k=5):
        return self.vectorstore.similarity_search(query, k=k)
