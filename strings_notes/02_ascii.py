#script to print the ASCII characters
counter = 0
for i in range(32,127):
  print(chr(i), end=' ')
  counter = counter+1
  if counter == 10:
    print()
    counter = 0
    