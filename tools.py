from langchain.tools import tool
import requests
from bs4 import BeautifulSoup
from tavily import TavilyClient
from rich import print

import os
import json
from dotenv import load_dotenv
load_dotenv()

#Tavily tool
tavily = TavilyClient(
    api_key=os.getenv("TAVILY_API_KEY")
)
@tool
def web_search(query: str) -> str:
    """
    Search the web for recent and reliable information.
    Returns titles, URLs and snippets.
    """

    try:

        results = tavily.search(
    query="Nepal flood latest news August 2026",
    search_depth="basic",
    topic="news",
    max_results=10
)


        formatted_results = []

        for r in results.get("results", []):

            formatted_results.append({
                "title": r.get("title", "Untitled"),
                "url": r.get("url", ""),
                "snippet": r.get("content", "")[:500]
            })

        return json.dumps(
            formatted_results,
            ensure_ascii=False
        )

    except Exception as e:

        return json.dumps({
            "error": str(e)
        })
@tool
def web_search(query: str) -> str:
    """
    Search the web for recent and reliable information.
    Returns titles, URLs and snippets.
    """

    try:

        results = tavily.search(
            query=query,
            max_results=5
        )

        formatted_results = []

        for r in results.get("results", []):

            formatted_results.append({
                "title": r.get("title", "Untitled"),
                "url": r.get("url", ""),
                "snippet": r.get("content", "")[:500]
            })

        return json.dumps(
            formatted_results,
            ensure_ascii=False
        )

    except Exception as e:

        return json.dumps({
            "error": str(e)
        })
@tool
def web_search(query: str) -> str:
    """
    Search the web for recent and reliable information.
    Returns titles, URLs and snippets.
    """

    try:

        results = tavily.search(
            query=query,
            max_results=5
        )

        formatted_results = []

        for r in results.get("results", []):

            formatted_results.append({
                "title": r.get("title", "Untitled"),
                "url": r.get("url", ""),
                "snippet": r.get("content", "")[:500]
            })

        return json.dumps(
            formatted_results,
            ensure_ascii=False
        )

    except Exception as e:

        return json.dumps({
            "error": str(e)
        })@tool
def web_search(query: str) -> str:
    """
    Search the web for recent and reliable information.
    Returns titles, URLs and snippets.
    """

    try:

        results = tavily.search(
            query=query,
            max_results=5
        )

        formatted_results = []

        for r in results.get("results", []):

            formatted_results.append({
                "title": r.get("title", "Untitled"),
                "url": r.get("url", ""),
                "snippet": r.get("content", "")[:500]
            })

        return json.dumps(
            formatted_results,
            ensure_ascii=False
        )

    except Exception as e:

        return json.dumps({
            "error": str(e)
        })
@tool
def web_search(query: str) -> str:
    """
    Search the web for recent and reliable information.
    Returns titles, URLs and snippets.
    """

    try:

        results = tavily.search(
            query=query,
            max_results=5
        )

        formatted_results = []

        for r in results.get("results", []):

            formatted_results.append({
                "title": r.get("title", "Untitled"),
                "url": r.get("url", ""),
                "snippet": r.get("content", "")[:500]
            })

        return json.dumps(
            formatted_results,
            ensure_ascii=False
        )

    except Exception as e:

        return json.dumps({
            "error": str(e)
        })
@tool
def web_search(query: str) -> str:
    """
    Search the web for recent and reliable information.
    Returns titles, URLs and snippets.
    """

    try:

        results = tavily.search(
            query=query,
            max_results=5
        )

        formatted_results = []

        for r in results.get("results", []):

            formatted_results.append({
                "title": r.get("title", "Untitled"),
                "url": r.get("url", ""),
                "snippet": r.get("content", "")[:500]
            })

        return json.dumps(
            formatted_results,
            ensure_ascii=False
        )

    except Exception as e:

        return json.dumps({
            "error": str(e)
        })
@tool
def web_search(query: str) -> str:
    """
    Search the web for recent and reliable information.
    Returns titles, URLs and snippets.
    """

    try:

        results = tavily.search(
            query=query,
            max_results=5
        )

        formatted_results = []

        for r in results.get("results", []):

            formatted_results.append({
                "title": r.get("title", "Untitled"),
                "url": r.get("url", ""),
                "snippet": r.get("content", "")[:500]
            })

        return json.dumps(
            formatted_results,
            ensure_ascii=False
        )

    except Exception as e:

        return json.dumps({
            "error": str(e)
        })
@tool
def web_search(query: str) -> str:
    """
    Search the web for recent and reliable information.
    Returns titles, URLs and snippets.
    """

    try:

        results = tavily.search(
            query=query,
            max_results=5
        )

        formatted_results = []

        for r in results.get("results", []):

            formatted_results.append({
                "title": r.get("title", "Untitled"),
                "url": r.get("url", ""),
                "snippet": r.get("content", "")[:500]
            })

        return json.dumps(
            formatted_results,
            ensure_ascii=False
        )

    except Exception as e:

        return json.dumps({
            "error": str(e)
        })
