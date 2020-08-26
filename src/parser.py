from datetime import datetime

import numpy as np
import requests
from bs4 import BeautifulSoup, element


class DailyDataGrabber:
    """Grabs contributions data from the GitHub profile page"""

    def __init__(self, github_username):
        self.github_username = github_username
        self.date = None
        self.count = None

    def get(self) -> element.ResultSet:
        soup = self.open()
        con = soup.find_all(attrs={"class": "day"})
        return con

    def open(self) -> BeautifulSoup:
        url = f'https://github.com/{self.github_username}'
        webpage = requests.get(url)
        soup = BeautifulSoup(webpage.text, features="html5lib")
        return soup


class LastDate(DailyDataGrabber):
    """Grabs contributions data for the last available date"""

    def get_last(self):
        con = self.get()
        con_date = con[-1]['data-date']
        con_count = con[-1]['data-count']
        self.date = datetime.strptime(con_date, "%Y-%m-%d").date()
        self.count = int(con_count)


class AllDates(DailyDataGrabber):
    """Grabs contributions data for the last 365 days"""

    def get_all(self) -> dict:
        con = self.get()
        dct = dict()
        for i in con:
            dct[i['data-date']] = int(i['data-count'])
        return dct


class LastDateWithContrib(AllDates):
    """Grabs contributions data for the last date with at least one contribution"""

    def get_last_date_w_contrib(self):
        dates = self.get_all()
        counts = list(dates.values())
        last_non_zero_index = np.max(np.nonzero(counts))  # TODO: what if there are no contribs for 365 days?
        last_non_zero = list(dates.items())[last_non_zero_index]
        self.date = datetime.strptime(last_non_zero[0], "%Y-%m-%d").date()
        self.count = last_non_zero[1]


class NumberOfContinuousDays(LastDateWithContrib):
    """Gets number of continuous days of the last row of contributions"""

    def __init__(self, github_username):
        super().__init__(github_username)
        self.number_of_continuous_days = None

    def get_number_of_continuous_days(self):
        dates = self.get_all()
        dv = np.fromiter(dates.values(), dtype=int)
        contr_days = np.flatnonzero(dv)
        consecutive = np.split(contr_days, np.where(np.diff(contr_days) != 1)[0]+1)
        self.number_of_continuous_days = consecutive[-1].size


