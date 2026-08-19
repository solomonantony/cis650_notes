# Coded message
"""
The ASCII table is composed of 128 characters, as for the Latin alphabet and the Caesar code, 
the ASCII shift cipher consists in shifting the characters of a rank N to obtain another character.

Encryption considers the ASCII alphabet to be cyclic (moving after the end of the alphabet 
returns to the beginning) and uses a N value called offset, ranging from 1 to 127 (negative 
numbers are possible, this amounts to an offset in the other direction).

Example: A (ASCII code 65) shifted by N = 40 becomes the code 105 (65 + 40 = 105) so i (ASCII code 105).
"""
full_name = input("Enter full name: ")
if " " in full_name:
  space_at = full_name.index(' ')
  print(f'First name {full_name[:space_at]}')
  print(f'Last name {full_name[space_at:]}')

else:
  print('Input does not have two or more words')
# what happens if you enter a name with 3 words or 4 words
# how will you extract just the first word and just the last word
