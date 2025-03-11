#f string is not a cuss word
number1 = 10.25
print(f'number1 {number1}') # no format
print(f'number1 {number1:6.2f}') # 2 decimals
print(f'number1 {number1:<6.2f}') # 2 decimals, aligned left
print(f'number1 {number1:>6.2f}') # 2 decimals, aligned right
print(f'number1 {number1:^6.2f}') # 2 decimals, aligned center
print(f'number1 {number1:=^6.2f}') # 2 decimals, aligned center, with leading = for filler
