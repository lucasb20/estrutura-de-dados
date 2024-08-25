from Heap import Heap
import random

def findBiggestPair(arr1 : list, arr2 : list):
    heap = Heap()
    for i, pair in enumerate(zip(arr1, arr2)):
        if i == 0:
            heap.add(0, pair)
        else:
            if pair > heap.min().value:
                heap.add(heap.min().key - 1, pair)
            else:
                heap.add(heap.min().key + 1, pair)
    return heap.min().value

if __name__ == '__main__':
    arr1, arr2 = list(), list()
    for _ in range(20):
        arr1.append(random.randint(0, 20))
        arr2.append(random.randint(0, 20))
    print(arr1)
    print(arr2)
    print(findBiggestPair(arr1, arr2))