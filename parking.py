import heapdict
from abc import abstractmethod, ABC

class Slot:

    def __init__(self, no) -> None:
        self.no = no
        self.isEmpty = True
        self.vehicle = None
    
    def addCar(self, vehicle):
        self.isEmpty = False
        self.vehicle = vehicle
 
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
        car.getParked(curSlot)
        self.carCount += 1



class Vehicle():
    def __init__(self, number, color) -> None:
        self.number = number
        self.color = color
        self.isParked = False
        self.slot = None
        self.time = 0
    
    def getSlot(self):
        return self.slot.no

    def setTime(self):
        self.time = 1
    
    def getParkerTime(self):
        pass


class Car(Vehicle):

    def __init__(self, number, color) -> None:
        super().__init__(number, color)
    
    def getParked(self, slot):
        self.slot = slot
        self.isParked = True
        print("car got Parked at slot "+ str(self.slot.no))



p1 = Parking(4)
car1 = Car("tn07dc2550", "black")
car2 = Car("tn07dc2550", "black")


p1.parkCar(car1)
p1.parkCar(car2)
print(car2.getSlot())


