def print_branches(level, size):
    # Base case: stop recursion when level equals size
    if level >= size:
        return
    # Print the current level of branches
    print(" " * (size - level) + "*" * (2 * level + 1))
    # Recursive call for the next level
    print_branches(level + 1, size)

def print_trunk(trunk_height, size, current_height=0):
    # Base case: stop recursion when current height reaches trunk height
    if current_height >= trunk_height:
        return
    # Print the current level of the trunk
    print(" " * (size - 1) + "|||")
    # Recursive call for the next line of the trunk
    print_trunk(trunk_height, size, current_height + 1)

# Get user input for the size of the tree
size = int(input("How big do you want the tree? "))

# Print the branches and trunk of the tree
print_branches(0, size)
print_trunk(3, size)
