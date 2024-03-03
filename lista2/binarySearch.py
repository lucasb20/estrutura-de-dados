def binarySearch(array, low, high, target):
    if high < low:
        return -1
    mid = (low + high)//2
    if array[mid] == target:
        return mid
    if array[mid] > target:
        return binarySearch(array, low, mid - 1, target)
    else:
        return binarySearch(array, mid + 1, high, target)


print(binarySearch([i for i in range(25)], 0, 24, 23))