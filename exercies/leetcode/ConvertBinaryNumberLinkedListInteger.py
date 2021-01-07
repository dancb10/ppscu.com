class Node:
    def __init__(self, value, next):
        self.value = value
        self.next = next

e = Node(1, None)
d = Node(0, e)
c = Node(1, d)
b = Node(0, c)
a = Node(1, b)


def getDecimalValue(head):
    ans = 0
    while head:
        ans = 2 * ans + head.val
        head = head.next
    return ans


print(getDecimalValue(a))
