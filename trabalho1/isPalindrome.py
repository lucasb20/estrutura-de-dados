
from util import Stack


def isPalindrome(expression):
    s = Stack()

    for char in expression:
        s.push(char)

    for char in expression:
        if s.pop() != char:
            return False
        
    return True


print(isPalindrome("racecar"))
print(isPalindrome("hello"))