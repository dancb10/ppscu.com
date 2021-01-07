import re
from collections import Counter


def chunk_read(f, chunksize):
    text = f.read(chunksize)
    c = ''
    c_list = []
    while c != ' ':
        c = f.read(1)
        if not c:
            break
        c_list.append(c)
    text += ''.join(c_list)
    return text

def process_text(text):
    match = re.findall('\w+', text)
    d = Counter(match)
    return d

def merge_dicts(d1, d2):
    for key in d2.keys():
        if key in d1:
            d1[key] = d1[key] + d2[key]
        else:
            d1[key] = d2[key]

def read_from_file(filename, chunksize=1024):
    per_file_dict = {}
    with open(filename) as f:
        text = chunk_read(f, chunksize)
        d = process_text(text)
        merge_dicts(per_file_dict, d)
    return per_file_dict

print(read_from_file("input.txt"))
