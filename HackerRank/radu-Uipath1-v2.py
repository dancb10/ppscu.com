from array import array

N = 1000

def countDuplicates(numbers):
    aux = array('I', [0] * N)

    for number in numbers:
        aux[number] += 1
    sum = 0
    for elem in aux:
        if aux[elem] > 1:
            sum += 1
    return sum


numbers = [1, 2, 1, 3, 3, 3, 4, 5, 3, 4]
print(countDuplicates(numbers))
