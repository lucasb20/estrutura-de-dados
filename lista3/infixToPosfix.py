
from Stack import Stack


def infixToPosfix(infix):
    posfix = ""
    stack = Stack()
    for c in infix:
        if c in "(":
            stack.push(c)
        elif c in ")":
            while stack.peek() != "(":
                posfix+=stack.pop()
        elif c in "+-":
            while not stack.isEmpty() and stack.peek() != "(":
                posfix+=stack.pop()
            stack.push(c)
        elif c in "*/":
            while not stack.isEmpty() and (stack.peek() not in "(+-"):
                posfix+=stack.pop()
            stack.push(c)
        else:
            posfix+=c

    while not stack.isEmpty():
        if stack.peek() not in "()": posfix+=stack.pop()
        else: stack.pop()

    return posfix


print(infixToPosfix("A*B-(C+D)+E"))
print(infixToPosfix("A+B*(C-D)+E"))