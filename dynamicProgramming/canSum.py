
from typing import List


def canSum(targetSum:int, nums:List[int]):
    """Write a `function canSum(targetSum,numbers)` that takes in a targeSum 
    and an array of numbers as arguments. The function should return a boolean indicating
    whether or not it is possible to generate the targetSum using numbers from the array.
    You may use an element of the array as many times as needed.
    You may assume that all input numbers are nonnegative.
    Example `canSum(7,[5,3,6,8,9,2,7])-> true`
            `canSum(8,[5,1])-> false`
            `canSum(17,[3,6,1,0,8,4,5])->true`
       """
    if targetSum == 0:
        return True
    if targetSum < 0:
        return False

    for n in nums:
        if canSum(targetSum-n, nums) == True:
            return True

    return False


print(canSum(17, [3, 6, 1, 0, 8, 4, 5]))
print(canSum(7, [5, 3, 6, 8, 9, 2, 7]))
print(canSum(1, [3, 6, 0, 8, 4, 5, 0, .6, 0.4]))
