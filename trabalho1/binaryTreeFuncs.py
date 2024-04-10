
from node import Node
from util import Queue

def nodeCount(root : Node):
    if not root:
        return 0
    return nodeCount(root.left) + nodeCount(root.right) + 1

def searchMax(root : Node):
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

n = Node(2)
n.left = Node(-3)
n.right = Node(7)
n.left.left = Node(5)

print(nodeCount(n))
print(searchMax(n))