# todo: Создать абстрактный класс Press (пресса) содержащий:
# Поля: название, цена за единицу.
# В классе должны быть абстрактные методы:
# метод SetPrice (без параметров) – установка цены.
# Метод Info - информация (без параметров), который возвращает строку, содержащую информацию об объекте.
#
# На его основе реализовать дочерние классы:
# Magazine - журнал,
# Book- книга.


from abc import ABC, abstractmethod


class Press(ABC):
    __name: None
    __unit_price: 0

    @abstractmethod
    def SetPrice(self):
        pass

    @abstractmethod
    def Info(self):
        return "No description"


class Magazine(Press):
    def __init__(self, name):
        self.__name = name

    def SetPrice(self):
        self.__unit_price = 100

    def Info(self):
        return f"Magazine \"{self.__name}\", price: {self.__unit_price}"


class Book(Press):
    def __init__(self, name):
        self.__name = name

    def SetPrice(self):
        self.__unit_price = 500

    def Info(self):
        return f"Book \"{self.__name}\", price: {self.__unit_price}"


magazine = Magazine("Space")
magazine.SetPrice()
print(magazine.Info())

book = Book("Science and technology")
book.SetPrice()
print(book.Info())
