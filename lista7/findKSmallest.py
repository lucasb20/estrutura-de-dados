
from Heap import Heap
import random

def findKSmallest(heap : Heap, k):
    if len(heap.heapList) < k:
        return None
    elements = sorted(heap.heapList.copy())
    return elements[k - 1]

if __name__ == '__main__':
    heap = Heap()
    for _ in range(20):
        heap.add(random.randint(10, 100), 0)
    print(heap.heapList)
    print(findKSmallest(heap, 3))