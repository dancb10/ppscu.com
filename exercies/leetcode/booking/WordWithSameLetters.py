#Call a function F in a loop. F returns a string of  140 chars.
# Write to the output 1 when F returns a string with the same letters (basically a permutation) of a string previously returned.
# (the question was not this well formed)
import hashlib


def check_word(word):
    sorted_word = str(sorted(word))
    local_hash = hashlib.sha1(sorted_word.encode('utf-8')).hexdigest()
    if local_hash in words:
        return 1
    else:
        words[local_hash] = 0
    return 0

words = dict()
print(check_word("caca"))
print(words)
print(check_word("acac"))
print(words)
print(check_word("test"))
print(words)
print(check_word("estt"))
print(words)
