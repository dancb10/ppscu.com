class Node:

    def __init__(self, id):
        self.id = id
        self.children = []

    def add_child(self, node):
        self.children.append(node)

    def get_children(self):
        return self.children

    def get_rev_children(self):
        children = self.children[:]
        children.reverse()
        return children

def dfs(root):
    nodes = []
    stack = [root]
    while stack:
        current_node = stack[0]
        stack = stack[1:]
        nodes.append(current_node)
        for child in current_node.get_rev_children():
            stack.insert(0, child)
    return nodes


def bfs(root):
    nodes = []
    stack = [root]
    while stack:
        current_node = stack[0]
        stack = stack[1:]
        nodes.append(current_node)
        for child in current_node.get_children():
            stack.append(child)
    return nodes




a0 = Node("1")
b0 = Node("2")
b1 = Node("3")
c0 = Node("4")
c1 = Node("5")

a0.add_child(b0)
a0.add_child(b1)
b0.add_child(c0)
b0.add_child(c1)

nodes1 = bfs(a0)
for node in nodes1:
    print(node.id)

nodes = dfs(a0)
for node in nodes:
    print(node.id)
