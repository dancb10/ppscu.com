a = [2, 4, -2, 5, 5, -5, 9]


def splitAraryCheckSum(array):
    begin = 0
    end = len(a)-1
    sum_front = 0
    sum_back = 0
    i = 0
    while begin <= end:
        if sum_front < sum_back:
            sum_front += array[begin+1]
        else:
            sum_back += array[end-1]
        print("step " + str(i))
        print("front sum " + str(sum_front) + " index is " + str(begin))
        print("back sum " + str(sum_back) + " index is " + str(end))
        print("\n")
        begin += 1
        end -= 1
        i += 1

    print(sum_back)
    if sum_front == sum_back:
        print(True)
    else:
        print(False)

print(splitAraryCheckSum(a))
