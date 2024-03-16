
from Stack import Stack


def infixToPostfix(infix):
    postfix = ""
    stack = Stack()
    for c in infix:
        if c in "(":
            stack.push(c)
        elif c in ")":
            while stack.peek() != "(":
                postfix+=stack.pop()
        elif c in "+-":
            while not stack.isEmpty() and stack.peek() != "(":
                postfix+=stack.pop()
            stack.push(c)
        elif c in "*/":
            while not stack.isEmpty() and (stack.peek() not in "(+-"):
                postfix+=stack.pop()
            stack.push(c)
        else:
            postfix+=c

    while not stack.isEmpty():
        if stack.peek() not in "()": postfix+=stack.pop()
        else: stack.pop()

    return postfix


print(infixToPostfix("A*B-(C+D)+E"))
print(infixToPostfix("A+B*(C-D)+E"))