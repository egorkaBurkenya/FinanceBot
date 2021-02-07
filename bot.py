import logging
from aiogram import Bot, Dispatcher, executor, types
import json

import modules.sqlite3_module as database
from modules.clear_module import clear_list


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

@dp.message_handler(commands=['cat_history'])
async def cat_history(message: types.Message):
  if len(message.text.split(' ')) < 2:
    category_history = database.take_cat_history()
    await message.answer(category_history)
  else: 
    category_history = database.take_cat_history(message.text.split(' ')[1])
    await message.reply(category_history)

@dp.message_handler(commands=['history'])
async def history(message: types.Message):
    history = database.take_history()
    try: await message.answer(history)
    except: await message.answer('Пусто')

@dp.message_handler()
async def echo(message: types.Message):
  if ':' in message.text:
    message_args = message.text.split(':')
    if message_args[0] in database.take_category_title():   
      amount = message_args[1].split(' ')
      amount = clear_list(amount, '')
      database.insert_amount(amount, message_args[0])
      await message.answer('Добавленно !')
  if '/del_' in message.text:
    amount_id = message.text.split('_')[1]
    database.delete_amount(amount_id)
    await message.answer('Удаленно')

if __name__ == '__main__':
  executor.start_polling(dp, skip_updates=True)
