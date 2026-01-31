import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv(override=True)
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def extract_evidence(page_text: str):
    """
    Uses an LLM to extract structured research evidence from webpage text.
    """

    prompt = f"""
You are an AI research analyst.

From the text below, extract:
- Claims about synthetic data in training AI models
- Supporting evidence for each claim
- Label whether it is a RISK or BENEFIT
- Give a confidence score from 0 to 1

Return as JSON list like:
[
  {{
    "claim": "...",
    "evidence": "...",
    "type": "risk or benefit",
    "confidence": 0.85
  }}
]

TEXT:
{page_text[:12000]}
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.2
    )

    return response.choices[0].message.content


if __name__ == "__main__":
    sample_text = """
    Synthetic data can help scale AI training while preserving privacy.
    However, it may introduce distribution shift and bias amplification.
    """
    print(extract_evidence(sample_text))