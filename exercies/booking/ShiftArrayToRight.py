# shift an array to the right by n positions such that the right most indexes are become the first ones and the first ones move ahead.
#like:
# 1 2 3 4 5 --> shift by 2 --> 4 5 1 2 3


def rotate_left(array, d):
    index = 0
    while index <= d:
        array.append(array.pop(0))
        index += 1
    return array


def rotate_right(array, d):
    index = 0
    while index <= d:
        array = [array.pop()] + array
        index += 1
    return array

l = [1, 2, 3, 4, 5]
print(rotate_left(l, 2))
l = [1, 2, 3, 4, 5]
print(rotate_right(l, 2))
