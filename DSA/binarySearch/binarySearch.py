
# [1,2,3,4,5]
from typing import List


def search(arr, key, low: int, high: int):
    
    if len(arr) <= 0:
        return -1
    if high >= low:
        mid = (low+high)//2
        if arr[mid] == key:
            return mid
        elif key < arr[mid]:
            return search(arr, key, low, mid-1)
        elif key > arr[mid]:
            return search(arr, key, mid+1, high)
    else:
      return -1


def binarySearch(key, arr: List):
    """uses the binary search algorithm to find an element in arr

    Args:
       key:(Any): the key whose index we want to find in arr
       arr:List the SORTED array to search in
    Returns: The index of key in arr or -1 if it does not exist
    """
    arr.sort()
    return search(arr, key, 0, len(arr)-1)
