from Database.create_tables import init_database
from Database.sqlite_functions import sql_connection
from loguru import logger

con = sql_connection()
logger.debug(init_database(con))