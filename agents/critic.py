"""
agents/critic.py

Critic Agent

Responsibilities:
- Review the research collected so far.
- Identify missing or weak information.
- Decide whether another research iteration is required.
"""

from typing import Any

from langchain_core.output_parsers import JsonOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq

from config import (
    GROQ_API_KEY,
    MODEL_NAME,
    TEMPERATURE,
    MAX_ITERATIONS,
)

from graph.state import ResearchState


# -----------------------------------------------------
# LLM
# -----------------------------------------------------

llm = ChatGroq(
    model=MODEL_NAME,
    api_key=GROQ_API_KEY,
    temperature=TEMPERATURE,
)


# -----------------------------------------------------
# Prompt
# -----------------------------------------------------

critic_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
You are a senior research reviewer.

Review the collected research.

Your job is NOT to rewrite the research.

Instead decide whether more research is needed.

Return ONLY valid JSON.

Schema:

{
    "needs_more_research": true,
    "critique": "Explain what information is missing."
}

OR

{
    "needs_more_research": false,
    "critique": ""
}
"""
        ),
        (
            "human",
            """
Research Results:

{research}
"""
        ),
    ]
)


# -----------------------------------------------------
# Chain
# -----------------------------------------------------

critic_chain = (
    critic_prompt
    | llm
    | JsonOutputParser()
)


# -----------------------------------------------------
# LangGraph Node
# -----------------------------------------------------

def critic_node(state: ResearchState) -> dict[str, Any]:
    """
    Review research quality.
    """

    research = state.get("research_results", {})

    response = critic_chain.invoke(
        {
            "research": research
        }
    )

    needs_more = response.get(
        "needs_more_research",
        False,
    )

    critique = response.get(
        "critique",
        "",
    )

    iteration = state.get(
        "iteration",
        0,
    ) + 1

    # Stop looping if max iterations reached
    if iteration >= MAX_ITERATIONS:
        needs_more = False
        critique = ""

    return {
        "critique": critique,
        "iteration": iteration,
        "next": (
            "researcher"
            if needs_more
            else "summarizer"
        ),
    }