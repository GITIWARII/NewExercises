grocery_items = ' Grated Cheese, Coffee Powder, Pickles White Chocolate, Dark Chocolate, Eggs, Breads, Milk,Sugar, Salt, Cat Food, Fries'
s = ''
new_list = sorted(grocery_items.split(','))

for i in new_list:
    s = s + i +  ','
print(s.rstrip(','))
