def rob(nums):
    max_sum = 0
    i = 0
    while i < len(nums)-3:
        if nums[i]+nums[i+2] > nums[i+1]+nums[i+3]:
            max_sum += nums[i]+nums[i+2]
            i +=2
        else:
            max_sum += nums[i+1]+nums[i+3]
            i +=3
        print(max_sum)
    return max_sum


mylist = [2,7,9,3,1]
print(rob(mylist))
