seasons = ("Winter", "Spring", "Summer", "Autumn")


month = int(input("Enter the number of a month (1-12): "))


if 1 <= month <= 12:
    if month in (12, 1, 2):
        print(f"The season is {seasons[0]}.")
    elif month in (3, 4, 5):
        print(f"The season is {seasons[1]}.")
    elif month in (6, 7, 8):
        print(f"The season is {seasons[2]}.")
    else:
        print(f"The season is {seasons[3]}.")
else:
    print("Invalid month number. Please enter a number between 1 and 12.")
