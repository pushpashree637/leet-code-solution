intervals = [[4,7],[1,4]]
for i in range(len(intervals)):
    for j in range(i+1, len(intervals)):
        if intervals[i][0] > intervals[j][0]:
            intervals[i], intervals[j] = intervals[j], intervals[i]
result = [intervals[0]]
for i in range(1, len(intervals)):
    last = result[-1]
    if intervals[i][0] <= last[1]:
        last[1] = max(last[1], intervals[i][1])
    else:
        result.append(intervals[i])
print(result)
