num_1 = {'a': 5, 's': 7, 'x' : 11, 'm' : 12, 'o' : 8}
num_2 = {'r': 12, 'x': 9, 'n' : 8, 'm' : 12, 'q' : 10}
set_1 = set(num_1.keys())
set_2 = set(num_2.keys())
print("1.", set_1 & set_2)
out = {(key, value) for key, value in num_1.items() if key in num_2 and num_2[key] == value}
print("2.", out)
print("3.", set_1 ^ set_2)
print("4.", set_1 - set_2)
num_3 = {key:value for key, value in num_1.items() if key not in num_2}
print("5.",num_3)

