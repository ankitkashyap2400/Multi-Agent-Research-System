"""
graph/workflow.py

Builds the complete LangGraph workflow.
"""

from langgraph.graph import StateGraph
from langgraph.graph import START
from langgraph.graph import END

from langgraph.checkpoint.memory import MemorySaver

from graph.state import ResearchState

from graph.nodes import tool_node
from graph.router import research_router

from agents.planner import planner_node
from agents.researcher import researcher_node
from agents.critic import critic_node
from agents.summarizer import summarizer_node
from agents.reporter import reporter_node


# ---------------------------------------------
# Build Graph
# ---------------------------------------------

builder = StateGraph(ResearchState)


# ---------------------------------------------
# Nodes
# ---------------------------------------------

builder.add_node("planner", planner_node)

builder.add_node("researcher", researcher_node)

builder.add_node("tools", tool_node)

builder.add_node("critic", critic_node)

builder.add_node("summarizer", summarizer_node)

builder.add_node("reporter", reporter_node)


# ---------------------------------------------
# Start Edge
# ---------------------------------------------

builder.add_edge(START, "planner")


# ---------------------------------------------
# Planner -> Researcher
# ---------------------------------------------

builder.add_edge(
    "planner",
    "researcher"
)


# ---------------------------------------------
# Researcher Routing
# ---------------------------------------------

builder.add_conditional_edges(
    "researcher",
    research_router,
    {
        "tools": "tools",
        "critic": "critic",
    },
)


# ---------------------------------------------
# Tool -> Researcher
# ---------------------------------------------

builder.add_edge(
    "tools",
    "researcher",
)


# ---------------------------------------------
# Critic Routing
# ---------------------------------------------

builder.add_conditional_edges(
    "critic",
    lambda state: state["next"],
    {
        "researcher": "researcher",
        "summarizer": "summarizer",
    },
)


# ---------------------------------------------
# Summary
# ---------------------------------------------

builder.add_edge(
    "summarizer",
    "reporter",
)


# ---------------------------------------------
# Report
# ---------------------------------------------

builder.add_edge(
    "reporter",
    END,
)


# ---------------------------------------------
# Memory
# ---------------------------------------------

memory = MemorySaver()


# ---------------------------------------------
# Compile Graph
# ---------------------------------------------

graph = builder.compile(
    checkpointer=memory
)