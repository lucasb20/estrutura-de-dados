
class Node():
    def __init__(self, key = None):
        self.key = key
        self.parent = None
        self.left = None
        self.right = None

    def __str__(self):
        return f'Node(key={self.key})'

class AVLTree():
    def __init__(self, key = None):
        self.root = Node(key)

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
            return
        
        node = self.root
        while True:
            if key == node.key:
                return
            elif key < node.key:
                if not node.left:
                    node.left = Node(key)
                    node.left.parent = node
                    return
                node = node.left
            else:
                if not node.right:
                    node.right = Node(key)
                    node.right.parent = node
                    return
                node = node.right

def printTree(root : Node):
    if not root:
        return
    printTree(root.left)
    print(root)
    printTree(root.right)