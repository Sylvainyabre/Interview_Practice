
from typing import Any, List


class BinarySearchTree():
    def __init__(self, newData) -> None:
        self.data: Any = newData
        self.right: BinarySearchTree = None
        self.left: BinarySearchTree = None

    def insert(self, newData: Any, root):
        """Insert a non existing key into the binary search tree

        Args:
            newData (Any):data to be inserted into to the BST
            root (BinarySearchTree): The node to insert into

        Returns:
            root: The root of the tree
        """
        if root == None:
            return BinarySearchTree(newData)
        elif newData < root.data:
            root.left = self.insert(newData, root.left)
        elif newData > root.data:
            root.right = self.insert(newData, root.right)

        else:
            return root

    def inOrder(self, root, arr: List):
        """
        - work on the left child first
        - then the root
        - and finally the right child
        Returns: a list of the elements of the tree in from in-order traversal
        """
        if root == None:
            return arr
        else:

            self.inOrder(self.left, root, arr)
            arr.append(root.data)
            self.inOrder(self.right, root, arr)

    def preOrder(self, root, arr: List):
        """
        - work on the root node first
        - then the left child
        - and finally the right child
        Returns: a list of the elements of the tree in from a pre-order traversal
        """
        if root == None:
            return arr
        else:
            arr.append(root.data)
            self.preOrder(self.left, root, arr)
            self.preOrder(self.right, root, arr)

    def printPostOrder(self, root, arr: List):
        """
        - work on the left child first
        - then the right child
        - and finally the root node
        Returns: a list of the elements of the tree in from a post-order traversal
        """
        if root == None:
            return arr
        else:
            self.postOrder(self.left, root, arr)
            self.postOrder(self.right, root, arr)
            arr.append(root.data)
           

    def remove(self, data, root):
        return root

    def isBinarySearchTree(self, root):
        return root

    def invert(self, root):
        return root

    def find(self, key, root):
        return root
