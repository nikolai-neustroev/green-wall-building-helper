import pytest

from bot import ChatBot

config_file = '../bot.ini'


@pytest.fixture()
def bot() -> ChatBot:
    bot = ChatBot(config_file)
    return bot


def test_get_username(bot):
    bot.get_username()
    assert isinstance(bot.username, str)


def test_show_message(bot):
    bot.show_message()
    assert isinstance(bot.message, str)
