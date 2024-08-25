from Heap import Heap
import random

def findSmallerThenK(heap : Heap, k):
    if len(heap.heapList) == 0 or not heap.heapList[0].key < k:
        return []
    items = [heap.heapList[0]]
    h = 1
    while True:
        aux = []
        for element in heap.heapList[2**h - 1 : 2**(h+1) - 1]:
            if element.key < k:
                aux.append(element)
        if len(aux) == 0:
            break
        items.extend(aux)
        h += 1
    return items

if __name__ == '__main__':
    heap = Heap()
    for _ in range(20):
        heap.add(random.randint(10, 100), 0)
    print(heap.heapList)
    print(findSmallerThenK(heap, 30))