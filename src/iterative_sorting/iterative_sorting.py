# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        for a in range(cur_index, len(arr)):
            if(arr[smallest_index] > arr[a]):
                smallest_index = a

        # TO-DO: swap
        temp = arr[i]
        arr[i] = arr[smallest_index]
        arr[smallest_index] = temp

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    swapped = True

    def swap(i):
        temp = arr[i]
        arr[i] = arr[i-1]
        arr[i-1] = temp
    
    if(len(arr) < 1):
        return arr

    while swapped:
        for i in range(1, len(arr)):
            for i in range(1, len(arr)):
                swapped = False
                if( arr[i-1] > arr[i]):
                    swapped = True
                    swap(i)
        if not swapped:
            break

    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):
    if maximum < 1:
        for i in arr:
          if i > maximum:
            maximum = i
    count_arr = [0] * (maximum + 1)
    for item in arr:
        count_arr[int(item)] += 1

    for i in range(1, len(count_arr)):
        count_arr[i] = count_arr[i-1] + count_arr[i];

    for i in range(len(count_arr)-1, -1, -1):
        if i != 0:
            count_arr[i] = count_arr[i-1]
        else:
            count_arr[i] = 0

    sorted_arr = [0] * len(arr)
    for i in range(0, len(arr)):
        new_index = count_arr[arr[i]]
        count_arr[arr[i]] += 1
        sorted_arr[new_index] = arr[i]
    
    arr = sorted_arr

    return arr