# map, lambda
# my_list = [20,-3,15,2,-1,-21]
# l = list(map(lambda x: x*x,my_list))
# print(l)

#шифр цезаря
# abc = 'abcdefghijklmnopqrstuvwxyzabcdefgh'
# s = 'hello'
# plan = ''
# for i in s:
#   plan+=''.join(abc[abc.index(i)+13])
# print(plan)

#сложить числа
# list_1 = ['Hi','ananas',2,None,75,'pizza',36,100]
# def filter_and_sum(l):
#   new_l = []
#   for i in l:
#     if isinstance(i,int):
#       new_l.append(i)
#   return sum(new_l)
# print(filter_and_sum(list_1))
# print(sum(filter(lambda x: isinstance(x,int),list_1)))

#вывести четные числа
# list_1 = ['Hi','ananas',2,None,75,'pizza',36,100]
# def take_add(num):
#   if isinstance(num,int) and num%2==0:
#     return True
#   return False
# print(list(filter(take_add,list_1)))


# from Lesson_10_my_file import *
#
# def test(a,b):
#     assert sum_it(a,b) == 25, f'Test of sum failed. Actual result is {sum_it(a,b)}'
#     assert prod(a,b) == 100, f'Test test of prod failed. Actual result is {sum_it(a,b)}'
#     assert div(a, b) == 4, f'Test test of div failed. Actual result is {sum_it(a, b)}'
#
# test(20,5)
# print(div(4,2))
#
# #встроенные функции
# import math
# arr = [1,2,3,4,5]
# new_arr = math.prod(arr)
# print(new_arr)
#
# import datetime
# birth_date = 1990
# current_date = datetime.date.today()
# print(current_date)
# current_age = current_date.year - birth_date
# print(current_age)
# current_month = current_date.month
# print(current_month)

#**args
# def sum_it(*args):
#     result = 0
#     for i in args:
#         result += i
#     return(result)
# print(sum_it(1,2,3,4))

#**kwargs
# def sum_it(**kwargs):
#     result = 0
#     for i in kwargs.values():
#         result+=i
#     return result
# print(sum_it(num1=1,num2=2,num3=3))

#dz - 1
# import math
# def square(a):
#     p = a*4
#     s = a*a
#     d = math.sqrt(a*a+a*a)
#     return (p,s,d)
# print(square(4))

# dz-2
# d = input('Введите ключ : значение:')
# s = 'name:Azamat,lastname:Shakhiev,age:32'
# l = s.split(',')
# def printing(**kwargs):
#     return kwargs.items()
#
# for i in l:
#     m = i.split(':')
#     printing()

# dz-3
