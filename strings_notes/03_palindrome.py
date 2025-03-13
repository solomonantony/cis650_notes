### Check if a string is a palindrome
# 

while True:
  test_string = input("Enter string value: ")
  if test_string == test_string[::-1]:
    print(f'{test_string} is a palindrome')
  else:
    print(f'{test_string} is not a palindrome')
  if input("Try again? Y/N") != "Y": break
print('Thanks for playing')

