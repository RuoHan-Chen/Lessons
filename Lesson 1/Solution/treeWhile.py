size = int(input("How big do you want the tree? "))

# Print the branches of the tree using a while loop
i = 0
while i < size:
    line = " " * (size - i) + "*" * (2 * i + 1)
    print(line)
    i += 1

# Print the trunk of the tree using a while loop
height = 0
while height < 3:
    trunk = " " * (size - 1) + "|||"
    print(trunk)
    height += 1
