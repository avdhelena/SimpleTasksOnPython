#todo:
# Определите класс Person. При создании объекта p=Person(‘Иванов’, ‘Михаил’, ‘Федорович’) необходимо ввести полное имя человека.
# При печати объекта должно выводиться следующее:
# print(p) # чивородеФлиахиМвонавИ

class Person:
    def __init__(self, surname, name, patronymic):
        self.surname = surname
        self.name = name
        self.patronymic = patronymic

    def __str__(self):
        return self.patronymic[::-1] + self.name[::-1] + self.surname[::-1]   #''.join(reversed(self.surname))


p = Person('Иванов', 'Михаил', 'Федорович')
print(p)
print(p.surname)
print(p.name)
print(p.patronymic)

