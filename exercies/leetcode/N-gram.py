#http://www.albertauyeung.com/post/generating-ngrams-python/
import re


def generate_ngrams(s, n):
    s = s.lower()
    s = re.sub('[^a-zA-Z0-9\s]', ' ', s)
    tokens = [token for token in s.split(' ') if token != ""]

    i = 0
    j = n
    ngrams = []
    while j <= len(tokens):
        ngrams.append(tuple(tokens[i:j]))
        i += 1
        j += 1
    return ngrams


sentence = "Naturaal-language processing (NLP) is an area of computer science " \
    "and artificial intelligence concerned with the interactions " \
    "between computers and human (natural) languages."

ngrams = generate_ngrams(sentence, 2)
for ngram in ngrams:
    print(ngrams)

