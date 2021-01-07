# [[1, 1, 1, 0, 0, 0], [0, 1, 0, 0, 0, 0], [1, 1, 1, 0, 0, 0], [0, 0, 2, 4, 4, 0], [0, 0, 0, 2, 0, 0], [0, 0, 1, 2, 4, 0]]
# Complete the hourglassSum function below.
# def hourglassSum(arr):
#     last_sum = -math.inf
#     for i in range(4):
#         for j in range(4):
#             hourglass = arr[i][j] + arr[i][j+1] + arr[i][j+2] + arr[i+1][j+1] + arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2]
#             if hourglass > last_sum:
#                 last_sum = hourglass
#     print(last_sum)
#
# arr = [[1, 1, 1, 0, 0, 0], [0, 1, 0, 0, 0, 0], [1, 1, 1, 0, 0, 0], [0, 0, 2, 4, 4, 0], [0, 0, 0, 2, 0, 0], [0, 0, 1, 2, 4, 0]]
#
# hourglassSum(arr)

l=[1,2,3,4,5]
n=3

def rotLeft(a, d):
    index=0
    while index < d:
        a.append(a.pop(0))
        index += 1
    return a

def rotRight(a, d):
    index=0
    while index < d:
        a = [a.pop()] + a
        index += 1
    return a


# print(rotLeft(l,n))
print(rotRight(l,n))

