size = int(input("How big do you want the tree? "))

# Print the branches of the tree
for i in range(size):
    line = " " * (size - i) + "*" * (2 * i + 1)
    print(line)

# Print the trunk of the tree
for _ in range(3):
    trunk = " " * (size - 1) + "|||"
    print(trunk)
