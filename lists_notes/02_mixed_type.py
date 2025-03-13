#not a good idea to have different types of data in a list, but you can
myList = [123, 'spam', 1.23, [89, 90]]
print(myList[-1][1])
letters1 = list('spam') #unpack the string into a list
print(letters1)
list_in_list = [[1,2,3], [4,5,6], [7,8,9]] #list containing lists
print(list_in_list[1][-1])
nothing_list = [] #empty list

