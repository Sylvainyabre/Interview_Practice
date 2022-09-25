
def mergeSort(arr):
    if len(arr) <= 1:
        return arr

    # dividing
    mid = len(arr)//2
    #print(min)
    arr1 = arr[:mid]
    arr2 = arr[mid:]

    # conquering with recursion
    mergeSort(arr1)
    mergeSort(arr2)
    return merge(arr1, arr2, arr)

"""
This uses the approach of dividing and conquering.add()The array is 
recursively split down to individual items.
The helper function merge() then scans through the array and 
joins the items by creating the order
"""
def merge(arr1, arr2, arr):
    i = 0 # index in the sub-array arr1
    j = 0 # index in sub-array  arr2 
    k = 0 # index in the main array arr

# while we have not reached the end of both arrays
    while k < len(arr):
        # pick from the second array if we reached the end of the first array
        if i >= len(arr1):
            arr[k] = arr2[j]
            k += 1
            j += 1

        # pick from the first array if we reached the end of the second array
        elif j >= len(arr2):
            arr[k] = arr1[i]
            k += 1
            i += 1

        # if both arrays are non empty, pick the smaller of arr1[i] and arr2[2]
        else:
            if arr1[i] <= arr2[j]:
                arr[k] = arr1[i]
                i += 1
                k += 1
            else:
                arr[k] = arr2[j]
                j += 1
                k += 1

    return arr

"""
arr should not contain duplicate values
this algorithm runs in O(n^2)
Approach: Scan through the array, between the current index and the end
of the array,find the minimum and swap it with the current element

"""
def selectionSort(arr):
    i = 0
    while i < len(arr):
        # find the index of min in arr
        min = findMin(arr,i)
        minIndex = arr.index(min)
        print(min)
        #swap min and the ith element of arr 
        arr[i], arr[minIndex] = arr[minIndex],arr[i]
        i += 1
    return arr


def findMin(arr, i):
    min = arr[i]
    while i < len(arr):
        if arr[i] < min:
            min = arr[i]
        i += 1
    return min


def quickSort(arr):
    if len(arr)<=1:
        return 
    else:
        pivot = arr[len(arr)-1]
        left = []
        right = []
        for item in arr:
            if item<pivot:
                left.append(item)
            else:
                right.append(item)
        left = quickSort(left)
        right = quickSort(right) 
        result = [*left,pivot,*right]
        return result


def partition(arr, low, high):
    pivot = arr[high] 


arr = [1, 32, 100, -9, 43, -56, 23, -254, 400, -12,]
# sorted =  selectionSort(arr)#mergeSort(arr)
sorted = quickSort(arr)
print(sorted)
# print(findMin(arr,0))
