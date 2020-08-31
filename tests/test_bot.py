import pytest

from bot import Handler

config_file = '../bot.ini'


@pytest.fixture()
def handler() -> Handler:
    handler = Handler(config_file)
    return handler


def test_get_token(handler):
    handler.get_token()
    assert isinstance(handler.token, str)


def test_get_updates(handler):
    handler.get_updates()
    assert isinstance(handler.updates, dict)


def test_get_last_text(handler):
    handler.get_last_text()
    assert isinstance(handler.last_text, str)
