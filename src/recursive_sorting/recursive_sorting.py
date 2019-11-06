# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    # TO-DO
    i = 0; a = 0; b = 0
    while elements > 0:
        # print(f"elements: {elements} | a: {a} | len(arrA): {len(arrA)-1} | b: {b} | len(arrB): {len(arrB)-1}")
        if elements == 1:
            if arrA[a] > arrB[b]:
                merged_arr[i] = arrA[a]
            else:
                merged_arr[i] = arrB[b]
            elements -=1
        else:            
            if a < len(arrA) and arrA[a] < arrB[b]:
                # print(f'left: {arrA[a]}')
                merged_arr[i] = arrA[a]
                if(a < len(arrA)-1):
                    a += 1;
                i +=1; elements -=1
            elif b < len(arrB):
                # print(f'right: {arrB[b]}')
                merged_arr[i] = arrB[b]
                if(b < len(arrB)-1):
                    b += 1;
                i +=1; elements -=1
        # print(f"a: {a} | b: {b} | elements: {elements}")
    
    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO
        elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    # TO-DO
    i = 0; a = 0; b = 0
    while elements > 0:
        # print(f"elements: {elements} | a: {a} | len(arrA): {len(arrA)-1} | b: {b} | len(arrB): {len(arrB)-1}")
        if elements == 1:
            if arrA[a] > arrB[b]:
                merged_arr[i] = arrA[a]
            else:
                merged_arr[i] = arrB[b]
            elements -=1
        else:            
            if a < len(arrA) and arrA[a] < arrB[b]:
                # print(f'left: {arrA[a]}')
                merged_arr[i] = arrA[a]
                if(a < len(arrA)-1):
                    a += 1;
                i +=1; elements -=1
            elif b < len(arrB):
                # print(f'right: {arrB[b]}')
                merged_arr[i] = arrB[b]
                if(b < len(arrB)-1):
                    b += 1;
                i +=1; elements -=1
        # print(f"a: {a} | b: {b} | elements: {elements}")
    
    return merged_arr

# print(merge([1,3,5,7,9,11], [2,4,6,8,10,12]))
# print(merge([1,3,5,7,9,11,13], [2,4,6,8,10,12]))
import math

def merge_sort(arr):
    half = math.floor(len(arr)/2); left = []; right = []

    def merge_arr(arr1, arr2):
        merged = []; els = len(arr1) + len(arr2); a = 0; b = 0
        for i in range(0, els):
            if i == els-1:
               if a < len(arr1):
                    merged.append(arr1[a])
                else:
                    merged.append(arr2[b])
            else:
                if b == len(arr2) or a < len(arr1) and arr1[a] < arr2[b]:
                    merged.append(arr1[a])
                    a += 1
                else:
                    merged.append(arr2[b])
                    b += 1
        return merged
    
    if(len(arr) > 2):
        left = arr[:half]
        right = arr[half:]
        left = merge_sort(left)
        right = merge_sort(right)
    elif(len(arr) <= 2):
        left = arr[:half]
        right = arr[half:]
        
    return merge_arr(left, right)

# merge_sort([9,1,2,5,4,3,7,8,6])
merge_sort([9,1,2,5,4,3,7,8,6,10,19,18,12,11,14,15,17,16])

# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
