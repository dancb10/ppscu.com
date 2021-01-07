class Solution:
    def decompressRLElist(self, nums: [int]) -> [int]:
        result = []
        for index in range(0, len(nums), 2):
            for repeat in range(1, nums[index]+1):
                result.append(nums[index+1])
        return result

solution = Solution()
mylist = [1, 2, 3, 4]
print(solution.decompressRLElist(mylist))
