import webbrowser
from utils import clean_input
from youtubesearchpython import VideosSearch

def youtube(text):
    tokens = clean_input(text)
    query = " ".join(tokens)

    search = VideosSearch(query, limit=1)
    results = search.result()
    first_result = results["result"][0]

    title = first_result["title"]
    print(f"Playing {title}")

    url = first_result["link"]
    webbrowser.open(url)

