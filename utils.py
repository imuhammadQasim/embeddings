import requests
import feedparser
import fitz
from urllib.parse import quote


def search_arxiv(query):
    query = quote(query)

    base_url = (
        "http://export.arxiv.org/api/query?"
        f"search_query=all:{query}"
        "&start=0"
        "&max_results=1"
    )

    feed = feedparser.parse(base_url)

    if len(feed.entries) == 0:
        return None

    paper = feed.entries[0]

    return {
        "title": paper.title,
        "authors": [a.name for a in paper.authors],
        "summary": paper.summary,
        "published": paper.published,
        "pdf_url": paper.links[1].href
    }

def download_pdf(pdf_url):

    response = requests.get(pdf_url)

    filename = "paper.pdf"

    with open(filename, "wb") as f:
        f.write(response.content)

    return filename


def extract_text(pdf_path):

    doc = fitz.open(pdf_path)

    text = ""

    for page in doc:
        text += page.get_text()

    return text