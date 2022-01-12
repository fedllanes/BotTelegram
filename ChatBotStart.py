from ChatBot import ChatBot

WITAI_CHAT_TOKEN = ""
WITAI_URL = ""
TELEGRAM_TOKEN = ""

if __name__ == "__main__":
    while True:
        print("Buenas, el bot se encontrará encendido en @bigdataimfbot")
        chatbot = ChatBot(TELEGRAM_TOKEN, WITAI_CHAT_TOKEN, WITAI_URL)
        chatbot.start()
        try:
            chatbot = ChatBot(TELEGRAM_TOKEN, WITAI_CHAT_TOKEN, WITAI_URL)
            chatbot.start()
        except:
            print("error en el bot, reiniciando...")
