# Супер класс
class Car:
    def __init__(self, brand, model, color, year):
        self.brand = brand
        self.model = model
        self.color = color
        self.year = year
        print('Object has been created')

    def start_engine(self):
        print('Engine started')

    def drive(self, distance):
        print(f'Driving {distance} km')


car1 = Car('Toyota', 'Camry', 'red', 2020)

print(car1.color)

car1.start_engine()
car1.drive(100)
# Супер класс "конец"



# Под класс

class ElectricCar(Car):
    def __init__(self, brand, model, color, year, battery_capacity):
        super().__init__(brand, model, color, year)
        self.battery_capacity = battery_capacity

    def charge(self):
        print('Charging the battery')

    def drive(self, distance):
        super().drive(distance)
        self.driving = self.battery_capacity - distance
        print(f'battery used: {self.driving}')

ecar1 = ElectricCar('Set', 'x5', 'wite', 2023, 5000)
ecar1.start_engine()
ecar1.drive(144)
