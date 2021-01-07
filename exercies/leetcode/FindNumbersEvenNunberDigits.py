# Given an array nums of integers, return how many of them contain an even number of digits.


class Solution:

    def findNumbers(self, nums: [int]) -> int:
        if len(nums) < 1 or len(nums) > 500:
            return False
        nrs = 0
        for nu in nums:
            if nu < 1 or nu > 10 ** 5:
                return False
            if len(str(nu)) % 2 == 0:
                nrs += 1
        return nrs

nums = [12, 345, 2, 6, 7896]
s = Solution()
print(s.findNumbers(nums))
