# https://www.geeksforgeeks.org/perfect-sum-problem-print-subsets-given-sum/
"""
Input : arr[] = {2, 3, 5, 6, 8, 10}
        sum = 10
Output : 5 2 3
         2 8
         10
"""


class Solution:

    def comb(self, numbers: [int], trg: int, final: [int], buffer: [int], index: int):
        if sum(buffer) == trg:
            if buffer not in final:
                final.append(list(buffer))
            return

        for j in range(index, len(numbers)):
            locked = numbers[j]
            if locked + sum(buffer) <= trg:
                buffer.append(locked)

                self.comb(numbers, trg, final, buffer, j + 1)
                buffer.pop()

    def combination_sum(self, numbers: [int], target: int):
        final = []
        numbers.sort()
        self.comb(numbers, target, final, [], 0)

        return final

# 2 3 5 6 8 10
candidates = [10, 1, 2, 7, 6, 1, 5]
target = 8


sol = Solution()
print(sol.combination_sum(candidates, target))
