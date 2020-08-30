import configparser

import requests

config = configparser.ConfigParser()
config.read('../bot.ini')
TELEGRAM_TOKEN = config['DEFAULT']['TELEGRAM_TOKEN']

url = 'https://api.telegram.org/bot'
updates = requests.get(url + TELEGRAM_TOKEN + '/getUpdates').json()
print(updates)
