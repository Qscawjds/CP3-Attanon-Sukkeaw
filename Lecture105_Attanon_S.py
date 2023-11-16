class Vehicle:
    lecenseCode = ""
    serialCode = ""
    def turnOnAirConditioner(self):
        print("Turn On : Air")

class Car(Vehicle):
    def sayHello(self):
        print("Hello World")

class PickUp(Vehicle):
    pass

class Van(Vehicle):
    pass

class EstateCar(Vehicle):
    pass

car = Car()
car.turnOnAirConditioner()
car.sayHello()

pickup = PickUp()
pickup.turnOnAirConditioner()

van = Van()
van.turnOnAirConditioner()

estatecar = EstateCar()
estatecar.turnOnAirConditioner()