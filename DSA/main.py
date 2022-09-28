
from customQueue import Queue
from linkedList import LinkedList
from trees import *
import binarySearch as bs



def main():
    # q = Queue()
    # lst = LinkedList
    # bst = BinarySearchTree(None)
    # #bst.insert(23,None)
    # for i in range(10):
    #     bst.insert(i)
    # inorder = bst.inOrder([])
    # preorder = bst.preOrder([])
    # postorder = bst.postOrder([])
    # print("in order:",inorder)
    # print("preorder order:",preorder)
    # print("post order:",postorder)
    arr = [33,432,56,75,89,65,24,23,55,32,57,68]
    print("looking for the index of 0",bs.binarySearch(0,arr))
    print("looking for the index of 55",bs.binarySearch(55,arr))
    print("looking for the index of 68",bs.binarySearch(68,arr))
    print("looking for the index of 33",bs.binarySearch(33,arr))
    print("looking for the index of 75",bs.binarySearch(75,arr))


if __name__ == "__main__":
    main()
