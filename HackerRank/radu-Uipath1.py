input

numbers = [3,4,5,2,4,5]
def method():
    a = set([x for x in numbers if numbers.count(x) > 1])
    return len(a)

print(method())
