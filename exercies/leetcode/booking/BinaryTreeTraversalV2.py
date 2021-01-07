class Node:
    def __init__(self, id):
        self.id = id
        self.children = []

    def add_children(self, node):
        self.children.append(node)

    def get_children(self):
        return self.children

    def get_reverse_children(self):
        children = self.children[:]
        children.reverse()
        return children


def bfs(node):
    nodes = []
    stack = [node]
    while stack:
        current_node = stack[0]
        stack = stack[1:]
        nodes.append(current_node)
        for child in current_node.get_children():
            stack.append(child)
    return nodes


def dfs(node):
    nodes = []
    stack = [node]
    while stack:
        current_node = stack[0]
        stack = stack[1:]
        nodes.append(current_node)
        for child in current_node.get_reverse_children():
            stack.insert(0, child)
    return nodes


a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
e = Node(5)
f = Node(6)
g = Node(7)

a.add_children(b)
a.add_children(c)
b.add_children(d)
b.add_children(e)
c.add_children(f)
c.add_children(g)

nodes = bfs(a)
for node in nodes:
    print(node.id)

nodes1 = dfs(a)
for node in nodes1:
    print(node.id)
