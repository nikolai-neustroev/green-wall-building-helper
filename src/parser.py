from datetime import datetime

from bs4 import BeautifulSoup


class DailyData:
    """Last contribution date"""
    def __init__(self, html):
        self.html = html
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
        with open(self.html, "r") as f:
            contents = f.read()
            soup = BeautifulSoup(contents, features="html5lib")
            return soup
