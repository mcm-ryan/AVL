class Node:
    def __init__(self, value):
        self.value = value  # The value at this node
        self.left = None  # A link (if any) to a node with a lesser value
        self.right = None  # A link (if any) to a node with a greater value
        self.parent = None  # A link to the parent node


