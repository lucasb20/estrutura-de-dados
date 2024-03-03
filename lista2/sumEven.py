import random
import LinkedList

def sumEven(list):
    curr = list.head
    sum = 0
    while curr != None:
        if curr.data % 2 == 1:
            sum += curr.data
        curr = curr.next
    return sum

l = LinkedList.LinkedList()

for _ in range(10):
    l.insertAtBeginning(random.randint(-10,10))

print(l)
print(sumEven(l))