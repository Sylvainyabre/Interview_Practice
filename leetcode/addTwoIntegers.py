"""Given two non-negative integers, num1 and num2 represented as string,
 return the sum of num1 and num2 as a string.

You must solve the problem without using any built-in library for handling large integers (such as BigInteger). 
You must also not convert the inputs to integers directly.



Example 1:

Input: num1 = "11", num2 = "123"
Output: "134"
Example 2:

Input: num1 = "456", num2 = "77"
Output: "533"
Example 3:

Input: num1 = "0", num2 = "0"
Output: "0"


Constraints:

1 <= num1.length, num2.length <= 104
num1 and num2 consist of only digits.
num1 and num2 don't have any leading zeros except for the zero itself.
    """
  
from collections import deque


# def addTwoIntegers(num1,num2):
#     list1 = list(num1)
#     list2 = list(num2)
#     list1.reverse()
#     list2.reverse()
#     carry = 0
#     result = ""
#     for val1,val2 in zip(list1,list2):
#         sum = int(val1)+int(val2)+carry
       
#         if sum>=10:
#             result += str(sum%10)
#             carry = 1
#         else:
#             result += str(sum)
#             carry = 0
        
#     if carry>1:
#         result += str(carry)
#     return result




def addTwoStrings(num1, num2):
    list1 = list(num1)
    list2 = list(num2)
    list1.reverse()
    list2.reverse()
    print(list1,list2)
    maxIndex = max(len(list1), len(list2))
    carry = 0
    result = []
    ret = ""
    i = 0
    while i < maxIndex:
        if i < len(list1) and i < len(list2):
            n1 = int(list1[i])
            n2 = int(list2[i])
            sum = n1+n2+carry
            if sum >= 10:
                ret += str(sum % 10)
                carry = 1
            else:
                ret += str(sum)
                carry = 0
            i = i+1
        elif i >= len(list1) and i < len(list2):
            sum = int(list2[i])+carry
            if sum >= 10:
                ret += str(sum % 10)
                carry = 1
            else:
                ret += str(sum)
                carry = 0
            i = i+1
        elif i >= len(list2) and i < len(list1):
            sum = int(list1[i])+carry
            if sum >= 10:
                ret += str(sum % 10)
                carry = 1
            else:
                ret += str(sum)
                carry = 0
            i = i+1
    if carry>0: # if there is a final carry over
        ret += str(carry)
    # print(result)
    # for val in result:
    #     ret += str(val)
    res = list(ret)
    res.reverse()
    print(res)
    return "".join(res)


num1 = "456"
num2 = "77" 
res = addTwoStrings(num1,num2)
print(id(0))