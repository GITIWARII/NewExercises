passenger_list = {'Ross' : 35,
'Thomas': 42,
'Rick' : 55,
'Ericson' : 51,
 'Josh' : 45,
'Lara' : 50,
'Emma' : 38,
'Lily' : 46,
'Ron' : 41,
 'Michael' : 47,
'Joanna' : 56,
 'Arthur' : 42}
list_1 = list(passenger_list.keys())
list_2 = list(passenger_list.values())
resultant = {list_1[i] for i in range(len(list_1)) if list_2[i]> 45}
print(resultant)

