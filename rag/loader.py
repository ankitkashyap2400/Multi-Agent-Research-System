"""
rag/loader.py

Loads PDF documents for the RAG pipeline.
"""

from pathlib import Path
from typing import List

from langchain_core.documents import Document
from langchain_community.document_loaders import PyPDFLoader


class DocumentLoader:
    """
    Load one or more PDF documents.
    """

    def __init__(self, data_dir: str = "data/documents"):

        self.data_dir = Path(data_dir)

    def load_pdf(self, pdf_path: str) -> List[Document]:
        """
        Load a single PDF.

        Args:
            pdf_path: Path to PDF

        Returns:
            List[Document]
        """

        loader = PyPDFLoader(pdf_path)

        documents = loader.load()

        return documents

    def load_directory(self) -> List[Document]:
        """
        Load every PDF from the data directory.
        """

        documents = []

        if not self.data_dir.exists():
            return documents

        for pdf_file in self.data_dir.glob("*.pdf"):

            loader = PyPDFLoader(str(pdf_file))

            documents.extend(loader.load())

        return documents


if __name__ == "__main__":

    loader = DocumentLoader()

    docs = loader.load_directory()

    print("=" * 60)

    print(f"Loaded {len(docs)} pages")

    print("=" * 60)

    if docs:

        print()

        print(docs[0].page_content[:1000])