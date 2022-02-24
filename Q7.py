def reverse(s):
    try:
        if len(s)%2==0:
            print(s[::-1])
        else:
            raise Exception("Something went wrong.")
    except TypeError:
        print("Check the string.")
    except Exception as ex:
        print(ex)
reverse('gaurav')