import sqlite3

connection  = sqlite3.connect('data.db')
cursor = connection.cursor()

create_table = "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username text, password text)"
cursor.execute(create_table)

create_table = "CREATE TABLE IF NOT EXISTS items (name text, price real)"
cursor.execute(create_table)

connection.commit()

connection.close()



# if u want to use auto increment feature in sqlite then u ahve to use INTEGER instead of just int keyword, 
# this is how it is gonna do increment. and also specify PRIMARY KEY. 
# for the things which are auto incrementing u will specify NULL.  