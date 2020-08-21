from datetime import date

from parser import LastDate


def test_last_date():
    ld = LastDate('../page.html')
    ld.get()
    assert isinstance(ld.date, date)
