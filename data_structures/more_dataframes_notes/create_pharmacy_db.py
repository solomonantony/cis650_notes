import sqlite3
#create the tables
with open('create_pharmacy.sql') as sql_file:
    sql_script = sql_file.read()

db = sqlite3.connect('pharmacy.db')
cursor = db.cursor()
cursor.executescript(sql_script)

#populate the tables
with open('populate_pharmacy.sql') as sql_file:
    sql_script = sql_file.read()
cursor.executescript(sql_script)

db.commit()
db.close()

                