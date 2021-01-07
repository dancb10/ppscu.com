list = ["a","b","c","b","d","a"]
a = set(list)
list2 = ["a","b"]
b = set(list2)
# print(len(a-b))
# print("List converted to set:" +str(a))
# print(a&b)
# print(a-b)

d = set()
# print(type(d))

d = frozenset()
# print(hash(d))

from dis import dis
print(dis('{1}'))


print(dis("set(['a'])"))

e = frozenset(['a','b','c'])
print(e)

print(a.isdisjoint(d))
