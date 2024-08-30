
from HashTable import HashTable as Base

class HashTable(Base):
    def __init__(self, table_len, secondary_table_len):
        self.table = list()
        for _ in range(table_len):
            self.table.append([None] * secondary_table_len)

    def func_hash2(self, key):
        m = len(self.table[0])
        return m - (key % m)

    def insert(self, key):
        index = self.func_hash(key)
        table = self.table[index]
        index = self.func_hash2(key)
        k = 0
        while k != len(table):
            if table[index] is None:
                table[index] = key
                return
            index = (index + 1) % len(table)
            k+=1

if __name__ == '__main__':
    table = HashTable(11, 7)

    keys = [12, 44, 13, 88, 23, 97, 11, 39, 20, 16, 5]
    for key in keys:
        table.insert(key)
    
    print(table)