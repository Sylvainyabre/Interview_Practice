from Node import Node
import sys


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    """
    @params:
        - newVal: the value to insert
        - locationval: the value of the node after which we are inserting

    """

    def insertAfter(self, newKey, oldKey):
        if self.head == None:
            return
        else:
            curr = self.head
            while curr is not None:
                if curr.data == oldKey:
                    nextNode = curr.next
                    curr.next = Node(newKey, nextNode)
                    # if the previous node was the tail, set tail to the new node
                    if self.tail.data == curr.data:
                        self.tail = nextNode
                    break
                else:
                    curr = curr.next

    def insertEnd(self, newKey):
        if self.tail is not None:
            newNode = Node(newKey, None)
            self.tail.next = newNode
            self.tail = newNode
        else:
            newNode = Node(newKey, None)
            self.tail = newNode
            self.head = self.tail

    def insertFront(self, newKey):
        if self.head is None:
            self.head = Node(newKey, None)
            self.tail = self.head
        else:
            newNode = Node(newKey, self.head)
            self.head = newNode

    def remove(self, val):
        # special cases
        if self.head.data == val:
            removed = self.head.data
            self.head = self.head.next
            return removed
        # the node to remove is the tail of the list
        if self.tail.data == val:
            curr = self.head
            while curr is not None and curr.next is not None:
                if curr.next.data == self.tail.data:
                    removed = curr.next.data
                    curr.next = None
                    self.tail = curr
                    return removed
                else:
                    curr = curr.next

        # The node to delete is neither head nor tail
        else:
            curr = self.head
            while curr is not None and curr.next is not None:
                if curr.next.data == val:
                    removed = curr.next.data
                    curr.next = curr.next.next

                    return removed
                else:
                    curr = curr.next
        return None

    def removeFront(self):
        curr = self.head
        # special cases
        if curr==None:
            return None
        else:
            removed = curr.data
            curr = curr.next 
            self.head = curr 
            return removed
        


    def isEmpty(self):
        return self.head == None 

    def reverse(self):
        # iterative approach
        oldTail = self.tail
        oldHead = self.head
        prev = None
        curr = self.head
        nextNode = None
        while curr is not None:
            nextNode = curr.next
            curr.next = prev
            prev = curr
            curr = nextNode

        self.head = prev
        self.tail = oldHead

    def printList(self):
        curr = self.head
        while curr is not None:
            suffix = "-->" if curr.next is not None else ""
            print(curr.data, end=suffix)
            curr = curr.next

    def printReverse(self):
        self._reversePrint(self.head)

    def _reversePrint(self, curr):
        if curr is None:
            return
        if curr.next is not None:
            self._reversePrint(curr.next)
        suffix = "" if curr.data == self.head.data else "-->"
        print(curr.data, end=suffix)
