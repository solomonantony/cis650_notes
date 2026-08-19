import pandas as pd #alias
import functions
# creating from a list of lists
data = [['Alex', 10], ['Bob', 12], ['Ali', 13]]
df4 = pd.DataFrame(data)
functions.print_it('original list of lists', data)
functions.print_it('creating from a list of lists', df4)
# create another dataframe from lists and print it <<< TO DO
data = [['Alex', 10, 'xyz'], ['Bob', 12], ['Ali', 13], ['Jon',None,'ert']]
df4 = pd.DataFrame(data)
functions.print_it('original list of lists', data)
functions.print_it('creating from a list of lists', df4)

