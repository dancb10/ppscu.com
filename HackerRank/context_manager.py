import re
from collections import Counter
a=["abc", "aac", "ldam", "eqwa", "adwz"]
mca = list()
result = sorted([x[::-1] for x in a])


mycounter = Counter
def myfunct():
    with open("input.txt") as f:
        line = f.readline()
        words = re.findall("\w+", line)
        d = mycounter(words)
        return d

caca = dict(myfunct())

# print(caca)
#
# print(dict(caca.most_common(1)))
# for x, y in caca.elements():
#     print(x,y)

for key, value in caca.items():
    print("Key: " + key + " ; " + "Value: " + str(value))
