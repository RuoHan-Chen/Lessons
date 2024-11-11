# Creating a set
unique_numbers = {1, 2, 3, 4, 4}  # Duplicates are removed automatically
print(unique_numbers)  # Output: {1, 2, 3, 4}

# Adding and removing elements
unique_numbers.add(5)
print(unique_numbers)  # Output: {1, 2, 3, 4, 5}
unique_numbers.remove(3)
print(unique_numbers)  # Output: {1, 2, 4, 5}

# Set operations
set_a = {1, 2, 3}
set_b = {2, 3, 4}
print(set_a | set_b)  # Union: {1, 2, 3, 4}
print(set_a & set_b)  # Intersection: {2, 3}
print(set_a - set_b)  # Difference: {1}
