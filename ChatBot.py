import json
import requests
import time

from Google import (
    google_answer,
    google_image,
)
from Witai import (
    WitAi
)
from constants import (
    iter_hola,
    iter_gracias,
    iter_quien,
    iter_error,
)
import random


class ChatBot:

    def __init__(self, token, witai_token, witait_url):
        """
        :type token: Our Telegram BOT Api
        """
        self.token = token
        self.witai_token = witai_token
        self.witait_url = witait_url
        self.url = "https://api.telegram.org/bot" + token + "/"
        self.last_read_message = len(self.update()["result"])
        self.wit = WitAi(self.witai_token, self.witait_url)

    def start(self):
        while True:
            get_update = self.update()
            self.reply_to_messages(get_update)
            self.last_read_message = len(self.update()["result"])
            time.sleep(5)

    def update(self):
        reply = requests.get(self.url + "getUpdates")
        messages = reply.content.decode("utf8")
        return json.loads(messages)

    def reply_to_messages(self, get_update):
        if not get_update["ok"]:
            pass
        for message in get_update["result"][self.last_read_message:]:
            id_user = message["message"]["chat"]["id"]
            if "text" not in message['message']:
                self.send_reply("Solo puedo entender texto, amigo...", id_user)
            text = message['message']["text"]
            intent, body = self.wit.get_results(text)
            reply = self.get_reply(intent, body, text)
            self.send_reply(reply, id_user)

    @staticmethod
    def get_reply(intent, body, text):
        if intent == "edad" or intent == "altura":
            time.sleep(1)
            return f"La {intent} de {body} es {google_answer(body, intent)}"
        if intent == "imagen":
            time.sleep(1)
            return google_image(body)
        if intent == "hola":
            return random.choice(iter_hola)
        if intent == "gracias":
            return random.choice(iter_gracias)
        if intent == "quien":
            return random.choice(iter_quien)
        return random.choice(iter_error)
        # return search_duck_duck_go(text)

    def send_reply(self, reply, id_user):
        requests.get(self.url + "sendMessage?text=" + reply + "&chat_id=" + str(id_user))
