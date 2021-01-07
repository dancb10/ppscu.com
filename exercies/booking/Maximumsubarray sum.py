# Python program to find maximum contiguous subarray sum
import sys

def maxSubArraySum(a):
    max_so_far = -sys.maxsize
    current_max = 0

    for i in range(0 , len(a)):
        current_max = current_max + a[i]
        if(max_so_far < current_max):
            max_so_far = current_max

        if current_max < 0:
            current_max = 0
    return max_so_far

def maxSubArraySum2(a):
    max_so_far = a[0]
    current_max = a[0]
    for i in range(1, len(a)):
        current_max = max(a[i], current_max + a[i])
        max_so_far = max(max_so_far, current_max)
    return max_so_far




a = [-2, -3, 4, -1, -2, 1, 5, -3]
print(maxSubArraySum2(a))
