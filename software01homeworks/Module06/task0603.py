def gallons_to_liters(gallons):
    return gallons * 3.78541
    # 1 US gallon = 3.78541 liters
while True:
    gallons = float(input("Enter the volume in gallons: "))
    if gallons < 0:
        print("You can't use negative values, Thank you.")
        break
    liters = gallons_to_liters(gallons)
    print(f"{gallons} gallons is equal to {liters:.2f} liters.\n")
