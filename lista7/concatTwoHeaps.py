
from Heap import Heap
import random

def concatTwoHeaps(heap1 : Heap, heap2 : Heap):
    heap = Heap()
    items = heap1.heapList + heap2.heapList
    for item in items:
        heap.add(item.key, item.value)
    return heap

if __name__ == '__main__':
    heap1, heap2 = Heap(), Heap()
    for _ in range(7):
        heap1.add(random.randint(0, 20), 0)

    for _ in range(3):
        heap2.add(random.randint(0, 20), 0)
    
    heap = concatTwoHeaps(heap1, heap2)
    print(heap.heapList)