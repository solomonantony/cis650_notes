#Like everything else in Python, functions are just objects;

def remember(x):  #define a function
  return f'Hi {x}'

print(remember('joe'))

i = remember  # assign it to an object
i.me = 'solomon' # attach an attribute for later use
print(i.me)  #recall the value
# add an age attribute to the object and see if you can recall it
