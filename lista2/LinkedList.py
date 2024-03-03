class Node:
  def __init__(self, data=None, next=None):
    self.data = data
    self.next = next

  def __str__(self):
    return self.data.__str__()

class LinkedList(object):
  def __init__(self):
    self.length = 0
    self.head = None

  def insertAtBeginning(self, data):
    newNode = Node()
    newNode.data = data
    if self.length == 0:
      self.head = newNode
    else:
      newNode.next = self.head
      self.head = newNode
    self.length += 1

  def insertAtGivenPosition(self, pos, data):
    if pos > self.length or pos < 0:
      return None
    else:
      if pos == 0:
        self.insertAtBeginning(data)
      else:
        if pos == self.length:
          self.insertAtEnd(data)
        else:
          newNode = Node()
          newNode.data = data
          count = 1
          current = self.head
          while count < pos-1:
            count +=1
            current = current.next
          newNode.next = current.next
          current.next = newNode
          self.length +=1

  def insertAtEnd(self, data):
    newNode = Node()
    newNode.data = data
    if ( self.length == 0 ):
      self.head = newNode
      self.length +=1
      return
    current = self.head
    while current.next != None:
      current = current.next
    current.next = newNode
    self.length +=1

  def deleteAtPosition(self,pos):
    count = 0
    currentNode = self.head
    previousNode = self.head

    if pos > self.length or pos <0:
      return None
    else:
      while currentNode.next!=None or count <pos:
        count = count+1
        if count == pos:
          previousNode.next=currentNode.next
          self.length-=1
          return
        else:
          previousNode=currentNode
          currentNode=currentNode.next


  def deleteFromBeginning(self):
    if self.length != 0:
      self.head = self.head.next
      self.length -=1

  def deleteFromEnd(self):
    if self.length != 0:
      currentNode = self.getHead()
      previousNode = self.getHead()
      while currentNode.next != None:
        previousNode = currentNode
        currentNode = currentNode.next
      previousNode.next = None
      self.length -=1
 
  def __str__(self):
    array = []
    current = self.head
    while current != None:        
      array.append(current.data)
      current = current.next
    return array.__str__()

  def getNodeAtPosition(self, index):
    if self.length != 0:
      current = self.head
      i = 0
      while ( (current != None) and (i < index) ):
        current = current.next
        i += 1
      return current
    else:
      return None
    
