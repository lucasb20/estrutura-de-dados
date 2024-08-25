class Item:
    def __init__(self, k, v):
        self.key = k
        self.value = v

    def isEmpty(self):
        return len(self)==0

    def __lt__(self, other):
        return self.key < other.key
       
    def __gt__(self,other):
        return self.key > other.key
    
    def __str__(self):
        return f"(key={self.key}, value={self.value})"
    
    def __repr__(self):
        return str(self)

class Heap:
    def __init__(self):
        self.heapList = []
    
    def parent(self, index):
        return (index - 1) // 2

    def leftChild(self, index):
        return 2*index + 1
    def rightChild(self,index):
        return 2*index + 2

    def hasLeft(self,index):
        return self.leftChild(index) < len(self.heapList)
    def hasRight(self,index):
        return self.rightChild(index) < len(self.heapList)
   
    def swap(self, i, j):
        self.heapList[i], self.heapList[j] = self.heapList[j], self.heapList[i]

    def upHeap(self, j):
        parent = self.parent(j)
        if j > 0:
            if self.heapList[j] < self.heapList[parent]:
                self.swap(j,parent)
                self.upHeap(parent)

    def downHeap(self, j):
        if self.hasLeft(j):
            left = self.leftChild(j)
            small_child = left
            if self.hasRight(j):
                right = self.rightChild(j)
                if self.heapList[right] < self.heapList[left]:
                    small_child = right
            if self.heapList[small_child] < self.heapList[j]:
                self.swap(j, small_child)
                self.downHeap(small_child)

    def add(self, key, value):
        self.heapList.append(Item(key, value))
        if len(self.heapList) > 1:
            self.upHeap(len(self.heapList) - 1)

    def min(self):
        if len(self.heapList) > 0:
            item = self.heapList[0]
            return item

    def removeMin(self):
        if len(self.heapList) > 0:
            self.swap(0, len(self.heapList) - 1)
            item = self.heapList.pop()
            self.downHeap(0)
            return item