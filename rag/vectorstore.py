"""
rag/vectorstore.py

Persistent Chroma Vector Store
"""

from pathlib import Path

from langchain_chroma import Chroma
from langchain_core.documents import Document

from RAG.embeddings import get_embedding_model


class VectorStore:
    """
    Wrapper around Chroma vector database.
    """

    def __init__(
        self,
        persist_directory: str = "vectordb",
        collection_name: str = "research_documents",
    ):

        self.persist_directory = Path(persist_directory)
        self.persist_directory.mkdir(
            parents=True,
            exist_ok=True,
        )

        self.embeddings = get_embedding_model()

        self.db = Chroma(
            collection_name=collection_name,
            embedding_function=self.embeddings,
            persist_directory=str(self.persist_directory),
        )

    # -------------------------------------------------
    # Index Documents
    # -------------------------------------------------

    def index_documents(
        self,
        documents: list[Document],
    ) -> None:

        if not documents:
            print("No documents found.")
            return

        self.db.add_documents(documents)

        print(f"Indexed {len(documents)} chunks.")

    # -------------------------------------------------
    # Search
    # -------------------------------------------------

    def search(
        self,
        query: str,
        k: int = 4,
    ) -> list[Document]:

        return self.db.similarity_search(
            query=query,
            k=k,
        )

    # -------------------------------------------------
    # Search With Score
    # -------------------------------------------------

    def search_with_score(
        self,
        query: str,
        k: int = 4,
    ):

        return self.db.similarity_search_with_score(
            query=query,
            k=k,
        )

    # -------------------------------------------------
    # Retriever
    # -------------------------------------------------

    def get_retriever(
        self,
        k: int = 4,
    ):

        return self.db.as_retriever(
            search_type="similarity",
            search_kwargs={
                "k": k,
            },
        )

    # -------------------------------------------------
    # Delete Collection
    # -------------------------------------------------

    def delete(self):

        self.db.delete_collection()

    # -------------------------------------------------
    # Reset
    # -------------------------------------------------

    def reset(self):

        self.delete()

        self.db = Chroma(
            collection_name="research_documents",
            embedding_function=self.embeddings,
            persist_directory=str(self.persist_directory),
        )