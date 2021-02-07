import sqlite3
from sqlite3 import Error

def sql_create_table_history(con):
  cursorObj = con.cursor()
  cursorObj.execute(
    """CREATE TABLE IF NOT EXISTS history
    (
      id INTEGER PRIMARY KEY AUTOINCREMENT, 
      amount integer, 
      amountTitle text, 
      type integer, 
      createdDate text, 
      categoryId integer
      )"""
    )
  con.commit()

def sql_create_table_category(con):
  cursorObj = con.cursor()
  cursorObj.execute(
    """CREATE TABLE IF NOT EXISTS category
    (
      id integer PRIMARY KEY, 
      categoryTitle text, 
      worth integer
      )"""
    )
  con.commit()

def sql_insert_categories(con, values: list):
  cursorObj = con.cursor()
  for value in values:
    cursorObj.execute('INSERT INTO category(id, categoryTitle, worth) VALUES(?, ?, ?)', value)
  con.commit()

def init_database(con):
  if __name__ == '__main__':
    sql_create_table_category(con)
    sql_create_table_history(con)
    categories = [(
      1, "Такси", 1
      ),(
      2, "Еда", 0
      )]
    try:
      sql_insert_categories(con, categories)
      return "Tables have been created"
    except: 
      return "The categories have already been defined"

init_database(
  sqlite3.connect('./Database/mydatabase.db')
)