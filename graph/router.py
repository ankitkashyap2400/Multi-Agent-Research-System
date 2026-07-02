"""
graph/router.py

Routing functions for LangGraph.
"""

from langgraph.graph import END

from graph.state import ResearchState


# ----------------------------------------------------
# Research Router
# ----------------------------------------------------

def research_router(state: ResearchState):
    """
    Decide whether to execute tools or move to Critic.

    Returns:
        "tools"  -> Execute ToolNode
        "critic" -> Continue workflow
    """

    messages = state["messages"]

    if not messages:
        return "critic"

    last_message = messages[-1]

    # LLM requested one or more tools
    if getattr(last_message, "tool_calls", None):
        return "tools"

    # No tool call
    return "critic"


# ----------------------------------------------------
# Critic Router
# ----------------------------------------------------

def critic_router(state: ResearchState):
    """
    Decide whether another research iteration is needed.
    """

    critique = state.get("critique", "").strip()

    iteration = state.get("iteration", 0)

    # Maximum iterations reached
    if iteration >= 3:
        return "summarizer"

    # Critic requested more research
    if critique:
        return "researcher"

    # Research is sufficient
    return "summarizer"


# ----------------------------------------------------
# Report Router
# ----------------------------------------------------

def report_router(state: ResearchState):
    """
    Final router.
    """

    return END