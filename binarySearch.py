def binarySearch(arr,num):
    midNum = len(arr)//2
    if arr[midNum] == num:
        return midNum
    elif arr[midNum] > num:
        return binarySearch(arr[0:midNum],num) if midNum else -1
    return binarySearch(arr[midNum:],num) if midNum else -1


print(binarySearch([0,1,2,3,4,5],4))
