class Vehicle:
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage

# Call Vehicle in Bus in order to inherit (For example: Bus(Vehicle))
class Bus(Vehicle):
    def __init__(self, max_speed, mileage, passengers):
        super().__init__(max_speed, mileage)
        self.passengers = passengers

    def show_info(self):
        print(f'Max speed: {self.max_speed}km/h')
        print(f'Through: {self.mileage}km')
        print(f'Number of passengers: {self.passengers}')

bus1 = Bus(120, 50000, 45)
bus1.show_info()