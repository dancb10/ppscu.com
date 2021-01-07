# Given a text file containing the text for Hamlet (/usr/share/file.txt), return the top 5 most frequent words with count.

s = "Natural-language processing (NLP) is an area of computer science " \
    "and artificial intelligence concerned with the interactions " \
    "between computers and human (natural) languages."
from collections import Counter
import re

def process_text(string):
    text = re.sub("a-z-A-Z-0-9\w", ' ', string).split(" ")
    counter = Counter(text).most_common(5)
    return counter


print(process_text(s))
