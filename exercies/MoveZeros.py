def move_zeros(nums):
    i = 0
    j = 0
    n = len(nums)
    while j < n:
        if nums[j] == 0:
           j += 1
        else:
           nums[i] = nums[j]
           i += 1
           j += 1
    while i < n:
        nums[i] = 0
        i += 1


input = [0,1,0,3,12]
move_zeros(input)
