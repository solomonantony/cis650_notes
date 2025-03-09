# use sqlite3 package
import sqlite3
folder_name = '.'
file_name = 'ecars.db'
connection = sqlite3.connect(folder_name +'/' + file_name)
my_cursor = connection.cursor()
#Viewing the tables in the database
# reuse the code from 00_create_database.py to see the list of tables <=== TO DO 
sql_tables_list = """SELECT name FROM sqlite_master  WHERE type='table';"""
my_cursor = connection.execute(sql_tables_list)
print(my_cursor.fetchall())
my_cursor.execute('select * from sales')
rows = my_cursor.fetchall()
print(rows)
for row in rows:
  print(row)
#==  Viewing the column names of a table
#using cursor.description
column_names = [desc[0] for desc in my_cursor.description]
print(column_names)
#
#using the rows  of sqlite_schema table
my_cursor.execute('select * from sqlite_schema')
rows = my_cursor.fetchall()
for row in rows:
  print(row[4])
