"""
graph/nodes.py

Contains reusable LangGraph nodes.
"""

from langgraph.prebuilt import ToolNode

from tools.search import web_search_tool
from tools.wikipedia import wikipedia_tool
from tools.arxiv import arxiv_tool


# -----------------------------------------------------
# Register All Tools
# -----------------------------------------------------

TOOLS = [
    web_search_tool,
    wikipedia_tool,
    arxiv_tool,
]


# -----------------------------------------------------
# Tool Node
# -----------------------------------------------------

tool_node = ToolNode(TOOLS)