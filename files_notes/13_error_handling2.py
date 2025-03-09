import os
def printdir(dir):
    try:
        filenames = os.listdir(dir)
        for filename in filenames:
            print('file name: ',filename)  ## foo.txt
            #print('os path:', os.path.join(dir, filename)) ## dir/foo.txt (relative to current dir)
            #print(os.path.abspath(os.path.join(dir, filename))) ## /home/nick/dir/foo.txt
    except Exception as e:
        print(e)  #prints the message of that error 
    else:
        print('File path was good')

printdir('C:/Users/santony/Document/')

