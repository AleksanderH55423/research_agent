import os
from tavily import TavilyClient
from dotenv import load_dotenv

load_dotenv()

tavily = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))


BLOCKED_DOMAINS = [
    "medium.com",
    "researchgate.net",
    "quora.com",
    "wiley.com"
]

def search_web(query: str, max_results: int = 5):
    results = tavily.search(query=query, max_results=max_results)
    structured = []

    for r in results["results"]:
        url = r["url"]

        if any(domain in url for domain in BLOCKED_DOMAINS):
            continue

        structured.append({
            "title": r["title"],
            "url": url,
            "snippet": r["content"]
        })

    return structured


if __name__ == "__main__":
    res = search_web("risks of synthetic data for AI models")
    for r in res:
        print(r["title"])
        print(r["url"])
        print("---")
