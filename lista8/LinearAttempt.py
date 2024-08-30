
from HashTable import HashTable as Base

class HashTable(Base):
    def __init__(self, table_len):
        self.table = [None]*table_len
    
    def insert(self, key):
        index = self.func_hash(key)
        print("key:", key, "index:", index)
        k = 0
        while k != len(self.table):
            if self.table[index] is None:
                self.table[index] = key
                return
            index = (index + 1) % len(self.table)
            k+=1

if __name__ == '__main__':
    table = HashTable(11)

    keys = [12, 44, 13, 88, 23, 97, 11, 39, 20, 16, 5]
    for key in keys:
        table.insert(key)
    
    print(table)