letters_list = ['H', 'R', 'S']
numbers_list = [1, 2, 3]
new_list = []
for i in range(len(numbers_list)):
    for j in range(len(letters_list)):
        new_list.append(letters_list[j] + str(numbers_list[i]))
print(new_list)


