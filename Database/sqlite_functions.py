import sqlite3
from sqlite3 import Error

from modules.unpucking_module import unpucking_sqlite_answer

def sql_connection():
  try:
    con = sqlite3.connect('./Database/mydatabase.db')
    return con
  except Error:
    print(Error)

def sql_insert(con, entities):
  cursorObj = con.cursor()
  cursorObj.execute('INSERT INTO employees(id, name, salary, department, position, hireDate) VALUES(?, ?, ?, ?, ?, ?)', entities)
  con.commit()


def sql_fetch(con) -> list:
  cursorObj = con.cursor()
  cursorObj.execute('SELECT * FROM employees')
  rows = cursorObj.fetchall()
  return unpucking_sqlite_answer(rows)


def sql_drop(con):
  cursorObj = con.cursor()
  cursorObj.execute('DROP table if exists employees')
  con.commit()



# con = sql_connection()
# sql_table(con)
# # sql_drop(con)

# # entities = (3, 'Egor', 800, 'IT', 'Tech', '2018-02-06')
# # sql_insert(con, entities)

# sql_fetch(con)
