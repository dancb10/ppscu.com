def swaps(arr):
    noofswaps = 0
    for i in range(len(arr)):
        while arr[i] != i + 1:
            temp = arr[i]
            arr[i] = arr[arr[i] - 1]
            arr[temp - 1] = temp
            noofswaps += 1
    print(noofswaps)
    print(arr)

# arr = [1, 3, 5, 2, 4, 6, 7]
# swaps(arr)



arr = [1, 3, 5, 2, 4, 6, 7]

def swap(arr):
    results = 0
    for i in range(len(arr)):
        while arr[i] != i + 1:
            temp = arr[i]
            arr[i] = arr[arr[i] - 1]
            arr[temp - 1] = temp
            print(arr)
            results += 1

swap(arr)
