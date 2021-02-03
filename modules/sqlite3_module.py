from Database.sqlite_functions import *

def take_balance() -> int: 
  con = sql_connection()
  amounts = sql_fetch(con, "amount, type")
  balance = 0
  for one_amount in amounts:
    if one_amount[1] == 0:
      balance -= one_amount[0]
    else: 
      balance += one_amount[0]
  return balance