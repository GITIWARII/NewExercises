num_list = [[2, 8, 11], [4, 5, 7, 12], [8, 9, 10, 11], [19, 13, 7], [2, 5, 16]]
d = {}
for i in num_list:
    d[str(i)] = sum(i)
maximum = max(zip(d.values(), d.keys()))[1]
minimum = min(zip(d.values(), d.keys()))[1]
print("The list with the maximum sum of elements:", maximum)
print("The list with the minimum sum of elements:", minimum)


