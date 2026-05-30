class Node :
    def __init__(self, key):
        self.value = key
        self.left = None
        self.right = None
        self.height = 1

def height(n):
    return n.height if n else 0

def balance(n):
    return height(n.left) - height(n.right) if n else 0

def right_rotate(y):
    x = y.left
    y.left = x.right
    x.right = y

    y.height = 1 + max(height(y.left), height(y.right))
    x.height = 1 + max(height(x.left), height(x.right))

    return x

def left_rotate(x):
    y = x.right
    x.right = y.left
    y.left = x

    x.height = 1 + max(height(x.left), height(x.right))
    y.height = 1 + max(height(y.left), height(y.right))

    return y

def insert(root, key):
    if not root:
        return Node(key)
    
    if key < root.value:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)

    root.height = 1 + max(height(root.left), height(root.right))

    b = balance(root)

    # Rotasi 
    if b > 1 and key < root.left.value:
        return right_rotate(root)

    if b < -1 and key > root.right.value:
        return left_rotate(root)

    if b > 1 and key > root.left.value:
        root.left = left_rotate(root.left)
        return right_rotate(root)

    if b < -1 and key < root.right.value:
        root.right = right_rotate(root.right)
        return left_rotate(root)

    return root

def inorder(node):
    if node:
        inorder(node.left)
        print(node.value, end=" ")
        inorder(node.right)

# Main
data = [30, 10, 20]
root = None

for x in data:
    root = insert(root, x)

print("Inorder Traversal of the AVL Tree is:")
inorder(root)