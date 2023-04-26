# todo:
#  Определите класс Person. В конструктор которого передается фамилия и возраст ('Иванов', 29)
#  Реализуйте через магические методы условие, при котором возраст у объекта не будет меняться после инициализации.


class Person:
    def __init__(self, name, age):
        self.name = name
        self.__dict__['age'] = age

    def __setattr__(self, key, value):
        if key != "age":
            super().__setattr__(key, value)


p = Person("Ivanov", 30)
print(p.age)

p.age = 40
print(p.age)
