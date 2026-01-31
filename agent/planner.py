import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv(override=True)
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def create_research_plan(user_question: str):
    """
    Uses an LLM to break a research question into structured research tasks.
    """

    prompt = f"""
You are a research planning assistant.

Break the following research question into 4–6 concrete research tasks.

Rules:
- Each task should represent a distinct investigation angle.
- Focus on risks, benefits, technical concerns, evaluation issues, and bias when relevant.
- Keep each task short (one sentence).
- Do NOT answer the question, only produce tasks.

Research Question:
{user_question}

Return the result as a numbered list.
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3
    )

    text = response.choices[0].message.content

    # Convert numbered list → Python list
    tasks = []
    for line in text.split("\n"):
        line = line.strip()
        if line and line[0].isdigit():
            task = line.split(".", 1)[1].strip()
            tasks.append(task)

    return tasks



if __name__ == "__main__":
    q = "What are the real-world risks and benefits of synthetic data for LLMs?"
    plan = create_research_plan(q)
    print(plan)
