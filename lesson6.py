#Наследование
class Person:
    def __init__(self,name,surname):
        self.name = name
        self.surname = surname

    def walk(self):
        return 'i can walk'


person1 = Person('Alex','Will')
print(person1.name,person1.surname)
person2 = Person(surname='Popov', name='Vladimir')
print(person2.name, person2.surname)
print(person2.walk())


class Developer(Person):
    def __init__(self, name, surname, language):
        super().__init__(name, surname)
        self.language = language

    def coding(self):
        return 'I am coding'

dev1 = Developer('Max','Korzh','Russian')
print(dev1.walk())
print(dev1.coding())


class Tester(Developer):
    def __init__(self,name, surname, language, test_framework):
        super().__init__(name,surname,language)
        self.test_framework = test_framework

    def testing(self):
        return 'i am testing'


tester1 = Tester('Azamat', 'Shakhiev', 'Russian', 'Selenium')
print(tester1.name, tester1.surname, tester1.test_framework)
print(tester1.walk(),tester1.testing())
print(isinstance(tester1,Tester)) # tester1 экземпляр класса Tester (подсущность сущности Tester)
print(issubclass(Tester,Developer)) # Tester подкласс класса Developer

#полиморфизм
class Employee:
    def __init__(self, name, lastname):
        self.name = name
        self.lastname = lastname

    def work(self):
        print('i am working')


employee1 = Employee('Ivan', 'Ivanov')
print(employee1.work())

class Engineer(Employee):
    def __init__(self, name, lastname, language):
        super().__init__(name, lastname)
        self.__language = language

    def work(self):
        print('i am Engineer')

    def get_language(self):
        return f'my language is {self.__language}'
    def set_language(self,new_language):
        self.__language = new_language

engineer1 = Engineer('Sergei','Sergeev','Russian')
print(engineer1.work())

#инкапсуляция
# print(engineer1.__language) #не будет работать потому что скрыто
print(engineer1.get_language())
engineer1.name = 'Aleksei' # изменение обычного атрибута
print(engineer1.name)

engineer1.language = 'Spanish' # создает новую переменную. не касаясь нашей старой
engineer1.__language = 'English' # создает новую переменную. не касаясь нашей старой
engineer1.set_language('French') # меняет нашу старую переменную
print(engineer1.language, engineer1.__language)
print(engineer1.get_language())