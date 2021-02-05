import sqlite3
from sqlite3 import Error

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


