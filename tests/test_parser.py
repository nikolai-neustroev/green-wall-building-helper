from datetime import date

import pytest

from parser import DailyData


@pytest.fixture
def ld() -> DailyData:
    ld = DailyData('nikolai-neustroev')
    ld.get()
    return ld


def test_daily_data_date(ld):
    assert isinstance(ld.date, date)


def test_daily_data_count(ld):
    assert isinstance(ld.count, int)
