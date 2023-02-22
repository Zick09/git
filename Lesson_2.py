# a = 3.45
# print(a, '|type = ', type(a))
#
# b = str(a)
# print(f'+++{b*2}+++')
#
# c = 'Don\'t touch anything'
# print (c)
#
# d = 3
# print(bool(d))
#
# e = input('User name: ')
# n = int(input('Age: '))
# print('User name = ' + e)
# print('Age = ' +str(n))
# print(f'User name = {e}\nAge = {str(n)} ')
# print(input('Digit and string: '))

# m = input('Input digit or string: ')
# print(m)
# print(m.isdigit()) - все цифры?
# print(m.isalpha()) - все буквы?
# print(m.capitalize()) - преобразовать первую с заглавной буквы
# print(m.upper()) - преобразовать все в заглавные буквы
# print(m.isupper()) - все заглавные буквы?
# ------HOMEWORK--------
user_name = input('User name: ')
age = int(input('Age: '))
date_of_birth = 2023 - age
print(f'User name: {user_name} \nAge: {age}\nDate of birth: {date_of_birth}')