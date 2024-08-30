
class HashTable:
    def __init__(self, table_len):
        self.table = list()
        for _ in range(table_len):
            self.table.append(list())

    def func_hash(self, key):
        return (3*key + 5) % 11
    
    def insert(self, key):
        index = self.func_hash(key)
        bucket = self.table[index]
        if key not in bucket:
            bucket.append(key)
    
    def __str__(self):
        return str(self.table)

if __name__ == '__main__':
    table = HashTable(11)

    keys = [12, 44, 13, 88, 23, 97, 11, 39, 20, 16, 5]
    for key in keys:
        table.insert(key)
    
    print(table)