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
