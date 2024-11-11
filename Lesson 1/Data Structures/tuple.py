# Creating a tuple
dimensions = (1920, 1080)

# Accessing elements
print(dimensions[0])  # Output: 1920

# Tuple unpacking
width, height = dimensions
print("Width:", width)  # Output: Width: 1920
print("Height:", height)  # Output: Height: 1080

# Note: Tuples are immutable, so we cannot change elements.
# dimensions[0] = 1280  # This would raise an error
