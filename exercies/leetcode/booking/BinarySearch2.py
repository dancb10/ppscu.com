a = [4, 6, 7, 32, 54, 66, 84, 99]

def binary_search(a, x):
    low = 0
    high = len(a) - 1
    while low <= high:

        mid = (low + high) // 2
        if a[mid] == x:
            return a[mid]
        if a[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    return -1

print(binary_search(a, 7))
