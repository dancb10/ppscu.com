#Given a stream of characters and a list of words find and display count of each and every word once the stream ends.
#Input: stream = "acacabcatghhellomvnsdb", words = ["aca","cat","hello","world"]
#Output : ["aca" : 2 , "cat" : 1 , "hello" : 1 , "world" : 0]

from collections import Counter
stream = "acacabcatghhellomvnsdb"
words = ["aca","cat","hello","world"]
word_counter = Counter()

# def count_word(streamz, word):
#     word_c = list(word)
#     counter = 0
#     word_index = 0
#     for _, value in enumerate(streamz):
#         if value == word_c[word_index]:
#             if word_index == len(word_c)-1:
#                 counter += 1
#                 word_index = 0
#             else:
#                 word_index += 1
#     return counter

def count_word(streamz, word):
    word_c = list(word)
    word_index = 0
    counter = 0
    for poz, value in enumerate(streamz):
        if value == word[word_index]:
            if word_index == len(word_c) - 1:
                counter += 1
                word_index = 0
            else:
                word_index += 1
    return counter


def process_words(stream, words):
    for word in words:
        word_counter[word] = count_word(stream, word)
    print(str(word_counter))

# count_word("acacabcatghhellomvnsdb", "world")
process_words(stream, words)
