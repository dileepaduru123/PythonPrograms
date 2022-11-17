class ParentFile(object):
    def __init__(self, cars, bikes, bus):
        self.cars = cars
        self.bikes = bikes
        self.bus = bus

    def get_cars(self):
        return self.cars

    def get_bikes(self):
        return self.bikes

    def get_bus(self):
        return self.bus


