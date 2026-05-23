import os
import re

import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
from tavily import TavilyClient

load_dotenv()


def get_tavily_client() -> TavilyClient:
    api_key = os.getenv("TAVILY_API_KEY")
    if not api_key or api_key == "your_tavily_api_key_here":
        raise RuntimeError("TAVILY_API_KEY is missing. Add your Tavily key to the .env file.")
    return TavilyClient(api_key=api_key)


def web_search(query: str, max_results: int = 5) -> dict:
    """Search the web with Tavily and return Tavily's structured response."""
    return get_tavily_client().search(
        query=query,
        max_results=max_results,
        include_answer=True,
        search_depth="advanced",
        topic="general",
    )


def format_search_results(search_response: dict) -> str:
    out = []

    if search_response.get("answer"):
        out.append(f"Tavily Answer:\n{search_response['answer']}")

    for result in search_response.get("results", []):
        out.append(
            "Title: {title}\nURL: {url}\nSnippet: {snippet}".format(
                title=result.get("title", "Untitled"),
                url=result.get("url", "No URL"),
                snippet=result.get("content", "")[:500],
            )
        )

    return "\n\n----\n\n".join(out)


def _english_score(text: str) -> float:
    letters = [char for char in text if char.isalpha()]
    if not letters:
        return 1.0
    ascii_letters = [char for char in letters if char.isascii()]
    return len(ascii_letters) / len(letters)


def _clean_english_text(text: str, limit: int = 3000) -> str:
    blocked_phrases = (
        "jump to content",
        "search search",
        "edit links",
        "from wikipedia",
        "free encyclopedia",
        "not to be confused",
        "for other uses",
        "languages",
        "appearance",
        "contents",
        "main menu",
    )

    text = re.sub(r"\[[^\]]*\]", "", text)
    text = re.sub(r"\s+", " ", text).strip()
    rough_sentences = re.split(r"(?<=[.!?])\s+", text)

    cleaned = []
    for sentence in rough_sentences:
        sentence = sentence.strip(" -|•\t\r\n")
        lower = sentence.lower()

        if len(sentence) < 45:
            continue
        if any(phrase in lower for phrase in blocked_phrases):
            continue
        if _english_score(sentence) < 0.88:
            continue

        cleaned.append(sentence)
        if len(" ".join(cleaned)) >= limit:
            break

    return " ".join(cleaned)[:limit].strip()


def scrape_url(url: str) -> str:
    """Scrape and return clean text content from a given URL for deeper reading."""
    try:
        resp = requests.get(
            url,
            timeout=8,
            headers={
                "User-Agent": "Mozilla/5.0",
                "Accept-Language": "en-US,en;q=0.9",
            },
        )
        resp.raise_for_status()
        soup = BeautifulSoup(resp.text, "html.parser")
        for tag in soup(["script", "style", "nav", "footer", "header", "aside", "form", "table"]):
            tag.decompose()

        main = (
            soup.find("main")
            or soup.find("article")
            or soup.find(id="mw-content-text")
            or soup.find(class_="mw-parser-output")
            or soup.body
            or soup
        )

        paragraphs = [
            paragraph.get_text(separator=" ", strip=True)
            for paragraph in main.find_all("p")
            if paragraph.get_text(strip=True)
        ]
        raw_text = " ".join(paragraphs) if paragraphs else main.get_text(separator=" ", strip=True)
        cleaned = _clean_english_text(raw_text)
        return cleaned or "Could not extract enough English article text from this source."
    except Exception as exc:
        return f"Could not scrape URL: {exc}"
