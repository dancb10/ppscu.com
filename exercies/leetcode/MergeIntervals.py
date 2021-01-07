# class Interval(object):
#     def __init__(self, s, e):
#         self.start = s
#         self.end = e
#
# intervals = []
# a = Interval(2, 4)
# b = Interval(2, 5)
# c = Interval(5, 7)
# intervals.append(a)
# intervals.append(b)
# intervals.append(c)
#
# print(intervals)
#
#
# def merge(intervals_struct):
#     intervals = sorted(intervals_struct, key=lambda x: x.start)
#
#
#
# merge((intervals))


def merge(intervals):
    out = []
    for i in sorted(intervals, key=lambda start: start[0]):
        if out and i[0] <= out[-1][1]:
            out[-1][1] = max(out[-1][1], i[1])
        else:
            out.append(i)
    return out

a = [[1,4], [1,2], [2,5], [8, 12], [9, 10], [6,7]]
print(merge(a))
