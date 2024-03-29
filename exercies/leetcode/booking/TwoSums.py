# The two sum problem is a common interview question, and it is a variation of the subset sum problem. There is a popular dynamic programming solution for the subset sum problem, but for the two sum problem we can actually write an algorithm that runs in O(n) time. The challenge is to find all the pairs of two integers in an unsorted array that sum up to a given S.

#For example, if the array is [3, 5, 2, -4, 8, 11] and the sum is 7, your program should return [[11, -4], [2, 5]] because 11 + -4 = 7 and 2 + 5 = 7.

def two_sums(array, target):
    sums = []
    for index in range(len(array)):
        for index2 in range(index+1, len(array)):
            if array[index] + array[index2] == target:
                sums.append([array[index], array[index2]])
    return sums

def two_sums2(array, target):
    sums = []
    temp_sums = {}
    for index in range(len(array)):
        temp_sum = target - array[index]
        if temp_sum in temp_sums:
             sums.append([array[index], temp_sum])
        temp_sums[array[index]] = 1
    return sums


a = [3, 5, 2, -4, 8, 11]
target = 7
print(two_sums2(a, target))

