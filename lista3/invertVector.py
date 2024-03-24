
from Stack import Stack

def invertVector(v : list):
    stack = Stack()
    for element in v:
        stack.push(element)
    v.clear()
    while not stack.isEmpty():
        v.append(stack.pop())


v = [2**i for i in range(10)]

print(v)
invertVector(v)
print(v)