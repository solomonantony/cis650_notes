filename = input('Enter a text file name: ')
with open(filename, 'w') as your_file:
    line1 = "This here's the wattle,\n"
    your_file.write(line1)
print("reading the file \n=============")   
with open(filename) as your_file:
    print(your_file.readlines())