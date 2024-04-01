import timeit

def BinarySearchRecursive(arr, l, r, x):
 
    # Check base case
    if r >= l:
 
        mid = l + (r - l) // 2
 
        # If element is present at the middle itself
        if arr[mid] == x:
            return mid
 
        # If element is smaller than mid, then it
        # can only be present in left subarray
        elif arr[mid] > x:
            return BinarySearchRecursive(arr, l, mid-1, x)
 
        # Else the element can only be present
        # in right subarray
        else:
            return BinarySearchRecursive(arr, mid + 1, r, x)
 
    else:
        # Element is not present in the array
        return -1

def BinarySearchIterative(arr ,l, r, x):
    while l <= r:
        mid = l (r-1)//2

        if arr[mid] == x:
            return mid

        elif arr[mid] < x:
            l = mid + 1
        
        else: 
            r = mid - 1

    return -1


arr=[0,1,2,3,4,5,6,7,8,9,10,11,12,20,21,24,26,27,30,31,34]
x = 27

if __name__ == "__main__": 
    firsttime = timeit.default_timer()
    result_rec = BinarySearchRecursive(arr, 0, len(arr)-1, x)
    time_rec = timeit.default_timer() - firsttime

    secondtime = timeit.default_timer()
    result_iter = BinarySearchRecursive(arr, 0, len(arr)-1, x) 
    time_iter = timeit.default_timer() - secondtime

    if result_iter == -1 & result_rec == -1:
        print("element not in array")
        print(f"recursive time: {time_rec} ,,,,,,, iterative time: {time_iter}")

    else:
        print(f"element found at {result_rec}")
        print(f"recursive time: {time_rec} ,,,,,,, iterative time: {time_iter}")