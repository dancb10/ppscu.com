class Solution(object):
    def comb(self, candidates, target, final, intermediary, i):
        if sum(intermediary) == target:
            if intermediary not in final:
                final.append(list(intermediary))
            return

        for j in range(i, len(candidates)):
            item = candidates[j]
            if item + sum(intermediary) <= target:
                intermediary.append(item)

                self.comb(candidates, target, final, intermediary, j + 1)
                intermediary.pop()

    def combinationSum2(self, candidates, target):
        final = []
        candidates.sort()
        print(candidates)
        self.comb(candidates, target, final, [], 0)

        return final

# candidates = [10, 1, 2, 7, 6, 1, 5]
# target = 8

candidates = [2, 4, 7, 2, 1, 5, 9, 3, 4, 5, 6, 7, 3, 1]
target = 7

sol = Solution()
print(sol.combinationSum2(candidates, target))
