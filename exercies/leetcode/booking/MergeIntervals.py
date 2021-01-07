#Given a list of intervals, e.g. [1,4], [2,5], [6,7], merge overlapping intervals, e.g. [1,5],[6,7].
# booking

# [0 lowEnd, 1 highEnd]

def merge_intervals(intervals):
    merged_intervals = []
    for interval in sorted(intervals):
        if merged_intervals and interval[0] <= merged_intervals[-1][1]:
            merged_intervals[-1][1] = max(interval[1], merged_intervals[-1][1])
        else:
            merged_intervals.append(interval)
    return merged_intervals


a = [[1, 4], [1, 2], [2, 5], [8, 12], [9, 10], [6, 7]]
print(merge_intervals(a))
