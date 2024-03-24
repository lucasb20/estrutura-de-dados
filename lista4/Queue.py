
class Queue:
    def __init__(self, size_max):
        self.rear = 0
        self.front = 0
        self.count = 0
        self.size_max = size_max
        self.A = [None]*size_max
    
    def enqueue(self, data):
        if self.count < self.size_max:
            self.A[self.rear] = data
            self.rear= (self.rear + 1) % self.size_max
            self.count+=1

    def dequeue(self):
        if self.count > 0:
            data = self.A[self.front]
            self.A[self.front] = None
            self.count-=1
            self.front= (self.front + 1) % self.size_max
            return data

    def __str__(self):
        return self.A.__str__()