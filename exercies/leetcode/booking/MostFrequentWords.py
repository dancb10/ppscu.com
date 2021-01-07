from collections import Counter

text = "text"

def get_words(text):
    words = []
    with open(text, 'r') as f:
        for word in f:
            words.extend(word.rstrip().split(" "))
    return words

def count_words(words, no):
    counter = {}
    for word in words:
        if word in counter:
            counter[word] = counter[word] + 1
        else:
            counter[word] = 1

    # words = sorted(counter.items(), key=lambda x: (x[1], x[0]), reverse=True)
    words = merge_sort(list(counter.items()))
    return words[:no]

def merge_sort(words):
    if len(words) > 1:

        mid = len(words) // 2
        left = words[:mid]
        right = words[mid:]

        merge_sort(left)
        merge_sort(right)

        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i][1] > right[j][1]:
                words[k] = left[i]
                i += 1
            else:
                words[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            words[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            words[k] = right[j]
            j += 1
            k += 1
        return words




def count_words2(words, no):
    counter = Counter(words)
    return counter.most_common(no)


# print(count_words2(get_words(text), 5))
print(count_words(get_words(text), 5))
