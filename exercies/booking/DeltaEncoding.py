# xGiven a list of numbers, e.g.:

#25626 25757 24367 24267 16 100 2 7277
#Output a delta encoding for the sequence. In a delta encoding, the first element is reproduced as is. Each subsequent element is represented as the numeric difference from the element before it. E.g. for the sequence above, the delta encoding would be:

#25626 131 -1390 -100 -24251 84 -98

a = [25626, 25757, 24367, 24267, 16, 100, 2, 7277]


def delta_encoding(numbers):
    results = [numbers[0]]
    for index in range(1, len(numbers)):
        previous = numbers[index-1]
        current = numbers[index]
        results.append(current - previous)
    return results


print(delta_encoding(a))
