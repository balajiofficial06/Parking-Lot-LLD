import heapdict
from abc import abstractmethod, ABC
import datetime

class Slot:

    def __init__(self, no) -> None:
        self.no = no
        self.isEmpty = True
        self.vehicle = None
    
    def addCar(self, vehicle):
        self.isEmpty = False
        self.vehicle = vehicle
    
    def empty(self):
        self.isEmpty = False
        self.vehicle = None
 
class ParkingAlgo():
    def __init__(self, slotQunatities) -> None:
        self.h = heapdict.heapdict()
        self.slots = {}
        self.generateSlots(slotQunatities)


    def generateSlots(self, value):
        for i in range(1, value+1):
            st = Slot(i)
            self.h[st] = i
            self.slots[i] = st
    
    def getSlot(self):
        fs = self.h.popitem()
        print(list(self.h.values()))
        return fs[0]


        



class Parking:
    
    def __init__(self, slotValues) -> None:
        self.slotValues = slotValues
        self.algo = ParkingAlgo(slotValues)
        self.carCount = 0
        
    
    def isFull(self) -> bool:
        if self.slotValues == self.carCount:
            return True
        else:
            return False


    def parkCar(self, car):
        curSlot = self.algo.getSlot()
        if self.isFull():
            print("The parking is Full")
        if not curSlot.isEmpty:
            print("assign diffrent slot")
        
        curSlot.addCar(car)
        car.setTime()
        self.carCount += 1
    
    def removeVehicle(self, slotNumber): 
        VehicleSlot = self.algo.slots[slotNumber]
        vehicle = VehicleSlot.vehicle
        VehicleSlot.empty()
        parkedTime = vehicle.getParkedTime()
        cost = vehicle.CalculatePayment(parkedTime)
        print("please pay " + str(cost)+ "rs")
    
        




class Vehicle(ABC):
    def __init__(self, number, color) -> None:
        self.number = number
        self.color = color
        self.isParked = False
        self.time = 0
    

    def setTime(self):
        self.time = 1
    
    def getParkedTime(self):
        return 4 - self.time

    @abstractmethod
    def CalculatePayment(self, hours):
        ...
    




class Car(Vehicle):

    def __init__(self, number, color) -> None:
        super().__init__(number, color)
        self.payment  = CarPayment()
    
    def CalculatePayment(self, hours):
        return self.payment.calculateCost(hours)



class Payment():

    def __init__(self):
        self.totalCost = 0
    
    def calculateCost(self, hours):
        pass

class CarPayment(Payment):
    def __init__(self):
        super().__init__()
    
    def calculateCost(self, hours):
        return hours * 10
    

    



p1 = Parking(4)
car1 = Car("tn07dc2550", "black")
car2 = Car("tn07dc2550", "black")


p1.parkCar(car1)
p1.parkCar(car2)

p1.removeVehicle(1)


