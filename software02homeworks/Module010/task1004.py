

class Car:
    def __init__(self, license_plate, maximum_speed):
        self.license_plate = license_plate
        self.maximum_speed = maximum_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def accelerate(self, change):
        self.current_speed += change
        if self.current_speed > self.maximum_speed:
            self.current_speed = self.maximum_speed
        if self.current_speed < 0:
            self.current_speed = 0

    def drive(self, hours):
        self.travelled_distance += hours * self.current_speed



class Race:
    def __init__(self, name, distance, cars):
        self.name = name
        self.distance = distance
        self.cars = cars

    def hour_passes(self):
        """Simulate one hour passing in the race."""
        for car in self.cars:
            car.accelerate(random.randint(-10, 15))
            car.drive(1)

    def print_status(self):
        print(f"\n{'Car':<10} {'Max Speed':<12} {'Current Speed':<15} {'Distance (km)':<15}")
        print("-" * 55)
        for car in self.cars:
            print(f"{car.license_plate:<10} {car.maximum_speed:<12} {car.current_speed:<15} {car.travelled_distance:<15.1f}")

    def race_finished(self):
        return any(car.travelled_distance >= self.distance for car in self.cars)

import random

cars = []
for i in range(10):
    car = Car(f"ABC-{i+1}", random.randint(100, 200))
    cars.append(car)

race = Race("Grand Demolition Derby", 8000, cars)
print(f"Race created: {race.name} ({race.distance} km)")
print(f"Cars participating: {len(race.cars)}")

print(f"\nRace finished initially: {race.race_finished()}")

for hour in range(5):
    race.hour_passes()
    if hour == 2:
        print(f"After {hour+1} hours, race finished: {race.race_finished()}")