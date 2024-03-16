
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

def solvePosfix(posfix):
    stack = Stack()
    for c in posfix:
        if c in "*/+-":
            op1 = stack.pop()
            op2 = stack.pop()
            stack.push(exec(op2, op1, c))
        else:
            stack.push(int(c))
    return stack.pop()


print(solvePosfix("1234-*+5+"))