import os
print(os.getcwd())
new_directory = input('Enter a name for the new directory')
os.mkdir(new_directory)
print('New directory created')
print(os.listdir())
if input('Can we go ahead and delete the folder? y/n') in 'Yy':
    os.rmdir(new_directory)
    print('Thanks.  it is gone')
    print(os.listdir())

