def jumpingOnClouds(c):
    steps = 0
    index = 0
    while index < n1:
        print("index: " + str(index))
        print("steps: " + str(steps))
        if (index + 2 < n1) and (c[index+2] == 0):
            index += 2
            steps += 1
        else:
            index += 1
            steps += 1

    return steps-1

# n = 7
# l = [0,0,1,0,0,1,0]

n1 = 6
l1 = [0, 0, 0, 1,0, 0]

# print(jumpingOnClouds(l))
print(jumpingOnClouds(l1))
