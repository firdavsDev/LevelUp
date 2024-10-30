# OOP: Object Oriented Programming
class Car:
    def __init__(self, name, model, year):
        self.name = name
        self.model = model
        self.year = year

    def display(self):
        print(f"{self.name} {self.model} {self.year}")


### OOP: Incapsulation haqida
"""
Incapsulation: Obyektning ichidagi ma'lumotlarni boshqa obyektlardan yashirish
masalan: self.__name = name

"""


class Car:
    def __init__(self, name, model, year):
        self.__name = name
        self.__model = model
        self.__year = year

    def display(self):
        print(f"{self.__name} {self.__model} {self.__year}")


# OOP: Inheritance haqida
class Car:
    def __init__(self, name, model, year):
        self.name = name
        self.model = model
        self.year = year

    def display(self):
        print(f"{self.name} {self.model} {self.year}")


class ElectricCar(Car):
    def __init__(self, name, model, year, battery):
        super().__init__(name, model, year)
        # super() bu super classni chaqirish uchun ishlatiladi
        self.battery = battery

    def display(self):
        print(f"{self.name} {self.model} {self.year} {self.battery}")


car1 = Car("Chevrolet", "Malibu", 2020)
car2 = ElectricCar("Tesla", "Model S", 2020, 100)
car1.display()
car2.display()

# Vorislik olishning uslublari
# 1. issubclass() funksiyasi
print(issubclass(ElectricCar, Car))  # True


class Mexanik:
    def __init__(self, engine):
        self.engine = engine

    def display(self):
        print(f"{self.engine}")


class HybridCar(Car, Mexanik):  # Multiple inheritance

    def __init__(self, name, model, year, battery, engine):
        Car.__init__(self, name, model, year)
        Mexanik.__init__(self, engine)
        self.battery = battery

        # super() ishlatmadik, agar ishlatilsa Car classni chaqiradi
        # MRO (Method Resolution Order) - uslublarini ishlatadi

    def display(self):
        print(f"{self.name} {self.model} {self.year} {self.battery} {self.engine}")


# OOP: Polymorphism haqida
class Car:
    def __init__(self, name, model, year):
        self.name = name
        self.model = model
        self.year = year

    def display(self):
        print(f"{self.name} {self.model} {self.year}")


class ElectricCar(Car):
    def __init__(self, name, model, year, battery):
        super().__init__(name, model, year)
        self.battery = battery

    def display(self):
        print(f"{self.name} {self.model} {self.year} {self.battery}")


def display(car):
    car.display()


car1 = Car("Chevrolet", "Malibu", 2020)
car2 = ElectricCar("Tesla", "Model S", 2020, 100)
display(car1)
display(car2)


# OOP: Abstraction haqida
from abc import ABC, abstractmethod


class Car(ABC):
    def __init__(self, name, model, year):
        self.name = name
        self.model = model
        self.year = year

    @abstractmethod
    def display(self):
        pass


class ElectricCar(Car):
    def __init__(self, name, model, year, battery):
        super().__init__(name, model, year)
        self.battery = battery

    # def display(self):
    #     print(f"{self.name} {self.model} {self.year} {self.battery}")


car1 = Car(
    "Chevrolet", "Malibu", 2020
)  # : Can't instantiate abstract class Car with abstract methods display
car2 = ElectricCar("Tesla", "Model S", 2020, 100)
car1.display()  # TypeError: Can't instantiate abstract class Car with abstract methods display


################### STATIC METHOD & CLASS METHOD ###################

"""
@sataticmethod: Bu method classga bog'liq emas, classdan foydalanish uchun yaratilgan
@classmethod: Bu method classga bog'liq, classdan foydalanish uchun yaratilgan
"""

from datetime import date


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def fromBirthYear(cls, name, year):
        return cls(name, date.today().year - year)

    @staticmethod
    def isAdult(age):
        return age > 18


personl = Person("mayank", 21)
person2 = Person.fromBirthYear("mayank", 1996)
print(person2.age)
print(Person.isAdult(22))
