"""You are given two non-empty linked lists representing two non-negative integers.
 The digits are stored in reverse order, and each of their nodes contains a single digit.
  Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.



Example 1:


Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]
Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]


Constraints:

The number of nodes in each linked list is in the range [1, 100].
0 <= Node.val <= 9
It is guaranteed that the list represents a number that does not have leading zeros.
    """

# we approach this problem having a full implementation of a linkedlist class

from LinkedList.LinkedList import LinkedList


def addTwoNumbers(list1, list2):
    carry = 0
    result = LinkedList
    curr1 = list1
    curr2 = list2
    while list1 is not None or list2 is not None:
        if list1 is None and list2 is not None:
            data2 = curr2.data
            #data1 =curr1.data
            sum = carry+data2
            if sum >= 10:
                rem = sum % 10
                result.insertEnd(rem)
                carry = 1
            else:
                result.insertEnd(sum)
                carry = 0
            curr2 = curr2.next
        elif list2 is None and list1 is not None:
            data1 = curr1.data
            sum = carry+data1
            if sum >= 10:
                result.insertEnd(sum % 10)
                carry = 1
            else:
                result.insertEnd(sum)
                carry = 0
            curr1 = curr1.next
        else:
            # list1 and list2 both have data
            data1 = curr1.data
            data2 = curr2.data
            sum = carry+data1+data2
            if sum >= 10:
                result.insertEnd(sum % 10)
                carry = 1
            else:
                result.insertEnd(sum)
                carry = 0
            curr1 = curr1.next
            curr2 = curr2.next
    if curr1 is None and curr2 is None:
        if carry>0:
            result.insertEnd(carry)
            carry=0
    return result





#TESTS
    """
    [2,4,3]
[5,6,4]
[0]
[0]
[9,9,9,9,9,9,9]
[9,9,9,9]
    """
list1 = LinkedList()
list1.insertEnd(2)
list1.insertEnd(4)
list1.insertEnd(3)
#list1.insertEnd()
#list1.insertEnd()

list2 = LinkedList()
list2.insertEnd(5)
list2.insertEnd(6)
list2.insertEnd(4)
#list2.insertEnd()
#list2.insertEnd()
#list2.insertEnd()
res = addTwoNumbers(list1,list2)
#addTwoNumbers(list2)
res.printList()
