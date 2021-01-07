from collections import Counter


def single_number(nums):
    counts = Counter(nums)
    for key in counts:
        if counts[key] == 1:
            print(key)


def single_number2(nums):
    counts = Counter(nums)
    list = dict((filter(lambda elem: elem[1] != 2, counts.items())))
    print(list.keys())


def single_number3(nums):
    d = {}
    for num in nums:
        if num in d:
            d[num] += 1
        else:
            d[num] = 1
    for key in d:
        if d[key] == 1:
            print(key)

input = [4, 1, 2, 1, 2]
single_number3(input)
