class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        summ = 0
        for nr in range(1, int(num/2) + 1):
            if num % nr == 0:
                summ += nr
        return summ == num

s = Solution()
print(s.checkPerfectNumber(30402457))
