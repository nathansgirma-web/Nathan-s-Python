inch = float(input("Enter length in inches: "))

while inch >= 0:
    cm = inch * 2.54
    print(f"{inch} inches is {cm} centimeters.")
    inch = float(input("Enter length in inches: "))

print("Goodbye!")
