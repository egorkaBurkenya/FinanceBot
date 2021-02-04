import logging
from aiogram import Bot, Dispatcher, executor, types
import json

import init
import modules.sqlite3_module as database


with open('./configs/config.json', 'r', encoding='utf-8') as fh:
	config = json.load(fh)

API_TOKEN = config['Token']

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
  balance = database.take_balance()
  await message.reply(f"Баланс: {str(balance)} руб.")
  await message.reply(
    f"""/start /help - Баланс, список команд с кратким описанием
/balance - Баланс
/categories - Выводит список категорий и кол-во записей по каждой категории
/cat_history имя категории - История категории, или всех категорий 
Имя_категории "amount + title" - добавляет в указанную категорию amount c описанием
/history ~ история - Выводит все траты с командой /del_n для удаления 
    """)
    

@dp.message_handler()
async def echo(message: types.Message):
  await message.answer(message.text)

if __name__ == '__main__':
  executor.start_polling(dp, skip_updates=True)