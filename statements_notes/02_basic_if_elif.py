number1 = int(input('Enter first number: '))
number2 = int(input('Enter second number: '))
if number1 == number2:
    result = 'Equal'
elif number1 < number2:
    result = 'First is less than second'
else:
    result = 'First is greater than second'
print(result)
