from typing import Annotated
from typing import TypedDict

from langchain_core.messages import BaseMessage
from langgraph.graph.message import add_messages


class ResearchState(TypedDict):
    """
    Shared state for the Multi-Agent Research Assistant.

    Every node receives this state and returns updates to it.
    """

    # -----------------------------
    # Conversation History
    # -----------------------------
    messages: Annotated[list[BaseMessage], add_messages]

    # -----------------------------
    # Original User Query
    # -----------------------------
    query: str

    # -----------------------------
    # Planner Output
    # -----------------------------
    plan: list[str]

    # -----------------------------
    # Current Task
    # -----------------------------
    current_task: str

    # -----------------------------
    # Research Results
    # Example:
    # {
    #   "History": "...",
    #   "Applications": "..."
    # }
    # -----------------------------
    research_results: dict[str, str]

    # -----------------------------
    # Missing information identified
    # by the Critic Agent
    # -----------------------------
    critique: str

    # -----------------------------
    # Final Summary
    # -----------------------------
    summary: str

    # -----------------------------
    # Markdown Report
    # -----------------------------
    report: str

    # -----------------------------
    # Research Loop Counter
    # -----------------------------
    iteration: int

    # -----------------------------
    # Next Node
    # -----------------------------
    next: str