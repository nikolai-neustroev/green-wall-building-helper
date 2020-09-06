import configparser
import logging

from aiogram import Bot, Dispatcher, executor, types

config_file = '../bot.ini'
config = configparser.ConfigParser()
config.read(config_file)
API_TOKEN = config['DEFAULT']['TELEGRAM_TOKEN']

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler()
async def echo(message: types.Message):
    await message.answer('yo')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
