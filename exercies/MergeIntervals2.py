#Given a list of intervals, e.g. [1,4], [2,5], [6,7], merge overlapping intervals, e.g. [1,5],[6,7].
# booking

# [0 lowEnd, 1 highEnd]

class Solution:
    def merge(self, intervals: [[int]]) -> [[int]]:
        merged = []
        for interval in sorted(intervals):
            if merged and interval[0] <= merged[-1][1]:
                merged[-1][1] = max(interval[1], merged[-1][1])
            else:
                merged.append(interval)
        print(merged)


a = [[1,4], [1,2], [2,5], [8, 12], [9, 10], [6,7]]
s = Solution()
s.merge(a)

