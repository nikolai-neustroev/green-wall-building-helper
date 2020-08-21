from bs4 import BeautifulSoup


class LastDate:
    """Last contribution date"""
    def __init__(self, html):
        self.html = html

    def get(self):
        soup = self.open()
        date = soup.find_all(attrs={"class": "day"})[-1]['data-date']
        count = soup.find_all(attrs={"class": "day"})[-1]['data-count']
        print(date)
        print(count)

    def open(self):
        with open(self.html, "r") as f:
            contents = f.read()
            soup = BeautifulSoup(contents, features="html5lib")
            return soup
