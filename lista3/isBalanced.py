
from Stack import Stack


def isBalanced(expression):
    opening = ["{", "[", "("]
    closing = ["}", "]", ")"]
    
    stack = Stack()
    for letter in expression:
        if letter in opening:
            stack.push(letter)
        elif letter in closing:
            if letter == "}" and stack.pop() != "{":
                return False
            elif letter == "]" and stack.pop() != "[":
                return False
            elif letter == ")" and stack.pop() != "(":
                return False
    
    return stack.isEmpty()


print(isBalanced("[c[((b))a]]"))
print(isBalanced("[{a[]]d)"))
print(isBalanced("[[((f))j]]"))
print(isBalanced("[[(("))
print(isBalanced("]](())"))