# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        for x in arr[i:]:
            if x <= arr[smallest_index]:
                smallest_index = arr.index(x)

        # TO-DO: swap
        arr[i], arr[smallest_index] = arr[smallest_index], arr[i]
    
    return arr

# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    #get length
    length = len(arr)
    #set iteration to length
    for item in range(length):
        #create a variables to track swaps and array positions
        swap_count = False
        #iterate through array starting at the first element
        for i in range(0, length - item - 1):
            #if item on the lhs is bigger, swap, and update counters
            if arr[i] > arr[i + 1]:
                swap_count = True
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
        if swap_count != True:
            break
    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr