def sql_create_table_history(con):
  cursorObj = con.cursor()
  cursorObj.execute(
    """CREATE TABLE IF NOT EXISTS history
    (
      id integer PRIMARY KEY, 
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
  if __name__ != '__main__':
    sql_create_table_category(con)
    sql_create_table_history(con)
    categories = [(
      1, "1_Some Title", 1
      ),(
      2, "2_Some Title", 0
      )]
    try:
      sql_insert_categories(con, categories)
      return "Tables have been created"
    except: 
      return "The categories have already been defined"