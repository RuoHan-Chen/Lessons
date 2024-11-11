size = int(input("How big do you want the tree?"))

for i in range(size):
    line = ""
    for space in range(size - i-1):
        line += " "
    for leaf in range(2*i+1):
        line += "*"
    print(line)

treeHeight = 3
for height in range(treeHeight):
    line = ""
    for space in range(size-1-treeHeight//2):
        line += " "
    line += "|||"
    print(line)
