stock_market = {'AXIS BANK' : 7,
                'BHARTI AIRTEL' : 5,
                'COAL INDIA' : 10,
                'ITC' : 1,
                'TCS' : 3,
                'L&T' : 2,
                'RELIANCE' : 9,
                'KOTAK BANK' : 8,
                'AMERICAN EXPRESS' : 11}
list_1 = list(stock_market.values())
list_2 = list(stock_market.keys())
print((min(list_1), list_2[list_1.index(min(list_1))]))
print((max(list_1), list_2[list_1.index(max(list_1))]))
sorted_stock = [(i, list_2[list_1.index(i)]) for i in sorted(list_1)]
print(sorted_stock)