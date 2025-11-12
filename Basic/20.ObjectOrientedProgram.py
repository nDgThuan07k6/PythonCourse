class Car:
    # __init__ must include 4_
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def get_info(self):
        return f'{self.make} {self.model} {self.year}'

car1 = Car("Toyota", "Camry", 2020)
car2 = Car("Honda", "Civic", 2022)
car3 = Car("Ford", "Mustang", 2021)

print(car1.get_info())
print(car2.get_info())
print(car3.get_info())