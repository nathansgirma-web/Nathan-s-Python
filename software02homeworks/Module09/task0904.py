import random


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
        elif self.current_speed < 0:
            self.current_speed = 0

    def drive(self, hours):
        self.travelled_distance += hours * self.current_speed


def race():
    cars = [Car(f"ABC-{i + 1}", random.randint(100, 200)) for i in range(10)]

    while all(car.travelled_distance < 10000 for car in cars):
        for car in cars:
            car.accelerate(random.randint(-10, 15))

            car.drive(1)

    return sorted(cars, key=lambda c: c.travelled_distance, reverse=True)

race_results = race()
print(f"Race completed! {len(race_results)} cars participated.")
print("Top 3 finishers:")
for i, car in enumerate(race_results[:3]):
    print(f"{i+1}. {car.license_plate}: {car.travelled_distance:.1f} km (speed: {car.current_speed} km/h)")

winner = race_results[0]
print(f"\nWinner: {winner.license_plate} with {winner.travelled_distance:.1f} km!")