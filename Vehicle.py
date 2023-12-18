from abc import ABC, abstractmethod
class vehicle(ABC):
    @abstractmethod
    def No_of_wheels(self):
        pass
    def start(self):
        pass
    
class bike(vehicle):
    def No_of_wheels(self):
        print("Number of wheels of bike are",2)
    def start(self):
        print("Kick start")
        
class car(vehicle):
    def No_of_wheels(self):
        print("Number of wheels of car are",4)
    def start(self):
        print("Self start")
        
class bus(vehicle):
    def No_of_wheels(self):
        print("Number of wheels of bus are",12)
    def start(self):
        print("Self start")
        
        
bike1=bike()

bike1.No_of_wheels()
bike1.start()
car1=car()
car1.No_of_wheels()
car1.start()
bus1=bus()
bus1.No_of_wheels()
bus1.start()
