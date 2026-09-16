# Convert set to list
numbers = {1, 2, 3}
numbers_list = list(numbers)
print("As list:", numbers_list)

# Convert set to tuple
numbers_tuple = tuple(numbers)
print("As tuple:", numbers_tuple)

# Convert list to set (removes duplicates)
duplicates_list = [1, 2, 2, 3, 3, 3]
unique_set = set(duplicates_list)
print("Unique set:", unique_set)

