def sumfirstNs(n):
    if n == 0:
        return 0
    return n + sumfirstNs(n-1)


print(sumfirstNs(4))