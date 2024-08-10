
class Node():
    def __init__(self, key):
        self.key = key
        self.parent = None
        self.left = None
        self.right = None

    def __str__(self):
        return f'Node(key={self.key})'

class AVLTree():
    def __init__(self, key = None):
        self.root = Node(key) if key is not None else None

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
    if root:
        printTree(root.left)
        print(root)
        printTree(root.right)

if __name__ == '__main__':
    avl = AVLTree()
    avl.insert(1)
    avl.insert(2)
    avl.insert(3)
    avl.insert(4)
    avl.insert(5)
    printTree(avl.root)