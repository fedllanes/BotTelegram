import requests


class WitAi:

    def __init__(self, token, url):
        self.token = token
        self.authentication = {"Authorization":
                                   "Bearer PJH3TFS3CE2SZNZ5AI74VF33JLPV4E6E"}
        self.url = 'https://api.wit.ai/message?v=20210511&q='

    def query(self, query):
        response = requests.get(self.url + query, headers=self.authentication)
        response = response.json()
        return response

    @staticmethod
    def parse_query(response):
        if response["intents"]:
            intent = response["intents"][0]["name"]
        else:
            intent = None
        if response["entities"]:
            body = next(iter(response["entities"].values()))[0]["value"]
        else:
            body = None
        return intent, body

    def get_results(self, query):
        response = self.query(query)
        intent, body = self.parse_query(response)
        return intent, body
