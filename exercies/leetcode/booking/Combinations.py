# abc
# ['a', 'ab', 'abc', 'ac', 'b', 'bc', 'c']

results = []

def combineString(string, index, cur_s):
    for i in range(index, len(string)):
        new_s = cur_s + string[i]
        results.append(new_s)
        combineString(string, i + 1, new_s)


r = []
def combinationns(string, index, reminder):
    for i in range(index, len(string)):
        new_string = reminder + string[i]
        r.append(new_string)
        combinationns(string, i+1, new_string)

# combineString("abc", 0, "")
combinationns("abc", 0, "")
print(r)
