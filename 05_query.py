# use sqlite3 package
import sqlite3
folder_name = '.'
file_name = 'ecars.db'
connection = sqlite3.connect(folder_name +'/' + file_name)
my_cursor = connection.cursor()
query_statement = """
    Select * from sales
    where country = ? and year = ?
    """
values = ('Japan', 2017)
#use the cursor's fetchone() method to verify the result <=== TO DO


