
from linkedList import LinkedList

class Queue:
    """
    This is a linked list  implementation of a queue with a runtime of O(1) for push()
    and O(n) for pop()
    """

    def __init__(self):
        self._queue = LinkedList()
        self.top = self._queue.head

    def printQueue(self):
        if self.isEmpty():
            return
        else:
            while not self.isEmpty():
                removed = self.pop()
                print(removed, end="->")

    def peek(self):
        return self.top

    def pop(self):
        removed = self._queue.removeFront()
        self.top = self._queue.head
        return removed

    def push(self, data):
        self._queue.insertEnd(data)
        # this is technically node need here since
        # insertEnd does not change the head of the list
        self.top = self._queue.head

    def isEmpty(self):
        return self._queue.isEmpty()
