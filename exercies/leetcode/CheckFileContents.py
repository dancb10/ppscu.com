from collections import Counter
import hashlib
import os


def calculate_hash(file):
    with open(file, 'r') as f:
        content = f.read()
        hash = hashlib.sha256(content.encode(encoding='UTF-8')).hexdigest()
        print(hash)
    return hash


def check_files(files_list):
    counter = Counter()
    for file in files_list:
        file_hash = calculate_hash(file)
        counter.update([file_hash])
    return counter


def check_files2(files_list):
    files_checked = {}
    for file in files_list:
        file_hash = calculate_hash(file)
        if file_hash in files_checked:
            files_checked[file_hash].append(file)
        else:
            files_checked[file_hash] = [file]
    return files_checked

files = ['test/f1', 'test/f2', 'test/f3']
# print(check_files(files).most_common())
# print(check_files2(files))

d = 'test'
# def get_files(directory):
#     full_path_files = []
#     for root, dirs, files in os.walk(directory):
#         for file in


file_tree = []


def traverse_dir_recur(origin):
    dir = os.listdir(origin)
    for file_type in dir:
        dir_path = os.path.join(origin, file_type)
        if os.path.isdir(dir_path):
            traverse_dir_recur(dir_path)
        else:
            file_tree.append(dir_path)


traverse_dir_recur('test')
print(file_tree)
