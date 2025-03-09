import sqlite3
import os
def create_sqlite_database(filename):
    """ create a database connection to an SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(filename)
    except sqlite3.Error as e:
        print(e)
    else:
        print('Created the database file.')
    finally:
        if conn:
            conn.close()

if __name__ == '__main__':
    create_sqlite_database("my.db")
    #use the os package to verify that my.db file has been created <====  TO DO
    files_list = os.listdir()
    if 'my.db' in files_list:
        print('file exists')
    connection = sqlite3.connect('my.db')
    sql_tables_list = """SELECT name FROM sqlite_master  WHERE type='table';"""
    my_cursor = connection.execute(sql_tables_list)
    print(my_cursor.fetchall())





