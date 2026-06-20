largest = -99
while True:
    next_input = int(input('Enter a number or -1 to stop: '))
    if next_input == -1:
        break
    else:
        if next_input > largest:
            largest = next_input
print('The largest number is', largest)

