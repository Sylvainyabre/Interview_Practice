def mergeSort(arr):
    if len(arr) <= 1:
        return 

    # dividing
    mid = len(arr)//2
    print(min)
    arr1 = arr[:mid]
    arr2 = arr[mid:]

    # conquering with recursion
    mergeSort(arr1)
    mergeSort(arr2)
    return merge(arr1, arr2, arr)


def merge(arr1, arr2, arr):
    i = 0
    j = 0
    k = 0

# while we have not reached the end of both arrays
    while k < len(arr):
        # if we have reached the end of arr2 or if the
        # ith element of arr1 is smaller than the jth element of arr2
        # if j== len(arr2) or (i<len(arr1) and arr1[i]<arr2[j]):
        #     arr[i+j] = arr1[i]
        #     i +=1
        # else:
        #     arr[i+j] = arr2[j]
        #     j +=1

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
    pass


arr = [1, 32, 100, -9, 43, -56, 23, -254, 400, -12,]
sorted =  selectionSort(arr)#mergeSort(arr)
print(sorted)
# print(findMin(arr,0))
