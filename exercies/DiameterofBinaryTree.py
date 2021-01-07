# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# class Solution:
    # def deepthOfBinaryTree(self, root: TreeNode) -> int:
    #     diameter = 1
    #     if root.left:
    #         self.deepthOfBinaryTree(root.left)
    #         diameter += 1
    #     if root.right:
    #         self.deepthOfBinaryTree(root.right)
    #         diameter += 1
    #     return diameter

class Solution(object):
    def diameterOfBinaryTree(self, root):
        self.d = 0
        def dfs(node):
            if not node:
                return 0
            l, r = dfs(node.left), dfs(node.right)
            self.d = max(l + r, self.d)
            return 1 + max(l, r)
        dfs(root)
        return self.d


    def sizeOfBinaryTree(self, root):
        size = 1
        if root.left is not None:
            size += self.sizeOfBinaryTree(root.left)
        if root.right is not None:
            size += self.sizeOfBinaryTree(root.right)
        return size


f = TreeNode(6)
f.left = None
f.right = None

e = TreeNode(5)
e.left = None
e.right = f

d = TreeNode(4)
d.left = None
d.right = None

c = TreeNode(3)
c.left = None
c.right = None

b = TreeNode(2)
b.left = e
b.right = d

a = TreeNode(1)
a.left = b
a.right = c

# solution = Solution()
# print(solution.deepthOfBinaryTree(a))
#
solution = Solution()
print(solution.sizeOfBinaryTree(a))
