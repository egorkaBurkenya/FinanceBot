import sqlite3
from sqlite3 import Error

from modules.unpucking_module import unpucking_sqlite_answer

def sql_connection():
  try:
    con = sqlite3.connect('./Database/mydatabase.db')
    return con
  except Error:
    print(Error)

def sql_insert(con: sqlite3.connect, 
              values: tuple, 
              table="history", 
              columns="id, amount, amountTitle, type, createdDate, categoryId"):
  cursorObj = con.cursor()
  cursorObj.execute(f'INSERT INTO {table}({columns}) VALUES(?, ?, ?, ?, ?, ?)', values)
  con.commit()


def sql_fetch(con, columns="*", table="history") -> list:
  cursorObj = con.cursor()
  cursorObj.execute(f'SELECT {columns} FROM {table}')
  rows = cursorObj.fetchall()
  return unpucking_sqlite_answer(rows)