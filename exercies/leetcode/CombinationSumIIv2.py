# """
# candidates = [10,1,2,7,6,1,5], target = 8
# A solution set is:
# [
#   [1, 7],
#   [1, 2, 5],
#   [2, 6],
#   [1, 1, 6]
# ]
# """
# candidates = [10,1,2,7,6,1,5]
# target = 8
#
# # candidates = [2,5,2,1,2]
# # target = 5
#
    # def cand_combinations(cand, tar):
    #     # combinations = []
    #     length = len(candidates)
    #     sorted_c = sorted(candidates)
    #     for i in range(length):
    #         temp_sum = 0
    #         buffer = []
    #         locked = sorted_c[i]
    #         if locked < tar:
    #             temp_sum += locked
    #             buffer.append(locked)
    #             for j in sorted_c[i+1:]:
    #                 temp_sum += j
    #                 buffer.append(j)
    #                 # print("temp_sum II: " + str(temp_sum))
    #                 # print("buffer II: " + str(buffer))
    #                 if temp_sum > tar:
    #                     temp_sum -= j
    #                     buffer.pop()
    #                 if temp_sum == tar:
    #                     print("good combination: " + str(buffer))
    #                     temp_sum = 0
    #                     buffer = []
    #         if locked == tar:
    #             print("good combination: " + str([locked]))
#
#
# def combinationSum2(C: [int], t: int) -> [[int]]:
#     L, A, _ = len(C), [], C.sort()
#     def dfs(I, P, S):
#         if S == t: return A.append(P)
#         for i in range(I,L):
#             if i > I and C[i] == C[i - 1]: continue
#             if S + C[i] > t: break
#             dfs(i + 1, P + [C[i]], S + C[i])
#     dfs(0, [], 0)
#     return A
#
# print(combinationSum2(candidates, target)
#
class Solution:
    def combinationSum2(self, candidates: [int], target: int) -> [[int]]:

        candidates.sort()

        print(candidates)
        def fn(nums, x, i=0):
            """backtracking algorithm"""
            for k in range(i, len(candidates)):
                if k > i and candidates[k] == candidates[k - 1]: continue  # break repetition
                if candidates[k] > x:
                    break
                elif candidates[k] == x:
                    ans.append(nums + [candidates[k]])
                else:
                    fn(nums + [candidates[k]], x - candidates[k], k + 1)  # break repetition

        ans = []
        fn([], target)
        return ans


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        self.partial_sum = 0
        self.candidates = candidates
        self.target = target
        self.partial_solution = []
        self.solutions = set()
        self.bk(0)
        return [list(x) for x in self.solutions]

    def bk(self, i):
        if i >= len(self.candidates):
            return

        if self.partial_sum + self.candidates[i] > self.target:
            # skip
            self.bk(i + 1)
            return

        self.partial_solution.append(self.candidates[i])
        self.partial_sum += self.candidates[i]

        if self.partial_sum == self.target:
            # add solution
            self.solutions.add(tuple(sorted(self.partial_solution)))
        else:
            self.bk(i + 1)

        self.partial_solution.pop()
        self.partial_sum -= self.candidates[i]
        self.bk(i + 1)

candidates = [10,1,2,7,6,1,5]
target = 8
sol = Solution()
print(sol.combinationSum2(candidates, target))
