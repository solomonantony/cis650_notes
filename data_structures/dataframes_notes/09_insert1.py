
import pandas as pd #alias
import functions
df1 = pd.DataFrame()
functions.print_it('Empty dataframe', df1)
new_df = pd.DataFrame({'column1': [1, 2, 3], 'column2': [4, 5, 6]}, 
                      index=['a', 'b', 'c'])
df1 = pd.concat([df1,new_df])
functions.print_it('from balnk', df1)
# add another row to df1 and print it <<<< TO DO
