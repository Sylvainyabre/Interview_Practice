
from ..LinkedList import LinkedList

"""
    This is a linked list  implementation of a stack with a runtime of O(1) for both push() and pop()
"""
class Stack:
    def __init__(self):
        self._stack = LinkedList()
        self.top = self._stack.head
    
    def printStack(self):
        if self.isEmpty():
            return 
        while not self.isEmpty():
            removed = self.pop()
            print(removed,end="->")

    def peek(self):
        return self.top

    def pop(self):
        removed = self._stack.removeFront()
        self.top = self._stack.head
        return removed
        
    def push(self,data):
        self._stack.insertFront(data)
        self.top = self._stack.head
    
    def isEmpty(self):
        return self._stack.isEmpty()

    