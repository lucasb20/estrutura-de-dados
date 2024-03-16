
from Stack import Stack


def exec(op1, op2, op):
    if op == "+":
        return op1 + op2
    elif op == "-":
        return op2 - op1
    elif op == "*":
        return op1 * op2
    else:
        return op2 / op1

def solvePosfix(posfix):
    stack = Stack()
    for c in posfix:
        if c in "*/+-":
            op1 = stack.pop()
            op2 = stack.pop()
            stack.push(exec(op1, op2, c))
        else:
            stack.push(int(c))
        print(c, stack)
    return stack.pop()


print(solvePosfix("12*34+5+-"))