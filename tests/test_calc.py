import pytest

from calc import Calc, MessageCreator


@pytest.fixture
def calc() -> Calc:
    calc = Calc('nikolai-neustroev')
    calc.get_day_count_since_last_contribution()
    return calc


@pytest.fixture
def msg_creator() -> MessageCreator:
    msg_creator = MessageCreator('nikolai-neustroev')
    msg_creator.make_decision()
    msg_creator.get_message()
    return msg_creator


def test_get_day_count_since_last_contribution(calc):
    assert isinstance(calc.day_count, int)


def test_make_decision(msg_creator):
    assert isinstance(msg_creator.decision, bool)


def test_get_message(msg_creator):
    assert isinstance(msg_creator.message, str)
