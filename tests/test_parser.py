from datetime import date

import pytest

from parser import LastDate, LastDateWithContrib, NumberOfContinuousDays

username = 'nikolai-neustroev'


@pytest.fixture
def ld() -> LastDate:
    ld = LastDate(username)
    ld.get_last()
    return ld


@pytest.fixture
def ldwc() -> LastDateWithContrib:
    ldwc = LastDateWithContrib(username)
    ldwc.get_last_date_w_contrib()
    return ldwc


@pytest.fixture
def nocd() -> NumberOfContinuousDays:
    nocd = NumberOfContinuousDays(username)
    nocd.get_number_of_continuous_days()
    return nocd


def test_daily_data_last_date(ld):
    assert isinstance(ld.date, date)


def test_daily_data_last_count(ld):
    assert isinstance(ld.count, int)


def test_get_last_date_w_contrib_date(ldwc):
    assert isinstance(ldwc.date, date)


def test_get_last_date_w_contrib_count(ldwc):
    assert isinstance(ldwc.count, int)


def test_get_number_of_continuous_days(nocd):
    assert isinstance(nocd.number_of_continuous_days, int)
