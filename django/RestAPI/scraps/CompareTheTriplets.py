#!/bin/python

import sys


def solve(a0, a1, a2, b0, b1, b2):
    n = int(len(locals()))
    for i in range(0, n / 2):
        for j in range(n / 2, n):
            if "a" + str(i) > "b" + str(j):
                print("yes")


# a0, a1, a2 = input().strip().split(' ')
# a0, a1, a2 = [int(a0), int(a1), int(a2)]
# b0, b1, b2 = input().strip().split(' ')
# b0, b1, b2 = [int(b0), int(b1), int(b2)]
a0 = 2
a1 = 3
a2 = 6
b0 = 3
b1 = 4
b2 = 7
result = solve(a0, a1, a2, b0, b1, b2)
print(" ".join(map(str, result)))
