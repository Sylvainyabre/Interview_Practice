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

> Use a priority queue, compute frequencies, put the (-freq, num) in queue and pop k elements

```python
 
import collections
from queue import PriorityQueue
class Solution:
    
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        pq = PriorityQueue()
        returned = []
    
        counts = collections.Counter(nums)
        counts = dict(counts)
        for num in counts.keys():
            pq.put((-counts[num],num))

        while k>0:
            val = pq.get()
            k -=1
            returned.append(val[1])

        return returned
```

## Product of Array Except Self

Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]

Constraints:

2 <= nums.length <= 105
-30 <= nums[i] <= 30
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space for space complexity analysis.)

## Solution

> create two list, one for the prefix multiples and the other for suffix multiples.
> Next, iterate through nums and multiply prefix by suffix

```python
class Solution:
        
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        products = []
        prefix = [1]*len(nums)
        suffix = [1]*len(nums)
        for idx,num in enumerate(nums):
            if idx==0:
               prefix[idx]=num
            else:
                prefix[idx] = (prefix[idx-1]*nums[idx])
        step = len(nums)-1
        while step>0:
            if step==len(nums)-1:
                suffix[step] =nums[step]
            else:
                suffix[step] = suffix[step+1]*nums[step]
            step -=1
        for i in range(len(nums)):
            if i==0:
                products.append(suffix[i+1]) 
            elif i==len(nums)-1:
                products.append(prefix[i-1])
            else:
                products.append(prefix[i-1]*suffix[i+1])
        return products

```

## Valid Sudoku [Medium]

Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.

### Solution

```Python
from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Each row contains 1-9 without repetition
        # Each column contains 1-9 without repetition
        # Each of the nine 3 x 3 sub-boxes of the grid must 
        # contain the digits 1-9 without repetition
        rows = defaultdict(set) # key is the row order and value is content
        cols = defaultdict(set) # #key is the col order and value is content
        smallSquares = defaultdict(set)
        dot = "."
        DIM = 9


        for r in range(DIM):
            for c in range(DIM):
                cell = board[r][c]
                if cell == dot:
                   continue # Only care about digits
                elif cell in rows[r]:
                    return False
                elif cell in cols[c]:
                    return False
                elif cell in smallSquares[(r//3,c//3)]:
                    return False
                else:
                    rows[r].add(cell)
                    cols[c].add(cell)
                    smallSquares[(r//3,c//3)].add(cell)
        return True
    
```

## Encode and Decode strings

Description
Design an algorithm to encode a list of strings to a string. The encoded string is then sent over the network and is decoded back to the original list of strings.

Please implement encode and decode

## Solution

- Encode:
 choose a fixed delimiter, for example "$". Add the lenght of each word followed by the delimeter and join all the words together

 ```Python
def encode(strs):
   output = ""
   delim = "@"
   for st in strs:
   output = str(len(st))+delim+st
   return output
      

 ```

- Decode:
 iterate through the encoded string, find the position of the delimiter and get the length. Use the length and the delimiter to extract the word

 ```Python
 def decode(st):
    delim = "@"
    output = []
    i = 0
    while i<len(st):
       j = i
       while st[j]!=delim
          j+=1
        length = int(st[i:j])
        output.append(st[j+1:j+1+length])
        i = j+1+length
    return output


 ```

## Longest Consecutive sequence [Medium]
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

 

Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
Example 2:

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
 

Constraints:

0 <= nums.length <= 105
-109 <= nums[i] <= 109

## Solution

One obvious but wrong solution is to sort the numbers and loop over but that would be O(NlogN)
```Python
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ls = set(nums) #remove duplicates
        
        max_size=0
       
        for num in ls:
            if num-1 not in ls:
                curr_size =1
                diff = 1
                while (num+diff) in ls:
                    curr_size +=1
                    diff +=1
                max_size =max(curr_size,max_size)
                
        return max_size
```
