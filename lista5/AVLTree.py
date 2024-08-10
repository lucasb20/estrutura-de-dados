
class Node():
    def __init__(self, key = None):
        self.key = None
        self.parent = None
        self.left = None
        self.right = None

class AVLTree():
    def __init__(self, key : Node = None):
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
                    return
                node = node.left
            else:
                if not node.right:
                    node.right = Node(key)
                    return
                node = node.right
