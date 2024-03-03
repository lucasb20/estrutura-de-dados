def hanoi(n, begin = 1, inter = 2, destiny = 3):
    if n == 1:
        print("move the disk from tower %s to tower %s." % (begin, destiny))
    else:
        hanoi(n-1, begin, destiny, inter)
        print("move the disk from tower %s to tower %s." % (begin, destiny))
        hanoi(n-1, inter, begin, destiny)

hanoi(3)