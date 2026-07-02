"""
rag/retriever.py

Retrieval layer for the RAG pipeline.
"""

from typing import List

from langchain_core.documents import Document

from RAG.vectorstore import VectorStore


class RAGRetriever:
    """
    Wrapper around the VectorStore retriever.
    """

    def __init__(
        self,
        search_type: str = "similarity",
        k: int = 4,
    ):

        self.vector_store = VectorStore()

        self.retriever = self.vector_store.get_retriever(
            search_type=search_type,
            k=k,
        )

    # --------------------------------------------------
    # Retrieve Documents
    # --------------------------------------------------

    def retrieve(
        self,
        query: str,
    ) -> List[Document]:
        """
        Retrieve relevant documents.
        """

        return self.retriever.invoke(query)

    # --------------------------------------------------
    # Retrieve Context
    # --------------------------------------------------

    def retrieve_context(
        self,
        query: str,
    ) -> str:
        """
        Convert retrieved documents into
        a single context string.
        """

        documents = self.retrieve(query)

        if not documents:
            return "No relevant documents found."

        context = []

        for index, doc in enumerate(documents, start=1):

            source = doc.metadata.get(
                "source",
                "Unknown"
            )

            page = doc.metadata.get(
                "page",
                "Unknown"
            )

            context.append(
                f"""
==========================================
Document {index}

Source : {source}

Page   : {page}

Content

{doc.page_content}
"""
            )

        return "\n".join(context)

    # --------------------------------------------------
    # Similar Documents
    # --------------------------------------------------

    def similarity_search(
        self,
        query: str,
        k: int = 4,
    ) -> List[Document]:

        return self.vector_store.search(
            query=query,
            k=k,
        )

    # --------------------------------------------------
    # Similarity Search With Score
    # --------------------------------------------------

    def similarity_search_with_score(
        self,
        query: str,
        k: int = 4,
    ):

        return self.vector_store.search_with_score(
            query=query,
            k=k,
        )


# --------------------------------------------------
# Singleton
# --------------------------------------------------

retriever = RAGRetriever()


# --------------------------------------------------
# Test
# --------------------------------------------------

if __name__ == "__main__":

    while True:

        query = input("\nQuestion (exit to quit): ")

        if query.lower() == "exit":
            break

        print()

        print(retriever.retrieve_context(query))