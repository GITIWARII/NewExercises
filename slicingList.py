num_list = [31, 24, 2, 16, 19, 45, 75, 63, 79]
p = 1
i = 0
while i>=0 and i<len(num_list):
    print("Sub-List", p, list(num_list[i:i+3]))
    p += 1
    i += 3
