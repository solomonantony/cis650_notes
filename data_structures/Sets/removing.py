fruits = {"apple", "banana", "cherry"}

fruits.remove("banana")  # Removes banana (error if not found)
print("After remove:", fruits)

fruits.discard("orange")  # Removes safely (no error if missing)
print("After discard:", fruits)

removed_item = fruits.pop()  # Removes a random element
print("Popped:", removed_item)
print("Remaining:", fruits)
