# import itertools
#
#
# def func(string):
#     char_list = sorted(list(string))
#     combs = []
#     for i in range(1, len(char_list) + 1):
#         for x in itertools.combinations(char_list, i):
#             combs.append(x)
#     return combs

r = []


# def comb(string, index, reminder):
#     for i in range(index, len(string)):
#         current_string = reminder + string[i]
#         r.append(current_string)
#         comb(string, i + 1, current_string)
#
# a = "abc"
# comb(a, 0, "")
# print(r)

def combinations_of_k(string, index, reminder, k):
    for i in range(index, len(string)):
        current_string = reminder + string[i]
        if len(current_string) == k:
            r.append(current_string)
        combinations_of_k(string, i + 1, current_string, k)

a = "abc"
combinations_of_k(a, 0, "", 2)
print(r)

# import itertools
#
# def combinations(string):
#     for x in range(len(string)):
#         for com in itertools.combinations(string, x):
#             r.append(com)
#
# a = "abc"
# combinations(a)
# print(r)
