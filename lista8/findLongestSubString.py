

class HashTable:
    def __init__(self, table_len):
        self.table = list()
        for _ in range(table_len):
            self.table.append(list())

    def func_hash(self, key):
        mask = (1 << 32) - 1
        h = 0
        for char in key:
            h = (h << 5 & mask) | (h >> 27)
            h += ord(char)
        return h % len(self.table)
    
    def search(self, key):
        index = self.func_hash(key)
        bucket = self.table[index]
        for pair in bucket:
            if pair[0] == key:
                return pair[1]

    def insert(self, key, value):
        index = self.func_hash(key)
        bucket = self.table[index]
        for index, pair in enumerate(bucket):
            if pair[0] == key:
                bucket[index] = (key, value)
                return
        bucket.append((key, value))

    def remove(self, key):
        index = self.func_hash(key)
        bucket = self.table[index]
        for index in range(len(bucket)):
            if bucket[index][0] == key:
                pair = bucket.pop(index)
                return pair[1]

    def __str__(self):
        return str(self.table)

def findLongestSubString(data : str):
    n = len(data)
    table = HashTable(n)
    start = 0
    max_length = 0
    sub_string = ''
    for end in range(n):
        char = data[end]
        value = table.search(char)
        if value is not None and value >= start:
            start = value + 1
        table.insert(char, end)
        length = end - start + 1
        if length > max_length:
            max_length = length
            sub_string = data[start : end + 1]
    return sub_string

if __name__ == '__main__':
    data = "abcabcbb"
    print(data)
    print(findLongestSubString(data))