# use sqlite3 package
import sqlite3
folder_name = '.'
file_name = 'my.db'
connection = sqlite3.connect(folder_name +'/' + file_name)
my_cursor = connection.cursor()
#Viewing the tables in the database
# Create a table
my_cursor.execute('''CREATE TABLE IF NOT EXISTS inventory
               (id INTEGER PRIMARY KEY, name TEXT, quantity INTEGER)''')

connection.commit()

data = [(1, 'Apple', 50),
        (2, 'Banana', 100),
        (3, 'Cherry', 150)]

# Perform bulk insert
my_cursor.executemany('INSERT INTO inventory VALUES (?,?,?)', data)
connection.commit()
#write code to verify the data has been stored <== TO DO


