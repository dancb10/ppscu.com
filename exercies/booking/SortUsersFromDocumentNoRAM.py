# Sort the content of the a file based on second field, e.g.
"""
Input file:
Jervie,12,M
Jaimy,11,F
Tony,23,M
Janey,11,F
Output file:
Jaimy,11,F
Janey,11,F
Jervie,12,M
Tony,23,M
don’t worry about open file, close file etc
1Gb for memory but 4Gb for file
"""
import os


def get_file_size(myfile):
    size = os.path.getsize(myfile)
    return size // 4


def get_file_entries(myfile, start, size_limit):
    lines = []
    local_size = 0
    with open(myfile, 'r') as f:
        f.seek(start)
        for line in f:
            local_size += len(line.encode('utf-8'))
            if local_size <= size_limit:
                lines.append(line.rstrip().split(" "))
    return lines


def write_file_to_disk():
    pass


def merge_sort(lines):
    if len(lines) > 1:
        mid = len(lines) // 2
        left = lines[:mid]
        right = lines[mid:]

        merge_sort(left)
        merge_sort(right)

        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i][1] < right[j][1]:
                lines[k] = left[i]
                i += 1
                k += 1
            else:
                lines[k] = right[j]
                j += 1
                k += 1

        while i < len(left):
            lines[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            lines[k] = right[j]
            j += 1
            k += 1

    return lines



file_to_sort = "users.txt"
size = get_file_size(file_to_sort)
# for file in range(4):
#     entries = get_file_entries(file_to_sort, size)
#     print(merge_sort(entries))
print(get_file_entries(file_to_sort, 0, size))

