class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def merge_lists(l1, l2):
    dummy = cur = ListNode(0)

    while l1 and l2:
        if l1.val < l2.val:
            cur.next = l1
            l1 = l1.next
        else:
            cur.next = l2
            l2 = l2.next
        cur = cur.next
    cur.next = l1 or l2
    return dummy.next


l1 = [1, 2, 4, 6, 8]
l2 = [1, 3, 4]

e1 = ListNode(8)
e1.next = None

d1 = ListNode(6)
d1.next = e1

c1 = ListNode(4)
c1.next = d1

b1 = ListNode(2)
b1.next = c1

a1 = ListNode(1)
a1.next = b1


c2 = ListNode(4)
c2.next = None

b2 = ListNode(3)
b2.next = c2

a2 = ListNode(1)
a2.next = b2

d = merge_lists(a1, a2)
current = d
print("None -> ")
while current.next is not None:
    print("{} ->".format(current.val))
    current = current.next
print("None")
