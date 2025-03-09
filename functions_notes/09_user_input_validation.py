# Here is a function that checks for valid integer input
def input_int(prompt):
  while True:  #infinite loop
    variable = input(prompt)
    try:
      variable = int(variable)  #attempt to convert variable to int
      return variable  #if successful, return int
    except:  #if not successful,
      print('Invalid integer!')  #print error message

my_age = input_int("Enter your age: ")
print(my_age)

#modify the above code to test for float type
