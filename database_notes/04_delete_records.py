# use sqlite3 package
import sqlite3
folder_name = '.'
file_name = 'ecars.db'
connection = sqlite3.connect(folder_name +'/' + file_name)
my_cursor = connection.cursor()
#print(my_cursor.execute('select * from sales where country = 'United States'))
delete_sql_statement = """
    delete from sales 
    where country = ? and 
    year = ?
    """
try:
    values = ('Canada', 2019)
    my_cursor.execute(delete_sql_statement, values )
    connection.commit()
except sqlite3.Error as e:
    print(e)
else:
    print('Delete completed')
# Does not running commit make an change?  Find out <=== TO DO
#No, changes anot made permanaent if there is no commit
    