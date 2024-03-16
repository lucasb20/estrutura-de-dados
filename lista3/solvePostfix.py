
from Stack import Stack


def exec(op1, op2, op):
    if op == "+":
        return op1 + op2
    elif op == "-":
        return op1 - op2
    elif op == "*":
        return op1 * op2
    else:
        return op1 / op2

def solvePostfix(postfix):
    stack = Stack()
    for c in postfix:
        if c in "*/+-":
            op1 = stack.pop()
            op2 = stack.pop()
            stack.push(exec(op2, op1, c))
        else:
            stack.push(int(c))
    return stack.pop()


print(solvePostfix("1234-*+5+"))