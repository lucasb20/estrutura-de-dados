
class Stack:
    def __init__(self):
        self.A = []
        self.count = 0

    def push(self, data):
        self.A.append(data)
        self.count+=1

    def pop(self):
        if self.count == 0:
            return None
        self.count-=1
        return self.A.pop()
    
    def peek(self):
        return None if self.count == 0 else self.A[-1]
    
    def isEmpty(self):
        return self.count == 0
