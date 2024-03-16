
from Stack import Stack


def precedence(char1, char2):
    ops = "()*/+-"
    return ops.index(char1) < ops.index(char2)

def infixaToPosfixa(exp):
    stack = Stack()
    posfixa = ""

    for c in exp:
        if c in "()*/+-":
            while not stack.isEmpty() and precedence(c,stack.peek()):
                if stack.peek() not in "()":
                    posfixa+=stack.pop()
                else:
                    stack.pop()
                if c == "(": break
            stack.push(c)
        else:
            posfixa+=c

    while not stack.isEmpty():
        if stack.peek() not in "()":
            posfixa+=stack.pop()
        else:
            stack.pop()
    return posfixa


print(infixaToPosfixa("A*B-(C+D)+E"))