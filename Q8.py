def first_char(s):
    try:
        if len(s)>=10:
            print(s[:10:])
        else:
            raise ValueError("Oops! Too short string.")
    except ValueError as ex:
        print(ex)
s= input("Enter string:")
first_char(s)