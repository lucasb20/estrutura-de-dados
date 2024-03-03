def zeraPares(n):
    if n < 10:
        return 0 if n % 2 == 0 else n
    if n % 2 == 0:
        return zeraPares(n//10)*10
    else:
        return zeraPares(n//10)*10 + n%10

def removeImpares(n):
    if n < 10:
        return 0 if n % 2 == 1 else n
    if n % 2 == 1:
        return removeImpares(n//10)
    else:
        return removeImpares(n//10)*10 + n%10

def inverte(n, i=0):
    if n < 10:
        return i*10+n
    return inverte(n//10, i*10 + n%10)

print(zeraPares(1234))
print(removeImpares(1234))
print(inverte(1234))