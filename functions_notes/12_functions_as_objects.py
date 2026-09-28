#Like everything else in Python, functions are just objects;

def remember(x):  #define a function
  return f'Hi {x}'

print(remember('joe'))

i = remember  # assign it to an object; creates a second name to the function 
i.me = 'solomon' # attach an attribute for later use; available to the original function also
print(i.me)  #recall the value
# add an age attribute to the object and see if you can recall it
<<<<<<< HEAD
print('from the function', remember.me)

def say_okay():
  say_okay.counter += 1
  print('Okay')
say_okay.counter = 0

for _ in range (5):
  say_okay()
print(f'say_okay was called {say_okay.counter} times')
=======
i.age = 60
print(i.age)
>>>>>>> 24d8fa8fa66842fc9ad529948967df8d486fdec8
