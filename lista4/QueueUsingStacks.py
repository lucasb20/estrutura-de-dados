
from StackUsingQueues import Stack

class Queue:
    def __init__(self):
        self.rear = Stack()
        self.front = Stack()

    def enqueue(self, item):
        self.rear.push(item)

    def dequeue(self):
        if self.front.isEmpty():
            while not self.rear.isEmpty():
                self.front.push(self.rear.pop())
        return self.front.pop()

    def isEmpty(self):
        return self.rear.isEmpty() and self.front.isEmpty()
    