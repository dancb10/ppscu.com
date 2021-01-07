def climbstairs(n):
    if n <= 0:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 2

    value_minus_one = 2
    value_minus_two = 1
    all_ways = 0
    for i in range(2, n):
        all_ways = value_minus_one + value_minus_two
        value_minus_two = value_minus_one
        value_minus_one = all_ways
    return all_ways


myinput = 4
print(climbstairs(myinput))
