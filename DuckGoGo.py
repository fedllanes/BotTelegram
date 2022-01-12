import json
import requests


def search_duck_duck_go(query):
    url = "http://api.duckduckgo.com/?q=" + query.replace(" ", "+") + "&format=json"
    response = requests.get(url)
    response_json = json.loads(response.text)
    if response_json["RelatedTopics"]:
        return response_json["RelatedTopics"][0]["Text"]
    return f"No se ha encontrado información sobre {query}, intente de nuevo"
