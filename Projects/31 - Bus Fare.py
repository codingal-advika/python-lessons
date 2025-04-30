class Vehicle:
    def __init__(self , seating):
        self.seating = seating
    def fare(self):
        return self.seating * 100
class bus(Vehicle):
    def fare(self):
        total_fare = Vehicle.fare(self)
        maintain = total_fare * 0.10
        return total_fare + maintain
bus = bus(seating = 50)
print(f'The total fare for the bus is : INR {bus.fare()}')
