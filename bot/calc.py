from datetime import datetime

from bot.parser import LastDateWithContrib, NumberOfContinuousDays


class Calc:
    """Calculates the difference between today and last contribution date"""

    def __init__(self, github_username):
        self.github_username = github_username
        self.day_count = None

    def get_day_count_since_last_contribution(self):
        last_contribution = LastDateWithContrib(self.github_username)
        last_contribution.get_last_date_w_contrib()
        today = datetime.today().date()
        day_count = today - last_contribution.date
        self.day_count = day_count.days


class ReportCreator(Calc):
    """Creating a message based on contribution data"""

    def __init__(self, github_username):
        super().__init__(github_username)
        self.decision = None
        self.report = None

    def make_decision(self):
        self.get_day_count_since_last_contribution()
        self.decision = True if self.day_count == 0 else False  # TODO: What if calc.day_count is negative?

    def get_report(self):
        self.make_decision()
        if self.decision is True:
            nocd = NumberOfContinuousDays(self.github_username)  # TODO: refactor code so to avoid querying page twice
            nocd.get_number_of_continuous_days()
            self.report = f"{nocd.number_of_continuous_days} days in a row! Keep it up!"
        else:
            self.report = f"{self.day_count} day(s) with no contributions."
