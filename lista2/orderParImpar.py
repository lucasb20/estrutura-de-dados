import random

def orderParImpar(array, index = 0):
    if index == len(array):
        return array
    if array[index] % 2 == 0:
        num = array.pop(index)
        array.insert(0,num)
    return orderParImpar(array, index + 1)


array = [random.randint(0,50) for _ in range(10)]
print(array)
print(orderParImpar(array))