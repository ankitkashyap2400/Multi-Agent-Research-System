"""
rag/embeddings.py

Creates and manages the embedding model used by the RAG pipeline.
"""

from functools import lru_cache

from langchain_huggingface import HuggingFaceEmbeddings


class EmbeddingModel:
    """
    Singleton wrapper for HuggingFace embedding models.
    """

    DEFAULT_MODEL = "BAAI/bge-small-en-v1.5"

    def __init__(
        self,
        model_name: str | None = None,
        device: str = "cpu",
    ):
        self.model_name = model_name or self.DEFAULT_MODEL
        self.device = device

    def load(self) -> HuggingFaceEmbeddings:
        """
        Load the HuggingFace embedding model.
        """

        return HuggingFaceEmbeddings(
            model_name=self.model_name,
            model_kwargs={
                "device": self.device,
            },
            encode_kwargs={
                "normalize_embeddings": True,
            },
        )


@lru_cache(maxsize=1)
def get_embedding_model() -> HuggingFaceEmbeddings:
    """
    Return a cached embedding model instance.

    The model is loaded only once during the application's lifetime.
    """

    embedding_model = EmbeddingModel()

    return embedding_model.load()


def embed_query(query: str) -> list[float]:
    """
    Generate an embedding vector for a query.

    Args:
        query: User query

    Returns:
        List of floats
    """

    embeddings = get_embedding_model()

    return embeddings.embed_query(query)


def embed_documents(documents: list[str]) -> list[list[float]]:
    """
    Generate embeddings for multiple documents.

    Args:
        documents: List of text chunks

    Returns:
        List of embedding vectors
    """

    embeddings = get_embedding_model()

    return embeddings.embed_documents(documents)


if __name__ == "__main__":

    model = get_embedding_model()

    print("=" * 60)
    print("Embedding Model Loaded")
    print("=" * 60)

    print(f"Model: {EmbeddingModel.DEFAULT_MODEL}")

    query = "What is LangGraph?"

    vector = embed_query(query)

    print(f"Embedding Dimension: {len(vector)}")

    print()

    print("First 10 Values")

    print(vector[:10])

    print("=" * 60)