"""
agents/summarizer.py

Summarizer Agent

Responsibilities:
- Combine research from all completed tasks.
- Remove repetition.
- Produce a structured summary.
"""

from typing import Any

from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq

from config import (
    GROQ_API_KEY,
    MODEL_NAME,
    TEMPERATURE,
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

summarizer_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
You are an expert technical writer.

Your job is to combine multiple research findings into
one well-organized summary.

Guidelines:

1. Remove duplicate information.
2. Keep important facts.
3. Organize logically.
4. Use clear headings.
5. Keep the writing factual.
6. Do not invent information.
7. Return Markdown.
"""
        ),
        (
            "human",
            """
Research Results

{research}
"""
        ),
    ]
)


# -----------------------------------------------------
# Chain
# -----------------------------------------------------

summarizer_chain = (
    summarizer_prompt
    | llm
    | StrOutputParser()
)


# -----------------------------------------------------
# LangGraph Node
# -----------------------------------------------------

def summarizer_node(state: ResearchState) -> dict[str, Any]:
    """
    Combine all research into a single summary.
    """

    research_results = state.get("research_results", {})

    research_text = ""

    for topic, content in research_results.items():

        research_text += f"\n\n## {topic}\n\n"

        research_text += content

    summary = summarizer_chain.invoke(
        {
            "research": research_text
        }
    )

    return {
        "summary": summary,
        "next": "reporter",
    }