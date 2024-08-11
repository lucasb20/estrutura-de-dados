class Node():
    def __init__(self, key):
        self.key = key
        self.left : Node = None
        self.right : Node = None

def search(root : Node, key):
    if not root:
        return False
    if root.key == key:
        return True
    elif key < root.key:
        return search(root.left, key)
    else:
        return search(root.right, key)

if __name__ == '__main__':
    node = Node(12)
    node.left = Node(6)
    node.left.right = Node(8)
    node.right = Node(15)
    for i in range(16):
        print(f"{i}:{search(node, i)}")