#Input:
#[4,3,2,7,8,2,3,1]

#Output:
#[5,6]
from collections import Counter


def find_disappeared(nums):
    counts = Counter(nums)
    new_list = []
    for i in range(1, len(nums) + 1):
        if i not in counts:
            new_list.append(i)
    return new_list


def find_disappeared2(nums):
    nums = set(nums)
    return [x for x in range(1, len(nums) + 1) if x not in nums]


def findDisappearedNumbers(nums):
    for i in range(len(nums)):
        index = abs(nums[i]) - 1
        nums[index] = - abs(nums[index])

    print(nums)
    return [i + 1 for i in range(len(nums)) if nums[i] > 0]


my_input = [4, 3, 2, 7, 8, 2, 3, 1]
print(findDisappearedNumbers(my_input))
