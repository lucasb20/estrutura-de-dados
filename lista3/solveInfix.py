
from Stack import Stack

def precedence(op):
    precedences = {
        "+" : 1,
        "-" : 1,
        "*" : 2,
        "/" : 2
        }
    return precedences.get(op, 0)

def exec(op1, op2, op):
    if op == "+":
        return op1 + op2
    elif op == "-":
        return op1 - op2
    elif op == "*":
        return op1 * op2
    elif op == "/":
        return op1 / op2

def solveInfix(infix):
    operators = Stack()
    operands = Stack()
    for c in infix:
        if c == "(":
            operators.push(c)
        elif c == ")":
            while operators.peek() != "(":
                op = operators.pop()
                op2 = operands.pop()
                op1 = operands.pop()
                operands.push(exec(op1, op2, op))
            operators.pop()
        elif c in "*/+-":
            while not operators.isEmpty() and precedence(operators.peek()) >= precedence(c):
                op = operators.pop()
                op2 = operands.pop()
                op1 = operands.pop()
                operands.push(exec(op1, op2, op))
            operators.push(c)
        else:
            operands.push(int(c))

    while not operators.isEmpty():
        op = operators.pop()
        op2 = operands.pop()
        op1 = operands.pop()
        operands.push(exec(op1, op2, op))

    return operands.pop()


print(solveInfix("1+2*(3-4)+5"))