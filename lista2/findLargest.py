import random

def findLargest(array, index = 0):
    if index == len(array):
        return array[0]
    
    first = array[index]
    largest = findLargest(array, index + 1)
    if first > largest:
        return first
    else:
        return largest

array = [random.randint(0,25) for _ in range(5)]

print(array)
print(findLargest(array))