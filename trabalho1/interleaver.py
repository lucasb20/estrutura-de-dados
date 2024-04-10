
from util import Stack, Queue


def interleaver(s):
    q = Queue(s.count)

    count = s.count // 2

    for _ in range(count): q.enqueue(s.pop())

    while not s.isEmpty():
        q.enqueue(q.dequeue())
        q.enqueue(s.pop())

    return q


stack = Stack()
stack.push(5)
stack.push(2)
stack.push(3)
stack.push(4)

print(stack)
print(interleaver(stack))
