def binarySearch(arr,low, high, num):
    midNum = (high + low)//2
    if arr[midNum] == num:
        return midNum
    elif arr[midNum] > num:
        return binarySearch(arr, 0, midNum, num) 
    elif arr[midNum] < num:
        return binarySearch(arr, midNum, high, num)
    else:
        return -1



