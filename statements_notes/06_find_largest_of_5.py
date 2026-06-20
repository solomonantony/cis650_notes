largest = -99
for _ in range(5):
    next_input = int(input('Enter a positive number: '))
    if next_input > largest:
        largest = next_input
print('The largest number is ', largest)
        