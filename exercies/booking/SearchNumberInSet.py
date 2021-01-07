# You have a long set of numbers. More than 400k. How would you search if a specific number is in set? They expect a better solution than looping the set until you find the number.

a = [4, 6, 7, 32, 54, 66, 84, 99]

def binarySearch(array, x):
    low = 0
    high = len(array) - 1

    while low <= high:
        mid = (low + high) // 2

        if array[mid] == x:
            return mid
        if array[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    return -1

print(binarySearch(a, 84))
