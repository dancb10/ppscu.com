from collections import Counter
import re


def return_word_frequency(myfile):
    counters = Counter()
    with open(myfile, 'r') as f:
        for line in f:
            counters.update(re.split('\s', line))
    print(counters.most_common())


# return_word_frequency("text")

# lines = [line.rstrip('\n') for line in open('text')]

# with open("text", "r") as f:
#     for line in f.readline():
#         print(line)
#
# with open("text", "r") as f:
#     for line in f:
#         print(line)


b = "pula are mere. si mai are pere! sau cateodata, mancana cacat"
# counter = Counter()
# buf = ""
# for letter in b:
#     if letter.isalpha():
#         buf = buf + letter
#     else:
#         counter.update([buf])
#         buf = ""
# print(counter)

new_phrase = []
buf = []
for char in b:
    if char.isalpha():
        buf.append(char)
    else:
        new_phrase.append("".join(buf)[::-1])
        new_phrase.append(char)
        buf = []
new_phrase.append("".join(buf)[::-1])
print("".join(new_phrase))
