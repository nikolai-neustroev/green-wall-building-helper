from datetime import date

from parser import LastDate


def test_last_date():
    ld = LastDate
    ld.get_last_date()
    assert isinstance(ld.last_date, date)
