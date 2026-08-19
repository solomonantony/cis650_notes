## Collections

Collections are prepackaged data structures consisting of related data items.Examples of collections:

- Favorite songs on your smartphone
- Contacts list
- A library’s books
- Cards in a card game
- Favorite sports team’s players
- Stocks in an investment portfolio
- Patients in a cancer study
- Shopping list.

## Explore creation and accessing of a list at the terminal

Lists typically store homogeneous data. 
```
c = [-45, 6, 0, 72, 1543]
#run this to initialize c
c
c[0]
c[-1]
```
but may store heterogeneous data.

```
myList = [123, 'spam', 1.23, [89, 90]]
print(myList[-1][1])
letters1 = list('spam') #unpack the string into a list
print(letters1)
list_in_list = [[1,2,3], [4,5,6], [7,8,9]] #list containing lists
print(list_in_list[1][-1])
nothing_list = [] #empty list
```
Reference a list element by writing the list’s name followed by the element’s index enclosed in [] (the subscription operator).

```
c = [-45, 6, 0, 72, 1543]
c[0]
c[4]
c[-1] # same as last item
print(c[-5])
number1, number2, number3 = [2, 3, 5] #unpacks to list items
# run this line to initialize c
print(number1, number2)
```
## List properties
- Use len(listName) to find size of a list
- Index values must be in range.
- Indices Must Be Integers or Integer Expressions

```
i=1
print(c[i])
# Lists Are Mutable
c[1] = 100 #assigns 100 to second element in list c
# print to see if the value is updated
print(c)
```

## List operations: Adding to a list

```
c = [-45, 6, 0, 72, 1543]
c += [10]
print(c)
letters1 = list('spam') #unpack the string into a list
print(letters1)
print(letters1+['a','b']) # appends two items to letters1

letters1 + list("Python") #unpacks 'Python' and appends to letters1
print(letters1*3) # appends a copy of letters1 to letters1
letters1.append('a1') #appends 'a1' to letters
letters1.insert(0,123) #insert 123 at 0
print(c + c)
c.extend(['xx', 'yy']) #extends the list by two items
#print the result of each line above to verify the result
```
## List operations: Removing from a list

```
c = [-45, 6, 0, 72, 1543]
c.pop(1)  #removes the item at index 1; list is shorter now
letters1.remove('y') #finds and removes first occurrence of 'y'
del c[0]  #deletes the item at 0 position
c = [-45, 6, 0, 72, 1543]
del c[0:2] #Removes items 0 and 1
c = [-45, 6, 0, 72, 1543]
c.remove(72) #removes the item and resizes the list
c.clear() #empties the list
#print the value c after each operation to make sure you understand it
```
## List operations: Comparing lists

```
a = [1, 2, 3]
b = [1, 2, 3]
a == b  #compare for equality
c=[1,2, 4]
a<c #compare for inequality
# Does it compare item to item?
```
## List operations: Sorting a list
```
c = [45, 26, 10, 72, 43]
c.sort() #modified the list
c.sort(reverse=True) #sorts in descending order
c = [45, 26, 10, 72, 43]
sorted(c) #creates a sorted c; original c is unaffected
#check to see if original c is unaffected
```
## List operations: Searching Sequences
numbers = [3, 7, 1, 4, 2, 8, 5, 6, 3, 5, 6, 7]
print(numbers.index(5)) # index of first element that matches 5
print(numbers.index(5, 4)) #find index of 5 starting from position 4
numbers.index(7, 0, 4) #find position of 7 between 0 and 4
8 in numbers #using the in operator, returns boolean
8 not in numbers
numbers.count(3) # returns number of 3s in the list
#print each result to ensure it works as commented

## Asking questions of a list

```
len(numbers) # how many items are in the list
min(numbers) # what is the smallest value in the list
max(numbers) # what is the largest value in the list
23 in numbers # is 23 in the list? returns True or False
#print each result to ensure it works as commented
```
## Slicing
- To generate a list with some of the items from a source list, use slicing
- Slicing involves using square brackets and one of more colons within
```
numbers = [2, 3, 5, 7, 11, 13, 17, 19]
print(numbers[2:6]) # get entries from item index 2 to item index 6, excluding 6
numbers[:6] # Starting from 0, go up to item 6
numbers[6:] # starting from 6, all items after that
print(numbers[::2]) #Get every second item
print(numbers[::-1]) #starting from 0 go -1 index at a time
numbers[0:3] = ['two', 'three', 'five'] #replace the first
#print each result to ensure it works as commented
```

## 

