from abc import ABC, abstractmethod

class Car(ABC):
    @abstractmethod
    def Mileage(self):
        pass

    def Display(self):
        print(f"This is a {self.__class__.__name__}")

class Sedan(Car):
    def Mileage(self):
        return "Sedan: 25 miles per gallon"

class SUV(Car):
    def Mileage(self):
        return "SUV: 20 miles per gallon"

class ElectricCar(Car):
    def Mileage(self):
        return "Electric Car: No fuel consumption (measured in miles per 'charge')"

sedan_car = Sedan()
suv_car = SUV()
electric_car = ElectricCar()

sedan_car.Display()
print(sedan_car.Mileage())

suv_car.Display()
print(suv_car.Mileage())

electric_car.Display()
print(electric_car.Mileage())
