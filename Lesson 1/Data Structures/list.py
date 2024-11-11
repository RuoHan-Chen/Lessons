# Creating a list
fruits = ["apple", "banana", "cherry"]

# Accessing elements
print(fruits[1])  # Output: banana

# Modifying a list
fruits.append("date")
print(fruits)  # Output: ['apple', 'banana', 'cherry', 'date']

# Removing an element
fruits.remove("banana")
print(fruits)  # Output: ['apple', 'cherry', 'date']

# Adding "orange" at index 1 (middle of the list in this case)
fruits.insert(1, "orange")
print(fruits)  # Output: ['apple', 'orange', 'cherry', 'date']

# Slicing a list
print(fruits[:2])  # Output: ['apple', 'cherry']
