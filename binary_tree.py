class Node:
    def __init__(self, value=0) -> None:
        self.val = value
        self.left = None
        self.right = None

class Binary:
    def __init__(self, root: Node) -> None:
        self.root = root

    def add_left(self, parent: Node, value: int):
        if parent is not None:
            parent.left = Node(value)
        else:
            print("Parent node is None.")

    def add_right(self, parent: Node, value: int):
        if parent is not None:
            parent.right = Node(value)
        else:
            print("Parent node is None.")


root = Node(1)
binary_tree = Binary(root)
binary_tree.add_left(root, 2)
binary_tree.add_right(root, 3)

def print_tree(node: Node, level=0):
    if node is not None:
        print(" " * (level * 4) + f"Node({node.val})")
        print_tree(node.left, level + 1)
        print_tree(node.right, level + 1)
    
print_tree(binary_tree.root)
