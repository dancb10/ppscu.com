

def inverse_interval(i, j, nums):
    while i <= j:
        nums[i], nums[j] = nums[j], nums[i]
        i += 1
        j -= 1
    print(nums)




i=3
j=8

mylist = [2, 6, 1, 45, 12, 8, 31, 19, 6, 15, 20]
inverse_interval(i, j, mylist)
