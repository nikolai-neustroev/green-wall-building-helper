from datetime import date

from parser import DailyData


def test_last_date():
    ld = DailyData('../page.html')
    ld.get()
    assert isinstance(ld.date, date)
