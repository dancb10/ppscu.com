class Solution:
    def maximum69Number (self, num: int) -> int:
        return int(str(num).replace('6', '9', 1))

    def maximum69Number2(self, num: int) -> int:
        i = j = 0
        original_num = num

        while num != 0:
            i += 1
            d = num % 10

            if d == 6:
                j = i

            num //= 10

        print(original_num + int(pow(10, j-1))*3)

sol = Solution()
# print(sol.maximum69Number(9669))

print(sol.maximum69Number2(9699))



