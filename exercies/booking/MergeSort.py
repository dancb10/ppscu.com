# merge sort an array


def merge_sort(array):
    if len(array) > 1:
        mid = len(array) // 2
        left = array[:mid]
        right = array[mid:]

        merge_sort(left)
        print("left:" + str(left))
        merge_sort(right)
        print("right:" + str(right))

        i =j=k=0
        while i < len(left) and j < len(right):
            print("left deep:" + str(left))
            print("right deep:" + str(right))
            if left[i] < right[j]:
                array[k] = left[i]
                i += 1
            else:
                array[k] = right[j]
                j += 1
            print("array deep:" + str(array))
            print("k deep:" + str(k))
            k += 1
        while i < len(left):
            array[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            array[k] = right[j]
            j += 1
            k += 1
    return array

if __name__ == '__main__':
    arraya=[12, 11, 13, 5, 6, 7]
    print(merge_sort(arraya))
