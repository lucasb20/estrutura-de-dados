
from node import Node
from util import Queue

def nodeCount(root):
    if not root:
        return 0
    return nodeCount(root.left) + nodeCount(root.right) + 1

def searchMax(root):
    q = Queue(nodeCount(root))
    q.enqueue(root)
    max_value = root.data
    while not q.isEmpty():
        node = q.dequeue()
        if node.data > max_value:
            max_value = node.data
        if node.left:
            q.enqueue(node.left)
        if node.right:
            q.enqueue(node.right)

    return max_value

def searchN(root, n):
    if not root:
        return False
    
    return root.data == n or searchN(root.left, n) or searchN(root.right, n)

n = Node(2)
n.left = Node(-3)
n.right = Node(7)
n.left.left = Node(5)

print(nodeCount(n))
print(searchMax(n))
print(searchN(n, 7))
print(searchN(n, 0))