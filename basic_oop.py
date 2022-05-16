from abc import ABC, abstractmethod
import matplotlib.pyplot as plt
import numpy as np

class Vehicle(ABC):
    def startEngine(self):
        print("starting Vehicle...")
    @abstractmethod
    def checkFuel(self):
        pass
    wheels = 2

class Car(Vehicle):
    def __init__(self, name) -> None:
        self.name = name
        print("Object \"%s\"(%s) created"%(self.name, self.__str__()))

    def __del__(self):
        pass
        #print("Object \"%s\" deleted."%self.name)

    def startEngine(self):
        print("starting Car...")

    def checkFuel(self):
        print("Fuel checked !")

    def __gt__(self, other):
        if(self.__weight > other.__weight):
            return True
        else:
            return False

    def getWeight(self):
        return self.__weight
    
    def setWeight(self, nw):
        self.__weight = nw

    # private
    __weight = 100

class Motorbike(Vehicle):
    def __init__(self, name) -> None:
        self.name = name
        print("Object \"%s\"(%s) created"%(self.name, self.__str__()))

    def __del__(self):
        pass

    def checkFuel(self):
        print("Fuel checked !")



myLada = Car('Lada')
myScooter = Motorbike('Yamaha')
myLada.checkFuel()
myLada.startEngine()
myScooter.startEngine()
#del myLada
print(myLada.wheels)

# Make another car and let's add cars
myAudi = Car('Audi')
myAudi.setWeight(50)
if (myLada > myAudi):
    print("Hevy Lada")

