class InvalidNumError(Exception):
    def __init__(self,args):
        super().__init__(args)
try:
    n=int(input("Enter marks:"))
    if n<0 or n>100:
        raise InvalidNumError("Error! Try again.")
    else:
        print("'Results processing.'")
except InvalidNumError as ex:
    print(ex)