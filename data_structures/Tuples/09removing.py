numbers = (1, 2, 3, 4, 5)

# Convert to list, remove, convert back
numbers_list = list(numbers)
numbers_list.remove(3)
numbers = tuple(numbers_list)

print("After removing 3:", numbers)
