# This script demonstrates basic error handling in Python.
while True:
    try:
        value = int(input('Enter an integer: ')) 
    except ValueError:
        print('Invalid entry.  Please try again')
    else:
        print('Thanks!')
        break
    
