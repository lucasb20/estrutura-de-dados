import LinkedList

def twoCircular(l):
    fast = slow = l.head
    i = 0
    list1 = LinkedList.LinkedList()
    list2 = LinkedList.LinkedList()
    while True:
        if fast.next == None: break
        fast = fast.next
        if i % 2 == 0:
            list1.insertAtEnd(slow.data)
            slow = slow.next
        i+=1
    while slow != None:
        list2.insertAtEnd(slow.data)
        slow = slow.next
    curr1 = list1.head
    curr2 = list2.head
    while curr1.next != None:
        curr1 = curr1.next
    while curr2.next != None:
        curr2 = curr2.next
    curr1.next = list1.head
    curr2.next = list2.head

    return list1, list2


l = LinkedList.LinkedList()

data = [1,2,6,13,34]

for d in data:
    l.insertAtEnd(d)


print(l)
list1, list2 = twoCircular(l)
print(list1.circularPrint(), list2.circularPrint())