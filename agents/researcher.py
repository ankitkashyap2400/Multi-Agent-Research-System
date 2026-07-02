"""
agents/researcher.py

Research Agent

Responsibilities:
- Receive the current research task
- Decide whether to call tools
- Return an AIMessage
"""

from typing import Any

from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage

from config import (
    GROQ_API_KEY,
    MODEL_NAME,
    TEMPERATURE,
)

from graph.state import ResearchState

from prompts.researcher import research_prompt

from tools.search import web_search_tool
from tools.wikipedia import wikipedia_tool
from tools.arxiv import arxiv_tool


# ----------------------------------------------------
# Initialize LLM
# ----------------------------------------------------

llm = ChatGroq(
    model=MODEL_NAME,
    api_key=GROQ_API_KEY,
    temperature=TEMPERATURE,
)


# ----------------------------------------------------
# Register Tools
# ----------------------------------------------------

tools = [
    web_search_tool,
    wikipedia_tool,
    arxiv_tool,
]

llm_with_tools = llm.bind_tools(tools)


# ----------------------------------------------------
# Research Node
# ----------------------------------------------------

def researcher_node(state: ResearchState) -> dict[str, Any]:
    """
    LangGraph Research Node
    """

    task = state["current_task"]

    prompt = research_prompt.invoke(
        {
            "task": task
        }
    )

    response = llm_with_tools.invoke(prompt.messages)

    return {
        "messages": [response]
    }