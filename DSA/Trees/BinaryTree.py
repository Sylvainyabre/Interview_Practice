
from . import TreeNode


class BinaryTree:
    def __init__(self):
        self.root = None

        """inserts a new node with the provided key and data to the right of the tree

        Returns:
            TreeNode: the root of the tree
        """

    def insertRight(self, key, data):
        newNode = TreeNode(key, data)
        currNode = self.root
        if currNode == None:
            self.root = newNode
            return self.root
        while currNode != None:
            # if the tree if empty
            if currNode.right == None:
                currNode.right = newNode
            else:
                currNode = currNode.right
        return self.root

    def insertLeft(key, data):
        pass

    def remove(label):
        pass

    def printInOrder():
        pass

    def printPreOrder():
        pass

    def printPostOrder():
        pass

    def invert():
        pass

    def find(key):
        pass


tr = BinaryTree()
tr.insertRight("hey", 0)
