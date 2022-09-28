
from typing import Any, List

# TODO: turn this into methods instead of a class


class BinarySearchTree():
    def __init__(self, newData):
        self.data = newData
        self.right: BinarySearchTree = None
        self.left: BinarySearchTree = None

    def insert(self, newData):
        """Insert a non existing key into the binary search tree

        Args:
            newData:data to be inserted into to the BST
            root (BinarySearchTree): The node to insert into

        Returns:
            void
        """
        if self.data == None:
            self.data = newData
            return

        if self.data == newData:
            return

        elif newData < self.data:
            if self.left is None:
                self.left = BinarySearchTree(newData)
                return
            else:
                self.left.insert(newData)

        else:
            if self.right is None:
                self.right = BinarySearchTree(newData)
                return
            else:
                self.right.insert(newData)

    def inOrder(self, arr: List):
        """
        - work on the left child first
        - then the root
        - and finally the right child
        Returns: a list of the elements of the tree in from in-order traversal
        """
        if self.data == None:
            return arr
        if self.left:
            self.left.inOrder(arr)
        arr.append(self.data)
        if self.right:
            self.right.inOrder(arr)
        return arr

    def preOrder(self, arr: List):
        """
        - work on the root node first
        - then the left child
        - and finally the right child
        Returns: a list of the elements of the tree in from a pre-order traversal
        """
        if self.data == None:
            return arr
        arr.append(self.data)
        if self.left:
            self.left.preOrder(arr)
        if self.right:
            self.right.preOrder(arr)
        return arr

    def postOrder(self,  arr: List):
        """
        - work on the left child first
        - then the right child
        - and finally the root node
        Returns: a list of the elements of the tree in from a post-order traversal
        """
        if self.data == None:
            return arr
        if self.left:
            self.left.postOrder(arr)
        if self.right:
            self.right.postOrder(arr)

        arr.append(self.data)
        return arr

    def levelOrder(self, root):
        pass

    def remove(self, data, root):
        return root

    def isBinarySearchTree(self, root):
        return root

    def invert(self, root):
        return root

    def find(self, key, root):
        return root
