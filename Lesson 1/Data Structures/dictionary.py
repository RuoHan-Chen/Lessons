# Creating a dictionary
student = {
    "name": "Alice",
    "age": 21,
    "courses": ["Math", "Physics"]
}

# Accessing elements
print(student["name"])  # Output: Alice

# Adding a new key-value pair
student["grade"] = "A"
print(student)  # Output: {'name': 'Alice', 'age': 21, 'courses': ['Math', 'Physics'], 'grade': 'A'}

# Modifying a value
student["age"] = 22
print(student["age"])  # Output: 22

# Getting all keys and values
print(student.keys())   # Output: dict_keys(['name', 'age', 'courses', 'grade'])
print(student.values()) # Output: dict_values(['Alice', 22, ['Math', 'Physics'], 'A'])
