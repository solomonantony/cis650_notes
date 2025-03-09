import pandas as pd #alias
import functions
data = [1,2,3,4,5]
df3 = pd.DataFrame(data)
functions.print_it('original list', data)
functions.print_it('creating from a list', df3)
# create another dataframe from a list and print it <<< TO DO
data = ['a', 'b', 'c']
df3 = pd.DataFrame(data)
functions.print_it('original list', data)
functions.print_it('creating from a list', df3)