import sqlite3
from sqlite3 import Error
from datetime import datetime
from .collected_module import collect_the_pieces

def con():
  try: 
    return sqlite3.connect('./Database/mydatabase.db')
  except Error:
    print(Error)

def take_balance() -> int: 
  cursorObj = con().cursor()
  cursorObj.execute("SELECT amount, type FROM history")
  amounts = cursorObj.fetchall()
  balance = 0
  for one_amount in amounts:
    if one_amount[1] == 0:
      balance -= one_amount[0]
    else: 
      balance += one_amount[0]
  return balance

def take_category_status() -> str:
  cursorObj = con().cursor()
  cursorObj.execute("SELECT c.categoryTitle, COUNT(h.id) FROM category as c LEFT JOIN history as h ON c.id = h.categoryId GROUP BY c.id ")
  categories = cursorObj.fetchall()
  cat_status = ''
  for i in categories: cat_status += f'{i[0]} - {i[1]}\n'
  return cat_status

def take_category_title() -> list:
  cursorObj = con().cursor()
  cursorObj.execute("SELECT categoryTitle FROM category")
  category_titles = cursorObj.fetchall()
  categories_titles = []
  for title in category_titles:
    categories_titles.append(title[0])
  return categories_titles

def take_cat_history(category: str = '') -> str:
  cursorObj = con().cursor()
  cursorObj.execute("SELECT c.categoryTitle, h.amount, h.amountTitle FROM history as h LEFT JOIN category as c ON c.id = h.categoryId ORDER BY c.categoryTitle")
  categories = cursorObj.fetchall()
  cat_history = ''
  for i in categories: 
    if category == '':
      cat_history += f'{i[0]}: {i[1]}руб. - {i[2]}\n'
    else: 
      if category == i[0]:
        cat_history += f'{i[0]}: {i[1]}руб. - {i[2]}\n'
  return cat_history

def insert_amount(amount: list, category: str) -> bool:
  add_datetime = str(datetime.now()).split('.')[0]
  conection = con()
  cursorObj = conection.cursor()
  cursorObj.execute(f"SELECT id, categoryTitle FROM category")
  categories_id = cursorObj.fetchall()
  for cat in categories_id:
    if cat[1] == category:
      category_id =  cat[0]
  cursorObj.execute(f"INSERT INTO history (amount, amountTitle, type, createdDate, categoryId) VALUES ({amount[0]}, '{collect_the_pieces(amount[1:-1])}', {1 if amount[-1] == '+' else 0 }, '{add_datetime}', {category_id})")
  conection.commit()

def take_history() -> str:
  cursorObj = con().cursor()
  cursorObj.execute("SELECT c.categoryTitle, h.type, h.amount, h.amountTitle, h.id FROM history as h LEFT JOIN category as c ON c.id = h.categoryId ORDER BY c.categoryTitle")
  history = cursorObj.fetchall()
  amounts_history = ''
  number = 0
  for one_amount in history:
    number += 1
    amounts_history += f"{one_amount[0]} - {'Потратил' if one_amount[1] == 0 else 'Получил'} {one_amount[2]} руб. {one_amount[3]} /del_{one_amount[4]}\n"  
  return amounts_history

def delete_amount(amount_id: str):
  conection = con()
  cursorObj = conection.cursor()
  cursorObj.execute(f"DELETE FROM history WHERE id = {int(amount_id)}")
  conection.commit()
