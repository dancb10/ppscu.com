J = "aA"
S = "aAAbbbb"

class Solution:
    def numJewelsInStones(self, j: str, s: str) -> int:
        nr = 0
        for stone in s:
            if stone in j:
                nr += 1
        return nr

s = Solution()
print(s.numJewelsInStones(J, S))
