def factorial(n):
    '''
    This function returns factorial of n
    testing
    '''
    x = 1 if n < 2 else n * factorial(n-1)
    factorial.c = x
    return x

print(factorial(20))
print(factorial(21))
print(factorial.c)

# print(factorial.__doc__)
# print(type(factorial))

# fact = factorial
# print(fact(5))
# print(list(map(factorial, range(10))))


# l1 = [1, 2, 3, ['dd', 1, 5, ['aa', 1, 'bb'], 5], 7, 'a']
#
#
# def s1(l11, l12):
#     for x in l11:
#         if type(x) is not list:
#             l12.append(x)
#         else:
#             s1(x, l12)
#
#
# def s2(l11):
#     for x in l11:
#         if type(x) is not list:
#             yield x
#         else:
#             yield from s2(x)
#             # for y in s2(x):
#             #     yield y
#
# l2 = []
# s1(l1, l2)
# print(l2)
#
# print(list(s2(l1)))
#
# print(type(s2(l1)))
