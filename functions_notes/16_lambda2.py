#the first is a straigh up function
def before_lambda(n=2):
  x = 4
  return x ** n
print(before_lambda(3))

#this function returns a lambda
def func():
    x = 4
    action = (lambda n=2: x ** n)
    return action
y = func()
print(y(3))
# How is the parameter value used
