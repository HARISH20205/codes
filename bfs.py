class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def bfs(root):
    if not root:
        return

    queue = []
    queue.append(root)

    while queue:
        n = len(queue)
        for i in range(n):
            node = queue.pop(0)
            print(node.val, end=' ')

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        print()


if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    bfs(root)
