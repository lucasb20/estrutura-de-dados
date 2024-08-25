from Heap import Heap

class Queue:
    def __init__(self):
        self.heap = Heap()
        self.index = -1
    
    def enqueue(self, value):
        self.index += 1
        self.heap.add(self.index, value)

    def dequeue(self):
        return self.heap.removeMin()
    
    def isEmpty(self):
        return len(self.heap.heapList) == 0
    
if __name__ == '__main__':
    queue = Queue()
    queue.enqueue(4)
    queue.enqueue(12)
    queue.enqueue(3)
    queue.enqueue(6)
    queue.enqueue(-1)
    queue.enqueue(8)
    
    while not queue.isEmpty():
        print(queue.dequeue())