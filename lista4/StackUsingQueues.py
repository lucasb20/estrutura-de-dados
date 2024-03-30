from Queue import Queue

class Stack:
    def __init__(self, size_max):
        self.queue1 = Queue(size_max)
        self.queue2 = Queue(size_max)

    def push(self, element):
        self.queue1.enqueue(element)

    def pop(self):
        if self.empty():
            return None

        while self.queue1.size() > 1:
            self.queue2.enqueue(self.queue1.dequeue())

        data = self.queue1.dequeue()

        while not self.queue2.isEmpty():
            self.queue1.enqueue(self.queue2.dequeue())

        return data

    def peek(self):
        if self.empty():
            return None

        while self.queue1.size() > 1:
            self.queue2.enqueue(self.queue1.dequeue())

        data = self.queue1.dequeue()
        self.queue2.enqueue(data)

        while not self.queue2.isEmpty():
            self.queue1.enqueue(self.queue2.dequeue())

        return data
    
    def isEmpty(self):
        return self.queue1.isEmpty() and self.queue2.isEmpty()
