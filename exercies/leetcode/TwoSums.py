def twoSums(mylist, target):
    d = {}
    for index, value in enumerate(mylist):
        no = target - value
        if no in d:
            return no, value
        else:
            d[value] = target


def twoSums2(mylist, target):
    d = {}
    for index in mylist:
        no = target - index
        if no in d:
            return no, index
        else:
            d[index] = "test"


def twoSums3(nums, target):
    nodict = {}
    for i in range(len(nums)):
        no = target - nums[i]
        if no in nodict:
            return nodict[no], i
        else:
            nodict[nums[i]] = i

mylist = [2, 7, 11, 15]
print(twoSums3(mylist, 9))
