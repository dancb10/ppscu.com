class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        nr = n % 10
        summ = nr
        prod = nr
        n = int(n/10)
        while n:
            nr = n % 10
            summ += nr
            prod *= nr
            n = int(n/10)
        return prod-summ

number = 234
s = Solution()
print(s.subtractProductAndSum(number))
