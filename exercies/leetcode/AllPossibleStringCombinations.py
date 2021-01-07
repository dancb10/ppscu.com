#HackerRank: Given a string of lowercase unique characters  (e.g. "ab", "lmne") sort the string alphabetically and then find all possible combinations, ignoring ordering. e.g. "ab" -> "a", "b", "ab

word = "abc"

def comb(w, n, rez = []):
    if len(rez) == n:
        return rez
    rez.append(w[0])
    comb(w[1:], n, rez)
    rez.pop()


for i in range(len(word)):
    print(comb(word, i, []))

# a=[]
# a.sort()
