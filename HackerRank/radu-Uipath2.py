def move(a, i, j):
    a[i], a[j] = a[j], a[i]


def moves(a):
    count = 0
    length = len(a)
    even = 0
    odd = length - 1

    while (even < odd):
        while a[even] % 2 == 0:
            even += 1
        while a[odd] % 2 == 1:
            odd -= 1
        if even < odd:
            move(a, even, odd)
            count += 1

    return count

numbers = [13, 10, 21, 20]
print(moves(numbers))
