"""
tools/wikipedia.py

Wikipedia Tool
"""

from langchain_community.utilities import WikipediaAPIWrapper
from langchain_core.tools import Tool


# -----------------------------------------------------
# Wikipedia API
# -----------------------------------------------------

wikipedia = WikipediaAPIWrapper(
    top_k_results=3,
    doc_content_chars_max=4000,
)


# -----------------------------------------------------
# Search Function
# -----------------------------------------------------

def wikipedia_search(query: str) -> str:
    """
    Search Wikipedia.

    Args:
        query: Topic to search.

    Returns:
        Wikipedia summary.
    """

    try:
        return wikipedia.run(query)

    except Exception as e:
        return f"Wikipedia Error: {e}"


# -----------------------------------------------------
# LangChain Tool
# -----------------------------------------------------

wikipedia_tool = Tool(
    name="Wikipedia Search",
    description="""
Useful for finding factual information,
definitions, history, and general knowledge.
""",
    func=wikipedia_search,
)


# -----------------------------------------------------
# Test
# -----------------------------------------------------

if __name__ == "__main__":

    query = input("Wikipedia Search: ")

    print()

    result = wikipedia_search(query)

    print(result)