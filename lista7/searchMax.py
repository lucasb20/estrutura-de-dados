from Heap import Heap
import math
import random

def searchMax(heap : Heap):
    h = math.floor(math.log2(len(heap.heapList)))
    if h == 0:
        return heap.heapList[0]
    maxNumbers = heap.heapList[2**(h - 1) - 1:]
    return max(maxNumbers)

if __name__ == '__main__':
    heap = Heap()
    for _ in range(20):
        num = random.randint(0, 200)
        heap.add(num, 0)
    print(heap.heapList)
    print(searchMax(heap))