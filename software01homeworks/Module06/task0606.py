import math

def pizza_unit_price(diameter_cm, price_eur):
    radius_m = (diameter_cm / 2) / 100
    area_m2 = math.pi * radius_m ** 2
    unit_price = price_eur / area_m2
    return unit_price


diameter1 = float(input("Enter the diameter of pizza 1 (cm): "))
price1 = float(input("Enter the price of pizza 1 (euros): "))

diameter2 = float(input("Enter the diameter of pizza 2 (cm): "))
price2 = float(input("Enter the price of pizza 2 (euros): "))

unit_price1 = pizza_unit_price(diameter1, price1)
unit_price2 = pizza_unit_price(diameter2, price2)

print(f"\nUnit price of pizza 1: €{unit_price1:.2f} per square meter")
print(f"Unit price of pizza 2: €{unit_price2:.2f} per square meter")

if unit_price1 < unit_price2:
    print("Pizza 1 provides better value for money.")
elif unit_price2 < unit_price1:
    print("Pizza 2 provides better value for money.")
else:
    print("Both pizzas have the same unit price.")
