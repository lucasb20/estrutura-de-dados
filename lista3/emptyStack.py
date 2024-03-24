
from Stack import Stack

def emptyStack(stack):
    if stack.pop() != None:
        emptyStack(stack)


s = Stack()

for i in range(10):
    s.push(i**2)

print(s)
emptyStack(s)
print(s)