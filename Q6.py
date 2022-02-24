import datetime
given_date = datetime.datetime(2010, 6, 12)
try:
    if type(given_date.year) == int and type(given_date.month) == int and type(given_date.day) == int:
        print(given_date.strftime("%A"))
    else:
        raise ValueError('Oops! An error occurred.')
except ValueErro as ex:
    print(ex)