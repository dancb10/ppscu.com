def swaps(arr):
    noofswaps = 0
    for i in range(len(arr)):
        while arr[i] != i + 1:
            temp = arr[i]
            arr[i] = arr[arr[i] - 1]
            arr[temp - 1] = temp
            noofswaps += 1
    print(noofswaps)

arr = [1, 3, 5, 2, 4, 6, 7]
swaps(arr)
