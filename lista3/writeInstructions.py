
from Stack import Stack


def printInstructions(op1, op2, c, register):
    op = {
        "*" : "MT",
        "/" : "DV",
        "+" : "AD",
        "-" : "SB",
    }

    print(f"LD {op1}")
    print(f"{op.get(c)} {op2}")
    print(f"ST {register}")

def writeInstructions(postfix):
    stack = Stack()

    for c in postfix:
        if c in "*/+-":
            op2 = stack.pop()
            op1 = stack.pop()
            TEMPn = "TEMP"+str(stack.count)
            stack.push(TEMPn)
            printInstructions(op1, op2, c, TEMPn)
        else:
            stack.push(c)


writeInstructions("ABC*+DE-/")