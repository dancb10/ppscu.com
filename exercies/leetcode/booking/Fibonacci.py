# What a fibonacci function which return N th position number  both in recursive and loop, also give the explanation on both implementation on their time efficiency.

def fib_recursive(number):
    if number == 0:
        return 0
    if number == 1:
        return 1
    return fib_recursive(number-1) + fib_recursive(number-2)


def fib_interativ(number):
    a = 0
    b = 1
    nr = 0
    if number == 0:
        return 0
    if number == 1:
        return 1
    for i in range(1, number):
        nr = a + b
        a, b = b, b + a
    return nr


print(fib_recursive(25))
print(fib_interativ(25))
