from Heap import Heap

class priorityQueue:
    def __init__(self):
        self.heap = Heap()
    
    def add(self, key, value):
        self.heap.add(key, value)
    
    def remove_min(self):
        return self.heap.removeMin()

    def get_min(self):
        return self.heap.min()