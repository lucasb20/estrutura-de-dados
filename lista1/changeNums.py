def zeraPares(n):
    if n < 10:
        return 0 if n % 2 == 0 else n
    if n % 2 == 0:
        return zeraPares(n//10)*10
    else:
        return zeraPares(n//10)*10 + n%10

print(zeraPares(1234))