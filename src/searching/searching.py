# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    # Your code here
    
    if end >= start: #check if haven't seached entire list
        center = (end + start) // 2
        if arr[center] == target:
            return center
        elif arr[center] > target:
            return binary_search(arr, target, start, center - 1)
        else:
            return binary_search(arr, target, center + 1, end)
    else:
        return - 1

# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
# def agnostic_binary_search(arr, target):
#     # Your code here

