import pandas as pd
import sqlite3 as db
import functions
connection = db.connect('my_db')
connection.set_trace_callback(print) #prints the query 
cursor = connection.cursor()
#view all the records
results = pd.read_sql("Select * from users", connection)
functions.print_it('All records: ', results)
#view some records
user_input = input('Enter user name: ')
cursor.execute("SELECT * from users WHERE name = :name", {'name':user_input})
result = cursor.fetchall()
functions.print_it('Selected record:', result)



