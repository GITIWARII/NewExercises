countries = ['Austraiia', 'India', 'Austria', 'America', 'Russia', 'Iran']
def check(country):
    new_list=[]
    for i in country:
        if i[0]=='A' or i[0]=='a':
            new_list.append(i)
    print(new_list)
check(countries)