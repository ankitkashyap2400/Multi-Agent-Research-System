"""
agents/reporter.py

Final Report Generator

Responsibilities:
- Convert summary into a professional report
- Format using Markdown
- Return report to LangGraph state
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

report_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
You are an expert technical report writer.

Transform the summary into a professional research report.

Requirements:

1. Use Markdown.
2. Create an attractive title.
3. Add a short introduction.
4. Organize with headings.
5. Use bullet points where appropriate.
6. Add a conclusion.
7. Keep the report factual.
8. Do not invent information.
"""
        ),
        (
            "human",
            """
Topic

{query}

Summary

{summary}
"""
        ),
    ]
)


# -----------------------------------------------------
# Chain
# -----------------------------------------------------

report_chain = (
    report_prompt
    | llm
    | StrOutputParser()
)


# -----------------------------------------------------
# LangGraph Node
# -----------------------------------------------------

def reporter_node(state: ResearchState) -> dict[str, Any]:
    """
    Generate the final report.
    """

    report = report_chain.invoke(
        {
            "query": state["query"],
            "summary": state["summary"],
        }
    )

    return {
        "report": report,
        "next": "end",
    }