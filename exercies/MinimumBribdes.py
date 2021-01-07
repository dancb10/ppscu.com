def minimumBribes(q):
    moves = 0
    k = False
    for pos, val in enumerate(q):
        if (val-1) - pos > 2:
            k = True
        else:
            for j in range(max(0, val-2), pos):
                if q[j] > val:
                    moves += 1
    if k:
        print("Too chaotic")
    else:
        print(moves)


# original
# l = [1, 2, 3, 4, 5]
l = [2, 1, 5, 3, 4]
# l = [1,2,5,3,7,8,6,4]
# l = [5,1,2,3,7,8,6,4]
# l = [1,2,5,3,7,8,6,4]
minimumBribes(l)
