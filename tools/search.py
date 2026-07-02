"""
tools/search.py

Tavily Search Tool for the Multi-Agent Research Assistant.
"""

from langchain_community.tools.tavily_search import TavilySearchResults

from config import TAVILY_API_KEY


# --------------------------------------------------
# Tavily Search Tool
# --------------------------------------------------

web_search_tool = TavilySearchResults(
    api_key=TAVILY_API_KEY,
    max_results=5,
    search_depth="advanced",
    include_answer=True,
    include_raw_content=False,
    include_images=False,
)


# --------------------------------------------------
# Helper Function
# --------------------------------------------------

def search_web(query: str) -> str:
    """
    Search the web using Tavily.

    Args:
        query: Search query

    Returns:
        Search results as a string.
    """

    try:
        result = web_search_tool.invoke(
            {
                "query": query
            }
        )

        return str(result)

    except Exception as e:
        return f"Search Error: {e}"


# --------------------------------------------------
# Test
# --------------------------------------------------

if __name__ == "__main__":

    query = input("Search Query: ")

    print()

    results = search_web(query)

    print(results)