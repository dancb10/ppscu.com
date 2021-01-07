def test(n):
    num = 0
    while num < n:
        yield num
        num += 1
numbers = test(300)
for i in numbers:
    print(i,)