@tool
def web_search(query: str) -> str:
    """
    Search the web for recent and reliable information.
    Returns titles, URLs and snippets.
    """

    try:

        results = tavily.search(
            query=query,
            max_results=5
        )

        formatted_results = []

        for r in results.get("results", []):

            formatted_results.append({
                "title": r.get("title", "Untitled"),
                "url": r.get("url", ""),
                "snippet": r.get("content", "")[:500]
            })

        return json.dumps(
            formatted_results,
            ensure_ascii=False
        )

    except Exception as e:

        return json.dumps({
            "error": str(e)
        })
@tool
def web_search(query: str) -> str:
    """
    Search the web for recent and reliable information.
    Returns titles, URLs and snippets.
    """

    try:

        results = tavily.search(
            query=query,
            max_results=5
        )

        formatted_results = []

        for r in results.get("results", []):

            formatted_results.append({
                "title": r.get("title", "Untitled"),
                "url": r.get("url", ""),
                "snippet": r.get("content", "")[:500]
            })

        return json.dumps(
            formatted_results,
            ensure_ascii=False
        )

    except Exception as e:

        return json.dumps({
            "error": str(e)
        })@tool
def web_search(query: str) -> str:
    """
    Search the web for recent and reliable information.
    Returns titles, URLs and snippets.
    """

    try:

        results = tavily.search(
            query=query,
            max_results=5
        )

        formatted_results = []

        for r in results.get("results", []):

            formatted_results.append({
                "title": r.get("title", "Untitled"),
                "url": r.get("url", ""),
                "snippet": r.get("content", "")[:500]
            })

        return json.dumps(
            formatted_results,
            ensure_ascii=False
        )

    except Exception as e:

        return json.dumps({
            "error": str(e)
        })
@tool
def web_search(query: str) -> str:
    """
    Search the web for recent and reliable information.
    Returns titles, URLs and snippets.
    """

    try:

        results = tavily.search(
            query=query,
            max_results=5
        )

        formatted_results = []

        for r in results.get("results", []):

            formatted_results.append({
                "title": r.get("title", "Untitled"),
                "url": r.get("url", ""),
                "snippet": r.get("content", "")[:500]
            })

        return json.dumps(
            formatted_results,
            ensure_ascii=False
        )

    except Exception as e:

        return json.dumps({
            "error": str(e)
        })
@tool
def web_search(query: str) -> str:
    """
    Search the web for recent and reliable information.
    Returns titles, URLs and snippets.
    """

    try:

        results = tavily.search(
            query=query,
            max_results=5
        )

        formatted_results = []

        for r in results.get("results", []):

            formatted_results.append({
                "title": r.get("title", "Untitled"),
                "url": r.get("url", ""),
                "snippet": r.get("content", "")[:500]
            })

        return json.dumps(
            formatted_results,
            ensure_ascii=False
        )

    except Exception as e:

        return json.dumps({
            "error": str(e)
        })
@tool
def web_search(query: str) -> str:
    """
    Search the web for recent and reliable information.
    Returns titles, URLs and snippets.
    """

    try:

        results = tavily.search(
            query=query,
            max_results=5
        )

        formatted_results = []

        for r in results.get("results", []):

            formatted_results.append({
                "title": r.get("title", "Untitled"),
                "url": r.get("url", ""),
                "snippet": r.get("content", "")[:500]
            })

        return json.dumps(
            formatted_results,
            ensure_ascii=False
        )

    except Exception as e:

        return json.dumps({
            "error": str(e)
        })
@tool
def web_search(query: str) -> str:
    """
    Search the web for recent and reliable information.
    Returns titles, URLs and snippets.
    """

    try:

        results = tavily.search(
            query=query,
            max_results=5
        )

        formatted_results = []

        for r in results.get("results", []):

            formatted_results.append({
                "title": r.get("title", "Untitled"),
                "url": r.get("url", ""),
                "snippet": r.get("content", "")[:500]
            })

        return json.dumps(
            formatted_results,
            ensure_ascii=False
        )

    except Exception as e:

        return json.dumps({
            "error": str(e)
        })

#Beautifulsoup tool
import requests
from bs4 import BeautifulSoup
from langchain_core.tools import tool


@tool
def scrape_webpage(url: str) -> str:
    """
    Scrape a webpage and return its clean text content from a given URL for deeper reading.

    Args:
        url: The URL of the webpage to scrape.

    Returns:
        Clean text extracted from the webpage.
    """

    try:
        headers = {
            "User-Agent": "Mozilla/5.0"
        }

        response = requests.get(
            url,
            headers=headers,
            timeout=10
        )

        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")

        # Remove unnecessary elements
        for element in soup([
            "script",
            "style",
            "nav",
            "footer",
            "header"
        ]):
            element.decompose()

        # Extract text
        text = soup.get_text(separator=" ", strip=True)

        return text[:3000]

    except requests.RequestException as e:
        return f"Error fetching webpage: {e}"

    except Exception as e:
        return f"Error scraping webpage: {e}"
        

