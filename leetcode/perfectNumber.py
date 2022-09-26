"""A perfect number is a positive integer that is equal to the sum of its positive divisors,
 excluding the number itself. A divisor of an integer x is an integer that can divide x evenly.
Given an integer n, return true if n is a perfect number, otherwise return false.



Example 1:

Input: num = 28
Output: true
Explanation: 28 = 1 + 2 + 4 + 7 + 14
1, 2, 4, 7, and 14 are all divisors of 28.
Example 2:

Input: num = 7
Output: false


Constraints:

1 <= num <= 108
    """

"""if m is a divisor of n, then k = n/m is also a divisor of n, because mk = n. Thus, the positive divisors can be organized into pairs of the form (m, n/m), where m < n/m. The one exception to this is if n is a perfect square and m = sqrt(n), 
    in which case m = n/m. For example, if n = 100, then the positive divisors of n are given by ...
    """




from math import sqrt
def checkPerfectNumber(num):
    div = 1
    sum = 0
    while div < int(sqrt(num)):
        if num%div == 0:
            
           if div == 1 or div == num/div:
            sum += div
           else :
            sum += div +num/div
        div += 1

    print(sum)

    return sum == num


i = checkPerfectNumber(6)
print(i)
