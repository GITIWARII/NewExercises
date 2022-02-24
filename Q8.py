list_1 = [1, 5, 8]
list_2 = [3, 2, 5]
list_3 = [2, 3, 6]
Resultant_list = []
for i,j,k in zip(list_1,list_2,list_3):
    Resultant_list.append(i+j+k)
print("Resultant_list:",Resultant_list)