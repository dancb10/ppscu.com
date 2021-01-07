# If you are given 2 array A={3,1,2,4} B={1,4}. Write a program to compare
# two arrays and create another array which holds the common values between two array!


def common_values(arraya: [int], arrayb: [int]):
    return set(arraya).intersection(set(arrayb))


arraya = [3, 1, 2, 4]
arrayb = [1, 4]
print(common_values(arraya, arrayb))
