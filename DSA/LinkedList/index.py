from LinkedList import LinkedList
from Queue import Queue
from Stack import Stack


def main():
    list1 = LinkedList()
    # list1.insertEnd("Hello")
    # list1.insertEnd("Dear")
    # list1.insertEnd("Beautiful")
    # list1.insertEnd("World")
    # list1.insertFront("Sylvain")
    # list1.insertFront("Yabre")
    list1.insertAfter("Says","Sylvain")
    # list1.remove("Dear")
    # list1.remove("Hello")
    # list1.remove("World")
    # list1.printList()
    # list1.printReverse()
    # queue = Queue()
    # queue.push(1)
    # queue.push(2)
    # queue.push(3)
    # queue.push(4)
    # queue.pop()
    # queue.pop()
    # queue.pop()
    # queue.push(10)
    # queue.printQueue()
    stack  = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    # stack.pop()
    # stack.pop()
    # stack.pop()
    stack.printStack()
    


if __name__ == "__main__":
    main()
