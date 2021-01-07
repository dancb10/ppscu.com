#http://www.albertauyeung.com/post/generating-ngrams-python/
import re
s = "Natural-language processing (NLP) is an area of computer science " \
    "and artificial intelligence concerned with the interactions " \
    "between computers and human (natural) languages."


def generate_ngrams(text, length):
    text = re.sub("a-z-A-Z-0-9\w", ' ', text).split(" ")
    i = 0
    ngrams = []
    while i <= len(text)-length:
        ngrams.append(text[i:i+length])
        i += 1
    return ngrams


print(generate_ngrams(s, 5))
