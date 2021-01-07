# Given any number of arrays containing numbers, write a  function which finds the numbers that appear in exactly two arrays.
# arrays = [ [6, 2, 2, 0, 4], [5, 0, 2, 6, 7, 1], [6, 7, 9, 9], ] find_in_two(arrays) should return [2, 0, 7]
from collections import Counter
arrays = [[6, 2, 2, 0, 4], [5, 0, 2, 6, 7, 1], [6, 7, 9, 9]]

def find_in_two(arrays):
    global_counter = Counter()
    returned_values = []
    for array in arrays:
        global_counter = global_counter + Counter(set(array))
    for key, value in global_counter.items():
        if value == 2:
            returned_values.append(key)
    return returned_values

print(find_in_two(arrays))
