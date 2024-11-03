
class Car:
    def __init__(self, name="Car", fuel=0):
        self.name = name
        self.fuel = fuel
        self._odometer = 0

    def add_fuel(self, amount):
        self.fuel += amount

    def drive(self, distance):
        if distance > self.fuel:
            distance_driven = self.fuel
            self.fuel = 0
        else:
            distance_driven = distance
            self.fuel -= distance
        self._odometer += distance_driven
        return distance_driven

    def __str__(self):
        return f"{self.name}, fuel={self.fuel}, odometer={self._odometer}"
