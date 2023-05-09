#todo: Создать абстрактный класс Transport (транспорт) содержащий:
# Поля:
# скорость;
# себестоимость перевозки груза;
# стоимость перевозки груза.
# В классе должны быть абстрактные методы:
# метод Cost (без параметров) – вычисление стоимости перевозки груза.
# Метод Info - информация (без параметров), который возвращает строку, содержащую информацию об объекте.
#
# На его основе реализовать дочерние классы:
# Marine - морской транспорт,
# Ground - наземный транспорт.

from abc import *


class Transport(ABC):
    Speed: None
    TransportCost: None
    FullCost: None

    @abstractmethod
    def info(self):
        pass

    @abstractmethod
    def cost(self):
        pass


class MarineTransport(Transport):
    "Морской транспорт"
    def __init__(self, transport_cost, full_cost, speed):
        self.TransportCost = transport_cost
        self.FullCost = full_cost
        self.Speed = speed

    def info(self):
        print(f"Транспорт: \t{self.name()},\tскорость: \t{self.Speed} км/ч,\tстоимость: \t{self.cost()} ₽,\tсебестоимость: \t{self.TransportCost} ₽")

    def cost(self):
        return self.FullCost

    def name(self):
        return "Морской"


class GroundTransport(Transport):
    "Наземный транспорт"

    def __init__(self, transport_cost, full_cost, speed):
        self.TransportCost = transport_cost
        self.FullCost = full_cost
        self.Speed = speed

    def info(self):
        print(f"Транспорт: \t{self.name()},\tскорость: \t{self.Speed} км/ч,\tстоимость: \t{self.cost()} ₽,\tсебестоимость: \t{self.TransportCost} ₽")

    def cost(self):
        return self.FullCost

    def name(self):
        return "Наземный"


transports = [MarineTransport(100000,500000,30), GroundTransport(10000,30000,200),GroundTransport(90000,200000,100), MarineTransport(25000,40000,20)  ]

for unit in transports:
    print(unit.info())