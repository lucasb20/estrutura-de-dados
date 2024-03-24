
from Stack import Stack

def transferStack(s, t):
    aux = Stack()
    print(s, t, aux)
    while t.pop() != None:
        pass
    while not s.isEmpty():
        t.push(s.pop())


s = Stack()
t = Stack()

for i in range(10):
    s.push(2**i)
    t.push(3**(9-i))

print(s, t)
transferStack(s, t)
print(s, t)