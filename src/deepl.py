"""
Scripts for DeepL translation.
"""


from dotenv import load_dotenv

load_dotenv(verbose=True)
load_dotenv(".env")


import os
import requests


from model.paper import Paper


def translate(entry: Paper) -> str:
    params = {
        "auth_key": os.environ.get("DEEPL_API_KEY"),
        "text": entry.abstract,
        "source_lang": "EN",
        "target_lang": "JA",
    }
    request = requests.post("https://api-free.deepl.com/v2/translate", data=params)
    result = request.json()
    abstract_jap = result["translations"][0]["text"]
    message = "\n".join(
        [
            "<br>Title:  " + entry.title,
            "<br><br>URL: " + entry.url,
            "<br><br>Published: " + entry.date,
            "<br><br>JP_Abstract: " + abstract_jap,
        ]
    )
    return message
