import logging
from aiogram import Bot, Dispatcher, executor, types
import json

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
  await message.answer(f"Баланс: {str(balance)} руб.")
  await message.answer(
    f"""/start /help - Баланс, список команд с кратким описанием
/balance - Баланс
/categories - Выводит список категорий и кол-во записей по каждой категории
/cat_history имя категории - История категории, или всех категорий 
Имя_категории "amount + title" - добавляет в указанную категорию amount c описанием
/history ~ история - Выводит все траты с командой /del_n для удаления 
    """)

@dp.message_handler(commands=['balance'])
async def balance(message: types.Message):
  balance = database.take_balance()
  await message.reply(f'{balance} рублей')

@dp.message_handler(commands=['categories'])
async def categories(message: types.Message):
  category_status = database.take_category_status()
  await message.answer(category_status)
    

@dp.message_handler()
async def echo(message: types.Message):
  await message.answer(message.text)

if __name__ == '__main__':
  executor.start_polling(dp, skip_updates=True)