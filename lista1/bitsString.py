
def appendAtFront(array, num):
    return [ num + i for i in array ]

def bitsString(n):
    if n == 1:
        return ["1", "0"]
    return appendAtFront(bitsString(n-1), "0") + appendAtFront(bitsString(n-1), "1")


print(bitsString(1))
print(bitsString(2))
print(bitsString(3))
print(bitsString(4))