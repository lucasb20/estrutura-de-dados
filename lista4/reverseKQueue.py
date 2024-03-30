
from Queue import Queue
from StackUsingQueues import Stack


def reverseKQueue(queue, k):
    stack = Stack(queue.size_max)

    for _ in range(k):
        stack.push(queue.dequeue())
    for _ in range(k):
        queue.enqueue(stack.pop())

    count = queue.count - k

    for _ in range(count):
        queue.enqueue(queue.dequeue())


q = Queue(10)

for i in range(10):
    q.enqueue(i*25)

print(q)
reverseKQueue(q, 4)
print(q)