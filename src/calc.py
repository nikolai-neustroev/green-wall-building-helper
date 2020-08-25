from datetime import datetime

from parser import LastDateWithContrib


class Calc:
    def __init__(self, github_username):
        self.github_username = github_username
        self.day_count = None

    def get_day_count_since_last_contribution(self):
        last_contribution = LastDateWithContrib(self.github_username)
        last_contribution.get_last_date_w_contrib()
        today = datetime.today().date()
        self.day_count = today - last_contribution.date
