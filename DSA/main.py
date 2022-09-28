
from customQueue import Queue
from linkedList import LinkedList
from trees import *


def main():
    q = Queue()
    lst = LinkedList
    bst = BinarySearchTree(None)
    #bst.insert(23,None)
    for i in range(10):
        bst.insert(i)
    inorder = bst.inOrder([])
    preorder = bst.preOrder([])
    postorder = bst.postOrder([])
    print("in order:",inorder)
    print("preorder order:",preorder)
    print("post order:",postorder)


if __name__ == "__main__":
    main()
