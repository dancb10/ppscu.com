

def reverse(array, k):
    section = array[0:k][::-1]
    return section + array[k:]


a = [5, 6, 7, 2, 4, 3, 8, 10]
k = 3
print(reverse(a, k))
