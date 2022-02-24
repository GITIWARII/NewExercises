map_details = {101:'Park', 102:'Zoo', 103:'Mall'}

def find(details):
    for key,value in details.items():
        if value=='Mall':
            print(key)
find(map_details)
