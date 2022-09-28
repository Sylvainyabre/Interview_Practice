
from typing import Any


class BinarySearchTree():
    def __init__(self) -> None:
        self.data:Any = None
        self.right:BinarySearchTree = None
        self.left:BinarySearchTree = None



    def insert(self, newData:Any,root):
        if root==None:
            return BinarySearchTree(newData)
         
        else:
            right = node.right
            left:TreeNode = node.left
            if newData<right.data:
              node.left =   self.insert(newData,left)
            else:
                node.right = self.insert(newData,right)


