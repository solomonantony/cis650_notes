# This script demonstrates basic error handling in Python.
# while True:
#     value = int(input("Enter a number (-1 to quit): "))
#     if value == -1: break

while True:
    try:
        value = int(input('Enter an integer: ')) 
    except ValueError:
        print('Invalid entry.  Please try again')
    else:
        print('Thanks!')
        break
    
