# Problems solved with two pointers

## Valid palindrome

A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

- Solution

 ```Python
     def isPalindrome(self, s: str) -> bool:
        chars = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
        lst = list(filter(lambda x:x in chars or x.isnumeric(),list(s.lower())))
        i = 0
        while i<=len(lst)-1:
            if lst[i] != lst[len(lst)-i-1]:
                return False
            i+=1
        return True

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1

        while l < r:
            curSum = numbers[l] + numbers[r]

            if curSum > target:
                r -= 1
            elif curSum < target:
                l += 1
            else:
                return [l + 1, r + 1]

```

## Two sum II

Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.

Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.

The tests are generated such that there is exactly one solution. You may not use the same element twice.

Your solution must use only constant extra space.Ç

- Solution

```Python

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for idx,n in enumerate(numbers):
            # if (n>=0 and target>=0 and n>target) or (n<0 and target<0 and n<target) :
            #     continue
            subList = numbers[idx+1:]
            if target-n in subList:
                 
                return [idx+1,subList.index(target-n)+idx+2]

```
