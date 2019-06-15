import requests
from movie_scraper import MovieScraper

from config import TELEGRAM_SEND_MESSAGE_URL


class TelegramBot:

    def __init__(self):
        self.chat_id = None
        self.text = None
        self.first_name = None
        self.username = None
        self.outgoing_message_text = None
        self.incoming_message_text = None

    def parse_webhook_data(self, data):
        message = data['message']

        self.chat_id = message['chat']['id']
        self.incoming_message_text = message['text'].lower()
        self.first_name = message['from']['first_name']

    def action(self):
        success = None

        if self.incoming_message_text == '/hello':
            self.outgoing_message_text = "Hello {}!".format(self.first_name)
            success = self.send_message()
        if self.incoming_message_text == '/rad':
            self.outgoing_message_text = '🤙'
            success = self.send_message()
        else:
            self.outgoing_message_text = "We are looking for your movie..."
            self.send_message()
            try:
                self.outgoing_message_text = "\n\n".join(MovieScraper.get_movie(self.incoming_message_text))
                success = self.send_message()
            except TypeError:
                self.outgoing_message_text = "We couldn't find your movie 😕"
                success = self.send_message()

        return success

    def send_message(self):
        res = requests.get(TELEGRAM_SEND_MESSAGE_URL.format(self.chat_id, self.outgoing_message_text))
        return True if res.status_code == 200 else False

    @staticmethod
    def init_webhook(url):
        return requests.get(url)


