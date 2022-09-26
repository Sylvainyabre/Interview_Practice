""" from AMAZON SDE Internship Online Assessment
Write a function that takes two parameters:
    - An array of integers
    - A 2-D array of integers eg: [[2,4],[3,5]...]
then each array in the 2-D array represents indices in the main array that have to be reversed. 
both ends of each array in the 2-D array are inclusive
"""
def inverse(arr,indices):
    start,end = indices
    while start != end:
        endElem = arr[end]
        arr[end] = arr[start]
        arr[start] = endElem
        end -=1
        start +=1

def performInverses(arr,arrs):
    for ar in arrs:
        inverse(arr,ar)
    return arr


arr = [1,2,3,5,4,7,8]
arrs = [[1,5],[2,4],[3,5]]
# [1,5]-->[1,7,4,5,3,2,8]
# [2,4]-->[1,7,3,5,4,2,8]
# [3,5]-->[1,7,3,2,4,5,8]

print(performInverses(arr,arrs))