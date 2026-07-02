"""
app.py

Entry point for the Multi-Agent Research Assistant.
"""

from graph.workflow import graph


def main():

    print("=" * 70)
    print("        Multi-Agent Research Assistant")
    print("=" * 70)

    query = input("\nEnter your research topic:\n> ")

    initial_state = {
        "messages": [],
        "query": query,
        "plan": [],
        "current_task": "",
        "research_results": {},
        "critique": "",
        "summary": "",
        "report": "",
        "iteration": 0,
        "next": "planner",
    }

    config = {
        "configurable": {
            "thread_id": "research-session"
        }
    }

    final_state = graph.invoke(
        initial_state,
        config=config,
    )

    print("\n")
    print("=" * 70)
    print("FINAL REPORT")
    print("=" * 70)

    print(final_state["report"])

    with open(
        "output/report.md",
        "w",
        encoding="utf-8"
    ) as file:

        file.write(final_state["report"])

    print("\n")
    print("Report saved to output/report.md")


if __name__ == "__main__":
    main()