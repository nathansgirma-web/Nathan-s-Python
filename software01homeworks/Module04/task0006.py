import random

points_input = input("How many random points to generate? ")

if points_input.isdigit():
    total_points = int(points_input)
    inside_circle = 0
    count = 0

    while count < total_points:
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)

        if x * x + y * y < 1:
            inside_circle += 1

        count += 1

    pi_approx = 4 * inside_circle / total_points
    print(f"Approximation of pi: {pi_approx}")
else:
    print("Please enter a valid number.")
