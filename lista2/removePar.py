import LinkedList

def removePar(list : LinkedList.LinkedList):
    prev = list.head
    curr = prev.next
    while curr != None:
        if curr.data % 2 == 0:
            curr = curr.next
            prev.next = curr
        else:
            prev = prev.next
            curr = curr.next

            

l = LinkedList.LinkedList()

data = [1,2,6,13,34]

for d in data:
    l.insertAtEnd(d)

print(l)
removePar(l)
print(l)