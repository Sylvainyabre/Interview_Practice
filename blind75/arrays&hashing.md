# Problems and Solutions

## Contains duplicates [Easy]

Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

 

Example 1:

Input: nums = [1,2,3,1]
Output: true
Example 2:

Input: nums = [1,2,3,4]
Output: false
Example 3:

Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true
 

Constraints:

1 <= nums.length <= 105
-109 <= nums[i] <= 109


## Solution

```python
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        """
          
        """
        nums_set = set(nums)
        if(len(nums)>len(nums_set)):
            return True
        return False
```

## Valid Anangrams [Easy]

Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
 

Constraints:

1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.
 

Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?

## Solution O(N)

```python
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        t_list = list(t)
        s_list = list(s)
        if len(s_list) != len(t_list):
            return False
        else:
            for letter in t_list:
                if letter not in s_list:
                    return False
                s_list.remove(letter)
            return len(s_list)==0
```

We can also check if collections.Counter(t)==collections.Counter(s). collections.Counter(str) returns a dictionary where keys are individual letters and values are counts of these letters in str

## Two Sum [Easy]

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
 

Constraints:

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.
 

Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?


## Solution O(n)

```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diffs = {}
        for  idx,num in enumerate(nums):
            diff = target-num
            if diff in diffs:
                return [idx,diffs[diff]]
            diffs[num] = idx

```

## Group anagrams [Medium]
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Example 2:

Input: strs = [""]
Output: [[""]]
Example 3:

Input: strs = ["a"]
Output: [["a"]]
 

Constraints:

1 <= strs.length <= 104
0 <= strs[i].length <= 100
strs[i] consists of lowercase English letters.


## Solution

```python
import collections
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        anagrams = {}
        for word in strs:
            key = collections.Counter(list(word))
            key = str(len(list(word)))+"".join(sorted(word))
            if key not in list(anagrams.keys()):
                anagrams[key] = [word]
            else:
               anagrams[key].append(word)
        return list(anagrams.values())

```

## Top K frequent Elements [Medium]

Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

 

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]
 

Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104
k is in the range [1, the number of unique elements in the array].
It is guaranteed that the answer is unique.
 

Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size.

## Solution

```python
 

```
