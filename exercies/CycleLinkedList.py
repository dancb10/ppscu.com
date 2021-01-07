from collections import Counter

class ListNode:
    def __init__(self, x, next):
        self.val = x
        self.next = next


class Solution:
    # def hasCycle(self, head: ListNode) -> bool:
    #     if not head:
    #         return False
    #     if not head.next:
    #         return False
    #     p1 = head
    #     p2 = head.next
    #     while p1 and p2 and p2.next:
    #         if p1 == p2:
    #             return False
    #         else:
    #             p1 = p1.next
    #             p2 = p2.next.next
    #     return False

    # def hasCycle(self, head: ListNode) -> bool:
    #     while head:
    #         try:
    #             print(head.val)
    #         except RecursionError:
    #             return True
    #         head = head.next
    #     return False

    def hasCycle(self, head: ListNode) -> bool:
        visited = {}
        while head:
            if head not in visited:
                visited[head] = 1
            else:
                return True
            head = head.next
        return False


d = ListNode(-4, None)
c = ListNode(0, d)
b = ListNode(2, c)
a = ListNode(3, b)
d.next = b
s = Solution()
print(s.hasCycle(a))
