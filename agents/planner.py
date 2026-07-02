"""
Planner Agent

Responsibility:
- Receive the user's research query.
- Generate a structured research plan.
- Return the updated LangGraph state.
"""

from typing import Any

from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser

from config import (
    GROQ_API_KEY,
    MODEL_NAME,
    TEMPERATURE,
)

from prompts.planner import planner_prompt
from graph.state import ResearchState


# ----------------------------------------------------
# Initialize LLM
# ----------------------------------------------------

llm = ChatGroq(
    model=MODEL_NAME,
    api_key=GROQ_API_KEY,
    temperature=TEMPERATURE,
)


# ----------------------------------------------------
# Planner Chain
# ----------------------------------------------------

planner_chain = (
    planner_prompt
    | llm
    | StrOutputParser()
)


# ----------------------------------------------------
# Parse LLM Output
# ----------------------------------------------------

def parse_plan(plan_text: str) -> list[str]:
    """
    Convert numbered text into a Python list.

    Example Input:

        1. Introduction
        2. History
        3. Applications

    Example Output:

        [
            "Introduction",
            "History",
            "Applications"
        ]
    """

    tasks = []

    for line in plan_text.splitlines():

        line = line.strip()

        if not line:
            continue

        # Remove numbering

        if "." in line:

            _, task = line.split(".", 1)

            tasks.append(task.strip())

        else:

            tasks.append(line)

    return tasks


# ----------------------------------------------------
# Generate Plan
# ----------------------------------------------------

def generate_plan(query: str) -> list[str]:
    """
    Generate research tasks from the user's query.
    """

    response = planner_chain.invoke(
        {
            "query": query
        }
    )

    return parse_plan(response)


# ----------------------------------------------------
# LangGraph Node
# ----------------------------------------------------

def planner_node(state: ResearchState) -> dict[str, Any]:
    """
    LangGraph Planner Node.

    Input:
        state

    Output:
        {
            "plan": [...],
            "current_task": "...",
            "next": "researcher"
        }
    """

    query = state["query"]

    plan = generate_plan(query)

    return {
        "plan": plan,
        "current_task": plan[0] if plan else "",
        "next": "researcher",
    }