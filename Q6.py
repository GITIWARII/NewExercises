candidate_details = [('Harry', 168), ('Jhonny', 160), ('Brad', 178), ('Chris', 172)]
def sort(details):
    sorted_details = sorted(details , key = lambda i:i[1])
    print(sorted_details)
sort(candidate_details)
