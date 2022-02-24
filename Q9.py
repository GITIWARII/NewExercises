def sqr():
    try:
        n =int(input("Enter a number:"))
        print(n**2)
    except Exception as ex:
        print("Enter a valid input")
        sqr()
sqr()