# Given a string of characters, find the maximum substring with no repetitions

def max_substring(string):
    length = len(string)
    global_max = str()
    max_so_far = str()
    for i in range(length-1):
        for j in range(i, length-1):
            if string[j] not in max_so_far:
                max_so_far = max_so_far+string[j]
                if len(max_so_far) > len(global_max):
                    global_max = max_so_far
            else:
                max_so_far = str()
                break
    return len(global_max) if global_max else len(" ")

a = "ABDEFGABEF"
b = "BBB"
c = "pwwkew"
# c = " "
print(max_substring(a))
print(max_substring(b))
print(max_substring(c))


# def lengthOfLongestSubstring(self, s: str) -> int:
#     max_len = i = j = 0
#     hash_set = {}
#
#     while j < len(s):
#         if not hash_set.get(s[j]):
#             hash_set[s[j]] = hash_set.get(s[j], 1)
#             j += 1
#             max_len = max(max_len, len(hash_set))
#         else:
#             hash_set.pop(s[i])
#             i += 1
#
#     return max_len
