#based on notes at https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_sql.html
import pandas as pd
import sqlite3 as db
import functions
connection = db.connect('my_db')
#create insert sql command; add parameters
#read the data into a dataframe; add data to that data frame; use to_sql to re-create that table
df2=pd.read_sql('Select * from customers', connection)
functions.print_it('table columns are ', df2.columns)
functions.print_it('new data', df2)
