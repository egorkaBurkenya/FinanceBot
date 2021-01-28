import logging
from aiogram import Bot, Dispatcher, executor, types
import json

import init


with open('./configs/config.json', 'r', encoding='utf-8') as fh:
	config = json.load(fh)

API_TOKEN = config['Token']

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
  print(message)
  await message.reply("Hi!\nI'm EchoBot!\nPowered by aiogram.")

@dp.message_handler()
async def echo(message: types.Message):
  await message.answer(message.text)

if __name__ == '__main__':
  executor.start_polling(dp, skip_updates=True)
  
