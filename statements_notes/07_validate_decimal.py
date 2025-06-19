while True:
    print('Enter your age:')
    age = input()
    if age.isdecimal():
        break
    else:
        print('Please enter a number for your age.')
print(f'The age is {age}')
