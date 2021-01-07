
def get_substring(string):
    max_substring = ""
    buffer = ""
    i = 0
    j = 0
    if len(string) == 1:
        return 1
    while i < len(string) and j < len(string):
        if string[i] not in buffer:
            buffer = buffer + string[i]
            i += 1
        else:
            if len(max_substring) < len(buffer):
                max_substring = buffer
                buffer = ""
            j += 1
            i=j

    return len(max_substring)


# print(get_substring("ABDEFGABEF"))
# print(get_substring("BBB"))
# print(get_substring("pwwkew"))
print(get_substring(" "))
