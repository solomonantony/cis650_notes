# Create a list that contains multiple sets
list_of_sets = [
    {"apple", "banana", "cherry"},     # Set of fruits
    {"dog", "cat"},                   # Set of animals
    {1, 2, 3, 4},                     # Set of numbers
]

print("List of sets:")
for i, s in enumerate(list_of_sets, start=1):
    print(f"Set {i}: {s}")

# Accessing a specific set in the list
print("\nSecond set (animals):", list_of_sets[1])

# Adding an element to the first set (fruits)
list_of_sets[0].add("mango")
print("\nAfter adding 'mango' to the first set:", list_of_sets[0])

# Performing operations across sets
union_of_all = set().union(*list_of_sets)  # Union of all sets in the list
print("\nUnion of all sets:", union_of_all)
