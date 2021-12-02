from Group.chap_3.app_chassis import Chassis


class Car:
    total_car = 0

    def __init__(self):
        self.model = "Toyota"
        self.make = "Toyota"
        self.speed = 0
        self.chassis = Chassis()
        Car.incrementTotalCars()

    @classmethod
    def incrementTotalCars(cls):
        cls.total_car += 1

    def __str__(self):
        return f"This is a car {self.model} - {self.speed}"

    def accelerate(self, value):
        self.speed += value

    def decelerate(self, value):
        self.speed -= value


car_1 = Car()
ch = Car().chassis.suspension
print(ch)






