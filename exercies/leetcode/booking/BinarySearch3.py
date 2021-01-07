a = [3,5,4, 9 ,4 ,2, 10, 230, 8]

def deep_merge(a):
    if len(a) > 1:
        mid = len(a) // 2
        left = a[mid:]
        right = a[:mid]

        deep_merge(left)
        deep_merge(right)

        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                a[k] = left[i]
                i += 1
            else:
                a[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            a[k] = left[i]
            k += 1
            i += 1
        while j < len(right):
            a[k] = right[j]
            k += 1
            j += 1
        return a

def binary_search(a, x):
    low = 0
    high = len(a) - 1
    while low <= high:
        mid = (low + high) // 2
        if a[mid] == x:
            return x
        if a[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    return -1

b = deep_merge(a)
print(binary_search(b, 4))
