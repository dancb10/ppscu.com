class TreeNode:

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def max_depth(self, root: TreeNode) -> int:
    stack = [(1, root)]
    max_level = 1
    while stack:
        level, node = stack.pop()
        if max_level < level:
            max_level = level
        if node.left:
            stack.append((level + 1, node.left))
        if node.right:
            stack.append((level + 1, node.right))
    return max_level

input = [3,9,20,None,None,15,7]
tree = []
a = TreeNode()
print(max_depth(root=tree[0]))
