import sqlite3 as sql
connection = sql.connect('database.db')
cursor = connection.cursor()
create_table = "CREATE TABLE IF NOT EXISTS users(id integer primary key,username text, password text)"
cursor.execute(create_table)
create_table = "CREATE TABLE IF NOT EXISTS items(id integer primary key,name text, price real)"
cursor.execute(create_table)
connection.commit()
connection.close()
