from node import Node
from printExt import *


class AVL:
    def __init__(self):
        self.root = None

    def balanceTree(self, node):
        if node is None:
            return self
        balance = self.getBalance(node)
        if balance > 1:
            self.leftRotate(node)
        if balance < -1:
            self.rightRotate(node)
        else:
            if node.parent is not None:
                self.balanceTree(node.parent)
            else:
                return self

    def leftRotate(self, node):
        if self.getBalance(node.right) >= 0:
            tempNode = None
            newLeft = node
            newTop = node.right
            if newTop.left is not None:
                tempNode = newTop.left
            newTop.left = newLeft
            newTop.parent = newLeft.parent
            newLeft.parent = newTop
            newLeft.right = tempNode
            if tempNode is not None:
                tempNode.parent = newLeft
            if node == self.root:
                self.root = newTop
            elif newTop.value < newTop.parent.value:
                newTop.parent.left = newTop
            else:
                newTop.parent.right = newTop
            return self
        if self.getBalance(node.right) < 0:
            self.rightDubRotate(node.right)
            self.leftDubRotate(node)

    def rightRotate(self, node):
        if self.getBalance(node.left) <= 0:
            tempNode = None
            newRight = node
            newTop = node.left
            if newTop.right is not None:
                tempNode = newTop.right
            newTop.right = newRight
            newTop.parent = newRight.parent
            newRight.parent = newTop
            newRight.left = tempNode
            if tempNode is not None:
                tempNode.parent = newRight
            if node == self.root:
                self.root = newTop
            elif newTop.value < newTop.parent.value:
                newTop.parent.left = newTop
            else:
                newTop.parent.right = newTop
            return self
        #If we have different signs
        if self.getBalance(node.left) > 0:
            self.leftDubRotate(node.left)
            self.rightDubRotate(node)


    def leftDubRotate(self, node):
        tempNode = None
        newLeft = node
        newTop = node.right
        if newTop.left is not None:
            tempNode = newTop.left
        newTop.left = newLeft
        newTop.parent = newLeft.parent
        newLeft.parent = newTop
        newLeft.right = tempNode
        if tempNode is not None:
            tempNode.parent = newLeft
        if node == self.root:
            self.root = newTop
        elif newTop.value < newTop.parent.value:
            newTop.parent.left = newTop
        else:
            newTop.parent.right = newTop
        return self


    def rightDubRotate(self, node):
        tempNode = None
        newRight = node
        newTop = node.left
        if newTop.right is not None:
            tempNode = newTop.right
        newTop.right = newRight
        newTop.parent = newRight.parent
        newRight.parent = newTop
        newRight.left = tempNode
        if tempNode is not None:
            tempNode.parent = newRight
        if node == self.root:
            self.root = newTop
        elif newTop.value < newTop.parent.value:
            newTop.parent.left = newTop
        else:
            newTop.parent.right = newTop
        return self


    # ------------------------ADD FUNCTION------------------------------------
    def add(self, value):
        newNode = Node(value)
        if self.root is None:
            self.root = newNode
            return self
        else:
            self._add(value, self.root)
            self.balanceTree(self.find(value))
        return self

    def _add(self, value, currNode):
        if value < currNode.value:
            if currNode.left is None:
                currNode.left = Node(value)
                currNode.left.parent = currNode  # sets parent
            else:
                self._add(value, currNode.left)
        if value > currNode.value:
            if currNode.right is None:
                currNode.right = Node(value)
                currNode.right.parent = currNode  # sets parent
            else:
                self._add(value, currNode.right)

    # ------------------------REMOVE FUNCTION----------------------------------

    def find(self, value):
        if self.root is None:
            return
        elif self.root.value == value:
            return self.root
        else:
            return self._find(value, self.root)

    def _find(self, value, currNode):
        if value < currNode.value:
            if currNode.left is None:
                return
            elif currNode.left.value == value:
                return currNode.left
            else:
                return self._find(value, currNode.left)
        if value > currNode.value:
            if currNode.right is None:
                return
            elif currNode.right.value == value:
                return currNode.right
            else:
                return self._find(value, currNode.right)

    def remove(self, value):
        if self.root is None:
            return self
        deleteNode = self.find(value)
        balanceNode = deleteNode.parent
        if deleteNode.value == self.root.value:
            if deleteNode.left is not None and deleteNode.right is not None:
                if deleteNode.left.right is None:
                    deleteNode.left.right = deleteNode.right
                    deleteNode.right.parent = deleteNode.left
                    self.root = deleteNode.left
                    deleteNode.left.parent = None
                else:
                    currNode = deleteNode.left.right
                    while currNode.right is not None:
                        currNode = currNode.right
                    currNode.right = deleteNode.right
                    deleteNode.right.parent = currNode
                    self.root = deleteNode.left
                    deleteNode.left.parent = None
            elif deleteNode.left is not None:
                self.root = deleteNode.left
                deleteNode.left.parent = None
            elif deleteNode.right is not None:
                self.root = deleteNode.right
                deleteNode.right.parent = None
            else:
                self.root = None
            balanceNode = self.root
        elif deleteNode.left is not None and deleteNode.right is not None:
            if deleteNode.value < deleteNode.parent.value:
                deleteNode.parent.left = deleteNode.left
                deleteNode.left.parent = deleteNode.parent
                if deleteNode.left.right is None:
                    deleteNode.left.right = deleteNode.right
                    deleteNode.right.parent = deleteNode.left
                else:
                    currNode = deleteNode.left.right
                    while currNode.right is not None:
                        currNode = currNode.right
                    currNode.right = deleteNode.right
                    deleteNode.right.parent = currNode
            # This else works with deleting a node that has two children located on the right side of the subtree
            else:
                deleteNode.parent.right = deleteNode.left
                deleteNode.left.parent = deleteNode.parent
                if deleteNode.left.right is None:
                    deleteNode.left.right = deleteNode.right
                    deleteNode.right.parent = deleteNode.left
                else:
                    currNode = deleteNode.left.right
                    while currNode.right is not None:
                        currNode = currNode.right
                    currNode.right = deleteNode.right
                    deleteNode.right.parent = currNode
        # this elif deals with nodes that only have a left child
        elif deleteNode.left is not None:
            if deleteNode.left.value > deleteNode.parent.value:
                deleteNode.parent.right = deleteNode.left
                deleteNode.left.parent = deleteNode.parent
            else:
                deleteNode.parent.left = deleteNode.left
                deleteNode.left.parent = deleteNode.parent
        # this elif deals with nodes that only have a right child
        elif deleteNode.right is not None:
            if deleteNode.right.value > deleteNode.parent.value:
                deleteNode.parent.right = deleteNode.right
                deleteNode.right.parent = deleteNode.parent
            else:
                deleteNode.parent.left = deleteNode.right
                deleteNode.right.parent = deleteNode.parent
        # This else deals with leaf nodes
        else:
            if deleteNode.parent.right is not None and deleteNode.parent.right.value == value:
                deleteNode.parent.right = None
            else:
                deleteNode.parent.left = None
        self.balanceTree(balanceNode)
        return self

    # -----------------------CONTAINS FUNCTION----------------------------------
    def contains(self, value):
        if self.root is None:
            return False
        elif self.root.value == value:
            return True
        else:
            return self._contains(value, self.root)

    def _contains(self, value, currNode):
        if value < currNode.value:
            if currNode.left is None:
                return False
            elif currNode.left.value == value:
                return True
            else:
                return self._contains(value, currNode.left)
        if value > currNode.value:
            if currNode.right is None:
                return False
            elif currNode.right.value == value:
                return True
            else:
                return self._contains(value, currNode.right)
        return False

    # --------------------------SIZE FUNCTION-------------------------------
    def size(self):
        if self.root is None:
            return 0
        elif self.root.right is not None and self.root.left is not None:
            return self._size(self.root.left) + self._size(self.root.right) + 1
        elif self.root.left is not None:
            return self._size(self.root.left) + 1
        elif self.root.right is not None:
            return self._size(self.root.right) + 1
        else:
            return 1

    def _size(self, currNode):
        if currNode.left is not None and currNode.right is not None:
            return self._size(currNode.left) + self._size(currNode.right) + 1
        elif currNode.left is not None:
            return self._size(currNode.left) + 1
        elif currNode.right is not None:
            return self._size(currNode.right) + 1
        else:
            return 1

    # ------------------------ASLIST FUNCTION--------------------------------
    def asList(self):
        returnArray = []
        if self.root is None:
            return returnArray
        else:
            returnArray.append(self.root.value)
            returnList = self._asList(self.root, [])
            returnArray.extend(returnList)
        return returnArray

    def _asList(self, currNode, array):
        myArray = array
        if currNode.left is not None:
            myArray.append(currNode.left.value)
            self._asList(currNode.left, myArray)
        if currNode.right is not None:
            myArray.append(currNode.right.value)
            self._asList(currNode.right, myArray)
        return myArray

    # -------------------------HEIGHT FUNCTION-------------------------------
    def height(self):
        if self.root is None:
            return 0
        elif self.root.right is not None and self.root.left is not None:
            leftHeight = self._height(self.root.left)
            rightHeight = self._height(self.root.right)
            if leftHeight >= rightHeight:
                return leftHeight + 1
            else:
                return rightHeight + 1
        elif self.root.right is not None:
            return self._height(self.root.right) + 1
        elif self.root.left is not None:
            return self._height(self.root.left) + 1
        else:
            return 1

    def _height(self, currNode):
        if currNode.right is not None and currNode.left is not None:
            leftHeight = self._height(currNode.left)
            rightHeight = self._height(currNode.right)
            if leftHeight >= rightHeight:
                return leftHeight + 1
            else:
                return rightHeight + 1
        elif currNode.right is not None:
            return self._height(currNode.right) + 1
        elif currNode.left is not None:
            return self._height(currNode.left) + 1
        else:
            return 1

    def getBalance(self, node):
        if node is None:
            return
        if node.left is not None and node.right is not None:
            return self._height(node.right) - self._height(node.left)
        if node.left is not None:
            return 0 - self._height(node.left)
        if node.right is not None:
            return self._height(node.right)
        else:
            return 0

avl = AVL()
avl.add(15).add(7).add(3).add(1).add(0).add(2).add(5).add(4).add(6).add(11).add(9).add(8).add(10).add(13).add(12).add(14).add(23).add(19).add(17).add(16).add(18).add(21).add(20).add(22).add(27).add(25).add(24).add(26).add(29).add(28).add(30)
printExt(avl)
print(avl.asList())
