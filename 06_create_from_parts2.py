import pandas as pd #alias
import functions
grades_dict = {'Wally': [87, 96, 70],
               'Eva': [100, 87, 90],
               'Sam': [94, 77, 90],
               'Katie': [100, 81, 82],
               'Bob': [83, 65, 85]}
grades_df = pd.DataFrame(grades_dict)
grades_df.index = ['test1', 'test2', 'test3']
functions.print_it('Dictionary entries', grades_df)
# create a dataframe with 3-digit student numbers as index, 
# and data that stores three quiz grades  <<< TO DO
grades2_dictionary = {'name':['Samir', 'Lana', 'Xav'],
                      'quiz1': [99, 87, 22],
                      'quiz2':[67, 56, 33],
                      'quiz3':[90, 98, 95]}
grades2_df = pd.DataFrame(grades2_dictionary)
grades2_df.index = [354, 988, 102]
functions.print_it('Grade book 2', grades2_df)
