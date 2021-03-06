# Stack class as helper
class Stack(object):
    def __init__(self):
        self.items = []
    
    def __len__(self):
        return self.size()

    def size(self):
        return len(self.items)

    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        if not self.is_empty():
            return self.items.pop()

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
    
    def is_empty(self):
        return len(self.items) == 0

# Node Class
class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# Binary Tree Class
class BinaryTree(object):
    def __init__(self, root):
        self.root = Node(root)

    
    # Size of Binary tree: No. of nodes present in the tree
    # method-1: Iterative approach
    def size_iterative(self):
        if self.root is None:
            return 0
        
        stack = Stack()
        stack.push(self.root)
        size = 1
        while stack:
            node = stack.pop()
            if node.left:
                size += 1
                stack.push(node.left)
            if node.right:
                size += 1
                stack.push(node.right)
        return size

    # Method-2: Recursive approach
    def size_recursive(self, node):
        if node is None:
            return 0
        return 1 + self.size_recursive(node.left) + self.size_recursive(node.right)


tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)

print(tree.size_iterative())
print(tree.size_recursive(tree.root))