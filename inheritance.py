#mechanism which allows subclass to inherit attributes and methods from superclass
class Vehicle:
    def __init__(self):
        self.colour="white"
    def wheels(self):
        print("2 wheeler and 4 wheeler")
class Car(Vehicle):
    def __init__(self):
        super().__init__()
    def wheels(self):
        super().wheels()
        print("4 wheeler")
car=Car()
car.wheels()
print(car.colour)