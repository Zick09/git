def sum_it(a,b):
    return a+b

def prod(a,b):
    return a*b

def div(a,b):
    try:
        return a/b
    except ZeroDivisionError:
        print('На ноль делить нельзя')