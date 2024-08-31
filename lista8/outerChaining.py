
class HashTable:
    def __init__(self, table_len):
        self.table = list()
        for _ in range(table_len):
            self.table.append(list())

    def func_hash(self, key):
        return (3*key + 1) % len(self.table)
    
    def search(self, key):
        index = self.func_hash(key)
        bucket = self.table[index]
        return key in bucket

    def insert(self, key):
        index = self.func_hash(key)
        bucket = self.table[index]
        if key not in bucket:
            bucket.append(key)

    def remove(self, key):
        index = self.func_hash(key)
        bucket = self.table[index]
        for index in range(len(bucket)):
            if bucket[index] == key:
                bucket.pop(index)
                return

    def __str__(self):
        return str(self.table)

if __name__ == '__main__':
    table = HashTable(7)

    keys = [12, 44, 13, 88, 23, 97, 11]
    for key in keys:
        table.insert(key)
    
    print(table)

    print(table.search(11))
    print(table.search(69))
    print(table.search(13))

    table.remove(13)
    print(table)
    print(table.search(13))