import configparser

import requests


class Handler:
    def __init__(self, config_file: str):
        self.config_file = config_file
        self.token = None
        self.updates = None
        self.last_text = None

    def get_last_text(self):
        self.get_updates()
        message = self.updates['result'][-1]['message']
        if message['from']['is_bot']:
            print("Last result done by bot")
        else:
            self.last_text = message['text']

    def get_updates(self):
        self.get_token()
        url = 'https://api.telegram.org/bot'
        updates = requests.get(url + self.token + '/getUpdates').json()
        self.updates = updates

    # TODO: add check_updates(self) method

    def get_token(self):
        config = configparser.ConfigParser()
        config.read(self.config_file)
        self.token = config['DEFAULT']['TELEGRAM_TOKEN']
