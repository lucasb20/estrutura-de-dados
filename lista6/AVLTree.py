
class Node():
    def __init__(self, key):
        self.key = key
        self.parent : Node = None
        self.left : Node = None
        self.right : Node = None

    def __str__(self):
        parent = self.parent.key if self.parent else None
        left = self.left.key if self.left else None
        right = self.right.key if self.right else None
        return f'Node(key={self.key}, parent={parent}, left={left}, right={right})'
    
    def __hash__(self):
        return hash(self.key)

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
                return node
            elif key < node.key:
                if not node.left:
                    node.left = Node(key)
                    node.left.parent = node
                    return node.left
                node = node.left
            else:
                if not node.right:
                    node.right = Node(key)
                    node.right.parent = node
                    return node.right
                node = node.right

    @staticmethod
    def rotate(x : Node):
        y = x.parent
        z = y.parent

        x.parent = z
        if z.left == y:
            z.left = x
        else:
            z.right = x

        if y.left == x:
            y.left = x.right
            if y.left:
                y.left.parent = y
            x.right = y
            y.parent = x
        else:
            y.right = x.left
            if y.right:
                y.right.parent = y
            x.left = y
            y.parent = x

def printTreePreOrder(root : Node):
    if root:
        print(root)
        printTreePreOrder(root.left)
        printTreePreOrder(root.right)

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
    node = avl.insert(5)
    AVLTree.rotate(node)
    printTree(avl.root)