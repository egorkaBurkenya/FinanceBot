from Database.create_tables import init_database
from Database.sqlite_functions import sql_connection
from typing import NamedTuple
from loguru import logger

import os.path 


class AppFiles(NamedTuple):
  configs: bool
  configJson: bool 
  Database: bool
  create_tables: bool
  sqlite_functions: bool
  modules: bool
  unpucking_module: bool
  bot: bool

def check_the_pieces() -> tuple:
  return AppFiles(
  os.path.exists('./configs'),
  os.path.exists('./configs/config.json'),
  os.path.exists('./Database'),
  os.path.exists('./Database/create_tables.py'),
  os.path.exists('./Database/sqlite_functions.py'),
  os.path.exists('./modules'),
  os.path.exists('./modules/unpucking_module.py'),
  os.path.exists('./bot.py')
  )

con = sql_connection()

logger.debug(check_the_pieces())
logger.debug(init_database(con))