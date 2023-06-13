"""
For arxiv.
"""
import requests
from process.xml import parse


def fetch():
    """
    Fetch papers from arxiv.org
    """
    query = "recommend"
    url = (
        "http://export.arxiv.org/api/query?search_query="
        + query
        + "&start=0&max_results=100&sortBy=submittedDate&sortOrder=descending"
    )
    try:
        response = requests.get(url, timeout=10)
    except Exception as error:
        raise error
    return parse(response.text, "entry")
