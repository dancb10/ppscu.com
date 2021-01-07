#Input: [3,2,3]
#Output: 3

#Input: [2,2,1,1,1,2,2]
#Output: 2

from collections import Counter


def majority_element(nums):
    maj = len(nums)/2
    counts = Counter()
    for num in nums:
        counts[num] += 1
    if counts.most_common()[0][1] >= maj:
        return counts.most_common()[0][0]


def majority_element2(nums):
    return Counter(nums).most_common(1)[0][0]

my_input = [2, 2, 1, 1, 1, 2, 2]
print(majority_element2(my_input))

