import configparser
import logging
from pathlib import Path

from aiogram import Bot, Dispatcher, executor, types

from bot.calc import ReportCreator

config_file = Path('bot.ini')
config = configparser.ConfigParser()
config.read(config_file)
API_TOKEN = config['DEFAULT']['TELEGRAM_TOKEN']

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.answer("Please enter your Github username")


@dp.message_handler()
async def receive_username(message: types.Message):
    """
    This handler will be called when user sends Github username
    """
    rc = ReportCreator(message.text)
    rc.get_report()
    await message.answer(rc.report)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
