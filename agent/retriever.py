import requests
from bs4 import BeautifulSoup


def fetch_page_text(url: str, max_chars: int = 15000):
    """
    Fetches a webpage and returns cleaned text.
    Limits length to avoid huge pages.
    """

    try:
        headers = {
            "User-Agent": "Mozilla/5.0"
        }
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")

        # Remove scripts and styles
        for tag in soup(["script", "style", "noscript"]):
            tag.decompose()

        text = soup.get_text(separator=" ", strip=True)

        # Limit size so we don’t overload LLM
        return text[:max_chars]

    except Exception as e:
        print(f"Failed to fetch {url}: {e}")
        return None



if __name__ == "__main__":
    url = "https://www.ibm.com/think/insights/ai-synthetic-data"
    text = fetch_page_text(url)
    print(text[:1000])
