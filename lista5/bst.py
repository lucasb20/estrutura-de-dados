class Node():
    def __init__(self, key):
        self.key = key
        self.left : Node = None
        self.right : Node = None

    def __str__(self):
        left = self.left.key if self.left else None
        right = self.right.key if self.right else None
        return f'Node(key={self.key}, left={left}, right={right})'
    
    def __repr__(self):
        return str(self.key)

def TreeToArray(root : Node):
    arr : list[Node] = list()
    if not root: return arr
    arr.append(root)
    i = 0
    while i < len(arr):
        if arr[i] is None:
            i+=1
            continue
        arr.append(arr[i].left)
        arr.append(arr[i].right)
        i+=1
    return arr

def search(root : Node, key):
    if not root:
        return False
    if root.key == key:
        return True
    elif key < root.key:
        return search(root.left, key)
    else:
        return search(root.right, key)

def insert(root: Node, key):
    if not root:
        return Node(key)
    if root.key == key:
        return root
    elif key < root.key:
        root.left = insert(root.left, key)
        return root
    else:
        root.right = insert(root.right, key)
        return root

def findMin(root : Node):
    curr = root
    while curr.left:
        curr = curr.left
    return curr

def remove(root: Node, key):
    if not root:
        return None
    if key < root.key:
        root.left = remove(root.left, key)
    elif key > root.key:
        root.right = remove(root.right, key)
    else:
        if not root.left:
            return root.right
        elif not root.right:
            return root.left
        successor = findMin(root.right)
        root.key = successor.key
        root.right = remove(root.right, successor.key)
        return root

if __name__ == '__main__':
    node = insert(None, 12)
    insert(node, 6)
    insert(node, 8)
    insert(node, 15)
    print(TreeToArray(node))