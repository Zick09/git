def sum_args(arr1,arr2):
    return sum(arr1+arr2)

def sum_args2(arr1,arr2):
    result = 0
    for i in arr1:
        result+=i
    for i in arr2:
        result+=i
    return result

from functools import reduce
def sum_args3(arr1,arr2):
    return reduce(lambda x,y: x+y, arr1+arr2)