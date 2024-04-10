
from Node import Node


def morrisPreOrder(root):
    current = root
    while current:
        if not current.left:
            print(current.data)
            current = current.right
        else:
            predecessor = current.left
            while predecessor.right and predecessor.right != current:
                predecessor = predecessor.right

            if not predecessor.right:
                predecessor.right = current
                print(current.data)
                current = current.left

            else:
                predecessor.right = None
                current = current.right


n = Node(2)
n.left = Node(-3)
n.right = Node(7)
n.left.left = Node(5)
n.left.right = Node(4)

print(morrisPreOrder(n))
# 2 -> -3 -> 5 -> 4 -> 7