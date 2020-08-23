from datetime import datetime

import requests
from bs4 import BeautifulSoup


class DailyData:
    """Last contribution date"""

    def __init__(self, github_username):
        self.github_username = github_username
        self.date = None
        self.count = None

    def get(self):
        soup = self.open()
        con = soup.find_all(attrs={"class": "day"})[-1]
        con_date = con['data-date']
        con_count = con['data-count']
        self.date = datetime.strptime(con_date, "%Y-%m-%d").date()
        self.count = int(con_count)

    def open(self):
        url = f'https://github.com/{self.github_username}'
        webpage = requests.get(url)
        soup = BeautifulSoup(webpage.text, features="html5lib")
        return soup
