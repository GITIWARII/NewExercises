list_1 = [5, 10, 15, 20, 25, 30, 35]
list_2 = [7, 14, 21, 28, 35, 42, 49]
list_3 = []
list_3.extend(list_1[1::2])
list_3.extend(list_2[0::2])
print(list_3)