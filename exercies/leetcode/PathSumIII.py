class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


g = TreeNode(11)
g.val = 11
g.left = None
g.right = None

i = TreeNode(-2)
i.val = -2
i.left = None
i.right = None

j = TreeNode(1)
j.val = 1
j.left = None
j.right = None

h = TreeNode(3)
h.val = 3
h.left = None
h.right = None

c = TreeNode(3)
c.val = 3
c.left = h
c.right = i

d = TreeNode(2)
d.val = 2
d.left = None
d.right = j

b = TreeNode(-3)
b.val = -3
b.left = None
b.right = g

a = TreeNode(5)
a.val = 5
a.left = c
a.right = d

r = TreeNode(10)
r.val = 10
r.left = a
r.right = b


class Solution:

    def pathSum(self, root: TreeNode, sum: int) -> int:
        print(root.val)
        if root.left is not None:
            sum += root.left.value
            self.pathSum(root.left, sum)
        if root.right is not None:
            self.pathSum(root.right, sum)

suma = 8

sol = Solution()
sol.pathSum(r, suma)
