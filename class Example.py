class Vehicle:
    licenseCode = ""
    serialCode = ""
    def turnOnAirCon(self):
        print("Turn on Air Conditioner")

class Car(Vehicle):
    def sayHello(self):
        print("Say Hello")

class Pickup(Vehicle):
    pass
class Van(Vehicle):
    pass
class Estatecar(Vehicle):
    pass

pickup1 = Pickup()
pickup1.turnOnAirCon()

van1 = Van()
van1.turnOnAirCon()

estatecar1 = Estatecar()
estatecar1.turnOnAirCon()

car1 = Car()
car1.turnOnAirCon()
car1.sayHello()