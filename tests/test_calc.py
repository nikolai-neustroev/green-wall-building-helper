from datetime import timedelta

import pytest

from calc import Calc


@pytest.fixture
def calc() -> Calc:
    calc = Calc('nikolai-neustroev')
    calc.get_day_count_since_last_contribution()
    return calc


def test_get_day_count_since_last_contribution(calc):
    assert isinstance(calc.day_count, timedelta)
