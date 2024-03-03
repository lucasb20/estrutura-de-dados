import LinkedList

def interlaceLists(list1, list2):
    l = LinkedList.LinkedList()
    curr = list1.head
    while curr != None:
        l.insertAtEnd(curr.data)
        curr = curr.next
    curr = list2.head
    while curr != None:
        l.insertAtEnd(curr.data)
        curr = curr.next
    return l

list1 = LinkedList.LinkedList()
list2 = LinkedList.LinkedList()

for d in range(1,4):
    list1.insertAtEnd(d)
    list2.insertAtEnd(d+3)

print(list1, list2)
print(interlaceLists(list1, list2))