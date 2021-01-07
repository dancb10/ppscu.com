




# results = []
# def permute(a, l, r):
#     if l == r:
#         results.append(a)
#     else:
#         for i in range(l, r + 1):
#             a[l], a[i] = a[i], a[l]
#             print(a[l], a[i])
#             permute(a, l + 1, r)
#             a[l], a[i] = a[i], a[l]  # backtrack
#
#
# # Driver program to test the above function
# string = "ABC"
# n = len(string)
# a = list(string)
# permute(a, 0, n - 1)

# import itertools
# print(list(itertools.permutations(["A","B", "C"])))
def permutate_string(string, prefix=''):
    if len(string) == 0:
        print(prefix)
    else:
        for i in range(len(string)):
            rem = string[0:i] + string[i + 1:]
            permutate_string(rem, prefix + string[i])

permutate_string('abc')