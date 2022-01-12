from bs4 import BeautifulSoup
import re
import requests


def google_answer(query, intent):
    url = "https://google.com/search?lr=lang_en&q=" + query.replace(" ", "+") + "+" + intent
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit 537.36 (KHTML, like Gecko) Chrome",
        "Accept": "text/html,application/xhtml+xml,application/xml; q=0.9,image/webp,*/*;q=0.8"}
    request_result = requests.get(url, headers=headers)
    soup = BeautifulSoup(request_result.text, "html.parser")
    try:
        if intent == "edad":
            return re.findall("Age([0-9]{2})", soup.text)[0] + " Años"
        if intent == "altura":
            return re.findall("Height(1..)", soup.text)[0] + " Metros"
    except:
        return f"No conozco nada sobre {query}"
    return "No encontré nada :((("


def google_image(query):
    url = "https://www.bing.com/images/search?q=" + query.replace(" ", "+") + "&form=QBLH"
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) "
                      "AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Safari/605.1.15",
        "Accept": "text/html,application/xhtml+xml,application/xml; q=0.9,image/webp,*/*;q=0.8"}
    request_result = requests.get(url, headers=headers)
    soup = BeautifulSoup(request_result.text, "html.parser")
    return re.findall("murl\":.+\"(https:[^\"]*jpg)\"", str(soup))[0]
