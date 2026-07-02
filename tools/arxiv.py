"""
tools/arxiv.py

Search academic papers using arXiv.
"""

from langchain_community.utilities import ArxivAPIWrapper
from langchain_core.tools import Tool


# -----------------------------------------------------
# Arxiv Wrapper
# -----------------------------------------------------

arxiv = ArxivAPIWrapper(
    top_k_results=3,
    load_max_docs=3,
    doc_content_chars_max=4000,
)


# -----------------------------------------------------
# Search Function
# -----------------------------------------------------

def arxiv_search(query: str) -> str:
    """
    Search research papers from arXiv.

    Args:
        query: Research topic

    Returns:
        Summary of relevant papers.
    """

    try:
        return arxiv.run(query)

    except Exception as e:
        return f"Arxiv Error: {e}"


# -----------------------------------------------------
# LangChain Tool
# -----------------------------------------------------

arxiv_tool = Tool(
    name="Arxiv Search",
    description="""
Useful for scientific papers,
machine learning,
artificial intelligence,
computer science,
mathematics,
physics,
and academic research.
""",
    func=arxiv_search,
)


# -----------------------------------------------------
# Test
# -----------------------------------------------------

if __name__ == "__main__":

    topic = input("Research Topic: ")

    print()

    result = arxiv_search(topic)

    print(result)