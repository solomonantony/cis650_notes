"""
Creating a dicitonary
Create a dictionary by enclosing in curly braces, {}, a comma-separated list of key–value pairs, each of the form key: value.
key and its related value are separated by a colon
"""
dictionary0 = {}
print('dictionary0',dictionary0)
dictionary1 = dict()
dictionary2 = dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
print('dictionary2', )
dictionary3 = dict(sape=4139, guido=4127, jack=4098)
print('dictionary3', dictionary3)
country_codes = {'Finland': 'fi', 'South Africa': 'za', 'Nepal': 'np'}
print('country_codes', country_codes)
"""
Using zip to create a dictionary
Combine two lists to create a dictionary
items from the first list become the keys
items from the second list become the corresponding values
"""
names = ['bob', 'ken', 'ron']
grades = [98, 76, 80]
studentGrades = dict(zip(names, grades))
print("studentGrades",studentGrades)
"""
Dictionary Comprehensions
You can create a dictionary by dynamically creating the key value pairs.

The syntax is similar to list a comprehension
"""
myNumbers = {1:1, 2:2, 3:3, 4:4}
mySquares = {key: value**2 for key, value in myNumbers.items()}
print(type(mySquares))
print('mySquares', mySquares)
