from planner import create_research_plan
from search_tool import search_web
from retriever import fetch_page_text
from extractor import extract_evidence
from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv(override=True)
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


# Actually running  the research agent
def run_research_agent(user_question: str, max_tasks: int = 3):
    print("Planning research...")
    plan = create_research_plan(user_question)

    evidence_db = []

    for i, task in enumerate(plan[:max_tasks]):
        print(f"\nTask {i+1}: {task}")

        results = search_web(task)

        for r in results[:2]:  # limit pages per task
            print(f"Reading: {r['title']}")

            page_text = fetch_page_text(r["url"])
            if not page_text:
                continue

            print("Extracting evidence...")
            extracted = extract_evidence(page_text)

            evidence_db.append({
                "task": task,
                "source": r["url"],
                "evidence": extracted
            })

    return evidence_db


# Generating a markdown report.
from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv(override=True)
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def generate_markdown_report(user_question: str, evidence_db):
    evidence_text = "\n".join([
        f"TASK: {e['task']}\nSOURCE: {e['source']}\nEVIDENCE: {e['evidence']}\n"
        for e in evidence_db
    ])

    prompt = f"""
You are a research report writer.

Using the extracted evidence below, produce a structured Markdown research report.

Structure:
# Research Report
## Research Question
## Key Benefits
## Key Risks
## Evaluation and Quality Concerns
## Summary

For each claim:
- List the claim
- Provide the supporting evidence
- Cite the source URL

RESEARCH QUESTION:
{user_question}

EVIDENCE:
{evidence_text}
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3
    )
    return response.choices[0].message.content




if __name__ == "__main__":
    question = "What are the real-world risks and benefits of using synthetic data to train large language models?"

    evidence_db = run_research_agent(question)

    print("\nGenerating Markdown report...")
    report = generate_markdown_report(question, evidence_db)

    with open("research_report.md", "w", encoding="utf-8") as f:
        f.write(report)

    print("Report saved to research_report.md")
