from tools import format_search_results, scrape_url, web_search


def _clean_result_text(text: str) -> str:
    return " ".join(text.split())


def _make_report(topic: str, search_response: dict, scraped_content: str) -> str:
    answer = search_response.get("answer") or "Tavily returned source results for this topic."
    results = search_response.get("results", [])

    source_lines = []
    finding_lines = []

    for index, result in enumerate(results, start=1):
        title = result.get("title", "Untitled source")
        url = result.get("url", "")
        snippet = _clean_result_text(result.get("content", "").strip())

        if snippet:
            finding_lines.append(f"{index}. **{title}**\n\n   {snippet}")

        if url:
            source_lines.append(f"- [{title}]({url})")

    if not finding_lines:
        finding_lines.append("1. Tavily did not return detailed snippets for this topic.")

    return f"""# Research Report: {topic}

## Introduction

{answer}

## Key Findings

{chr(10).join(finding_lines)}

## Scraped Content Summary

{scraped_content[:1800] if scraped_content else "No page content could be scraped from the returned sources."}

## Conclusion

This report is generated using Tavily search results and direct webpage scraping only.

## Sources

{chr(10).join(source_lines) if source_lines else "- No source URLs returned."}
"""


def _make_feedback(search_response: dict, scraped_content: str) -> str:
    result_count = len(search_response.get("results", []))
    scraped_ok = bool(scraped_content and not scraped_content.startswith("Could not scrape URL"))

    return f"""Score: Tavily-only mode

Strengths:
- Used {result_count} Tavily search result(s).
- {"Successfully scraped one source for deeper content." if scraped_ok else "Search results were collected even though scraping was limited."}

Areas to Improve:
- This version is template-based, so the writing is simpler than a model-generated report.
- Use more source-specific formatting later if you want richer summaries and critique.

One line verdict:
The app is now working in Tavily-only mode.
"""


def run_research_pipeline(topic: str) -> dict:
    search_response = web_search(
        f"Find recent, reliable and detailed English-only information about: {topic}. "
        "Return English sources and English summaries only."
    )
    search_text = format_search_results(search_response)

    top_url = ""
    for result in search_response.get("results", []):
        if result.get("url"):
            top_url = result["url"]
            break

    scraped_content = scrape_url(top_url) if top_url else "No URL was available to scrape."
    report = _make_report(topic, search_response, scraped_content)
    feedback = _make_feedback(search_response, scraped_content)

    return {
        "search": search_text,
        "reader": scraped_content,
        "writer": report,
        "critic": feedback,
    }


if __name__ == "__main__":
    topic_value = input("\nEnter a research topic: ")
    result = run_research_pipeline(topic_value)
    print(result["writer"])
