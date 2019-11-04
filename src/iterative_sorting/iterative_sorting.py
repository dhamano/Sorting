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

    return arr