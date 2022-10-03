
from typing import Any, List
from .TreeNode import TreeNode


class BinarySearchTree():
    """Binary Search Tree
    """

    def __init__(self):
        self.root: TreeNode = None
    
    def __find(self, data,root:TreeNode):
        if root is None:
            return None
        elif root.data==data:
            return data
        elif data<root.data:
            return self.__find(data,root.left)
        elif data>root.data:
            return self.__find(data,root.right)
        else:
            return None

    def __insert(self, data, root: TreeNode) -> TreeNode:

        if root is None:
            root = TreeNode(data)
            return root
        elif root.data == data:
            return root
        elif data > root.data:
            root.right = self.__insert(data, root.right)
        else:
            root.left = self.__insert(data, root.left)
        return root

    def __remove(self, data, root: TreeNode):
        pass

    def __isBalanced(self, root: TreeNode) -> bool:
        return False

    def __isPerfect(self, root: TreeNode) -> bool:
        return False

    def __isFull(self, root: TreeNode) -> bool:
        return False

    def __isEmpty(self, root: TreeNode) -> bool:
        return root is None

    def __getHeight(self, root: TreeNode, height=-1) -> bool:
        if root is None:
            return height
        else:
            leftHeight = self.__getHeight(root.left, height+1)
            rightHeight = self.__getHeight(root.right, height+1)
            return max(leftHeight, rightHeight)

    def __preOrder(self, root: TreeNode, arr={}):
        if root is None:
            return arr
        arr.append(root.data)
        self.__preOrder(root.left)
        self.__preOrder(root.right)
        return arr

    def __inOrder(self, root: TreeNode, arr={}):
        if root is None:
            return arr
        self.__inOrder(root.left)
        arr.append(root.data)
        self.__inOrder(root.right)
        return arr

    def __postOrder(self, root: TreeNode, arr={}):
        if root is None:
            return arr
        self.__postOrder(root.left)
        self.__postOrder(root.right)
        arr.append(root.data)
        return arr

    def __levelOrder(self, root: TreeNode, arr={})->List:
        if root is None:
            return arr
        else:
            arr.append(root.data)
            self.__levelOrder(root.left)
            self.__levelOrder(root.right)
        return arr
    def __invert(self,root:TreeNode):
        pass
    def __isBinarySearchTree(self,root:TreeNode):
        return False
    def insert(self, newData) -> TreeNode:
        """Insert a non existing key into the binary search tree

        Args:
            newData:data to be inserted into to the BST
            root (BinarySearchTree): The node to insert into

        Returns:
            The root of the tree after insertion
        """
        return self.__insert(newData, self.root)
    

    def inOrder(self) -> List:
        """
        - work on the left child first
        - then the root
        - and finally the right child
        Returns: a list of the elements of the tree in from in-order traversal
        """
        return self.__inOrder(self.root)

    def preOrder(self) -> List:
        """
        - work on the root node first
        - then the left child
        - and finally the right child
        Returns: a list of the elements of the tree in from a pre-order traversal
        """
        return self.__preOrder(self.root)

    def postOrder(self) -> List:
        """
        - work on the left child first
        - then the right child
        - and finally the root node
        Returns: a list of the elements of the tree in from a post-order traversal
        """
        return self.postOrder(self.root)

    def levelOrder(self) -> List:
        """Performs a level order traversal of the tree

        Returns:
            List: The elements of the tree from a level order traversal
        """
        return self.__levelOrder(self.root)

    def remove(self, data, root) -> bool:
        return root

    def isBinarySearchTree(self) -> bool:
        return self.__isBinarySearchTree(self.root)

    def isBalanced(self) -> bool:
        return False

    def isPerfect(self) -> bool:
        return False

    def inverse(self) -> TreeNode:
        return self.__invert(self.root)

    def getHeight(self) -> int:
        """Computes the height of the tree
        - The height is define as the depth of the lowest node
        - The root node has a depth of 0
        - an empty tree a height of -1

        Returns:
            int: The height of the tree
        """
        return self.__getHeight(self.root)

    def find(self) -> Any:
        return self.__find(self.root)
