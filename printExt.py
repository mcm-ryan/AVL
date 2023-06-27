from node import Node

"""
It should be noted that THIS file was WRITTEN BY MY PROFESSOR for testing purposes to help with this project
"""

def stringReplace(string, index, character):
    return string[:index] + character + string[index+1:]

def printCurrentLevel(self, node, level):
        if level == 1:
            if node is None:
                return ["x"]
            if node.value is None:
                return ["+"]
            return [str(node.value) + " (" + str(self._height(node)) + "/" + str(self.getBalance(node)) + ")"]
        elif level > 1:
            toReturn = []
            if node is None:
                node = Node(None)
            left = node.left
            right = node.right
            l = printCurrentLevel(self, left, level-1)
            r = printCurrentLevel(self, right, level-1)
            toReturn.extend(l)
            toReturn.extend(r)
            return toReturn

def printExt(self, width=30):
    if self.root == None:
        print("< Empty BST >")
        return
    h = self.height()

    valuesByHeight = []
    lines = []  # Each line as a string
    starts = [[] for i in range(h)]  # Starting coordinate for each item
    bs = width  # How far between centers

    for i in range(1, h+1):  # For every row in the tree
        values = printCurrentLevel(self, self.root, i)
        valuesByHeight.append(values)

    g = 2**(h-1) # Number of items on the bottom row

    for i in range(h):
        lines.append("".ljust(bs*(g+1) + g, " "))


    for j in range(g):
        starts[h-1].append(bs*(j+1)+j)

    for i in reversed(range(h-1)):
        nextIndex = i+1
        nextRow = starts[nextIndex]
        for j in range(0, len(nextRow), 2):
            starts[i].append((nextRow[j] + nextRow[j+1])/2)

    for i in range(h-1):
        nextIndex = i + 1
        nextRow = starts[nextIndex]
        for j in range(0, len(nextRow), 2):
            start = int(nextRow[j])
            stop = int(nextRow[j+1])+1
            for k in range(start, stop):
                lines[i] = stringReplace(lines[i], k, "-")
            lines[i] = stringReplace(lines[i], start, "+")
            lines[i] = stringReplace(lines[i], stop-1, "+")

    for i in range(0, len(lines)):
        values = valuesByHeight[i]
        for j in range(len(values)):
            toAdd = str(values[j])
            start = int(starts[i][j])
            for k in range(0, len(toAdd)):
                lines[i] = stringReplace(lines[i], start+k, toAdd[k])

    for line in lines:
        print(line)
    return self