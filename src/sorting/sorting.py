# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements

    # Your code here

    indexA = 0 #current index of arrA
    indexB = 0 #current index on arrB
    mergeIndex = 0 #Index to place lowest value in merged_arr
          
    while indexA < len(arrA) and indexB < len(arrB): 
        if arrA[indexA] < arrB[indexB]: 
            merged_arr[mergeIndex] = arrA[indexA] 
            indexA += 1
        else: 
            merged_arr[mergeIndex] = arrB[indexB] 
            indexB += 1
        mergeIndex += 1
        
    while indexA < len(arrA): 
        merged_arr[mergeIndex] = arrA[indexA] 
        indexA += 1
        mergeIndex += 1
        
    while indexB < len(arrB): 
        merged_arr[mergeIndex] = arrB[indexB] 
        indexB += 1
        mergeIndex += 1
    
    return merged_arr

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    # Your code here
    if len(arr) > 1:
        #Var Assignment
        center = len(arr) // 2
        arrA = arr[:center]
        arrB = arr[center:]
        #Recursion
        arrA = merge_sort(arrA)
        arrB = merge_sort(arrB)
        arr = merge(arrA, arrB)
    return arr

# print(merge_sort([7,1,5,4,8,9,5]))

# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
#def merge_in_place(arr, start, mid, end):
    # Your code here


#def merge_sort_in_place(arr, l, r):
    # Your code here

