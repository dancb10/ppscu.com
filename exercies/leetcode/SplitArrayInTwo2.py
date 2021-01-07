a = [2, 4, -2, 5, 5, -5, 9]

def split_array(a):
    index_left = 0
    index_right = len(a) - 1
    sum_left, sum_right = 0, 0
    while index_left <= index_right:
        if sum_left < sum_right:
            sum_left += a[index_left+1]
        else:
            sum_right += a[index_right-1]

        index_left += 1
        index_right -= 1
    print(sum_left)
    print(sum_right)
    if sum_left == sum_right:
        return True
    else:
        return False


print(split_array(a))
