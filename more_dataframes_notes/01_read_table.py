import pandas as pd
import sqlite3 as db
import functions
file_name = 'ecars.db'
connection = db.connect(file_name)
tables_df = pd.read_sql("Select * from sqlite_master where type='table'", connection)
functions.print_it('tables', tables_df)

