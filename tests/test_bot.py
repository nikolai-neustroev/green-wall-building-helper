import pytest

from bot import ChatBot


@pytest.fixture()
def bot() -> ChatBot:
    bot = ChatBot
    return bot


def test_get_username(bot):
    assert False


def test_show_message(bot):
    assert False
