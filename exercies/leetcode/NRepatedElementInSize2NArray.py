from collections import Counter
class Solution:
    def repeatedNTimes(self, a: [int]) -> int:
        counter = Counter(a)
        return counter.most_common(1)[0][0]

a = [1,2,3,3]
s = Solution()
print(s.repeatedNTimes(a))
