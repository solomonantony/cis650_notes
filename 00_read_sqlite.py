#use a connection and an SELECT sql command to read data into a data frame
# refer to https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_sql.html
# for notes on using read_sql
import pandas as pd
import sqlite3 as db
import functions
file_name = 'ecars.db'
connection = db.connect(file_name)
countries_df2 = pd.read_sql('Select * from countries', connection)
functions.print_it('df directly from query result: ', countries_df2)
# create a dataframe that uses sales data and stores it to a dataframe <<<< TO DO
