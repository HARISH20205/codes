class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def dfs_recursive(node):
    if node is None:
        return
    print(node.value)
    dfs_recursive(node.left)
    dfs_recursive(node.right)


root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))
dfs_recursive(root)
