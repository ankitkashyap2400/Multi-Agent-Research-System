"""
tools/rag_tool.py

LangChain Tool for RAG Retrieval.
"""

from langchain_core.tools import tool


from RAG.retriver import retriever


@tool
def rag_search(query: str) -> str:
    """
    Search uploaded PDF documents using the RAG pipeline.

    Use this tool whenever the user's question is likely to be
    answered from uploaded documents, company manuals,
    internal documentation, books, PDFs, or knowledge bases.

    Do not use this tool for:
    - Latest news
    - Current events
    - Live web information

    Args:
        query: User question.

    Returns:
        Relevant document context.
    """

    try:

        context = retriever.retrieve_context(query)

        if context.strip() == "":
            return "No relevant documents found."

        return context

    except Exception as e:

        return f"RAG Search Error: {str(e)}"


# --------------------------------------------------
# Test
# --------------------------------------------------

if __name__ == "__main__":

    print("=" * 60)
    print("RAG Search Tool")
    print("=" * 60)

    while True:

        question = input("\nQuestion (type 'exit' to quit): ")

        if question.lower() == "exit":
            break

        print()

        response = rag_search.invoke(
            {
                "query": question
            }
        )
   
    print(response)