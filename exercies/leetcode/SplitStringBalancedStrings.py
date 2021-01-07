class Solution:
    def balancedStringSplit(self, s: str) -> int:
        count = 0
        listl = []
        listr = []

        for c in s:
            if c is 'R':
                listr.append(c)
                if len(listr) == len(listl):
                    del listr[:]
                    del listl[:]
                    count += 1
                    continue
            elif c is 'L':
                listl.append(c)
                if len(listr) == len(listl):
                    del listr[:]
                    del listl[:]
                    count += 1
                    continue
        print(count)

    def balancedStringSplit2(self, s: str) -> int:
        stack = []
        count = 0
        for c in s:
            if not stack:
                stack.append(c)
            else:
                if stack[-1] != c:
                    stack.pop()
                    if not stack:
                        count += 1
                else:
                    stack.append(c)
        return count

s = "RLRRLLRLRL"
sol = Solution()
sol.balancedStringSplit2(s)
