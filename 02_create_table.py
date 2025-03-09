import sqlite3 
folder_name = '.'
file_name = 'ecars2.db'
create_sql_statement = """
        CREATE TABLE countries (
        country text,
        continent text)
        """
connection = sqlite3.connect(folder_name +'/' + file_name)

try:
    cursor = connection.cursor()
    cursor.execute(create_sql_statement)
except sqlite3.Error as e:
    print(e)
else:
    print('created database table')
insert_sql_statement = """
    insert into countries(country, continent)
    values(?,?)
"""
try: 
    new_country = ('Japan' )
    cursor.execute(insert_sql_statement, new_country)
    connection.commit()
except sqlite3.Error as e:
    print(e)
else:
        print('added new_country')
# Does adding a record with a missing column create an error?  Find out <=== TO DO
# yes, it creates an error
        