from Node import Node


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
            self.head = self.head.next
        # the node to remove is the tail of the list
        if self.tail.data == val:
            curr = self.head
            while curr is not None:
                if curr.next.data == self.tail.data:
                    self.tail = curr
                    break
                else:
                    curr = curr.next

        # The node to delete is neither head nor tail
        else:
            curr = self.head
            while curr is not None and curr.next is not None:
                if curr.next.data == val:
                    curr.next = curr.next.next

                    break
                else:
                    curr = curr.next

    def reverse(self):
        # iterative approach
        oldTail = self.tail
        oldHead = self.head
        prev = None
        curr = self.head
        while curr is not None:
            curr.next = prev
            prev = curr
            curr = curr.next

        self.head = oldTail
        self.tail = oldHead

    def printList(self):
        curr = self.head
        while curr is not None:
            print(curr.data)
            curr = curr.next

    def printReverse(self):
        self.reversePrint(self,self.head)

    def reversePrint(self,curr):
        if curr is not None:
            return self.reversePrint(self,curr.next)
        print(curr)


