year = input("Enter a year: ")

if year != int:
    year = int(year)

    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print(f"{year} is a leap year.")
    else:
        print(f"{year} is not a leap year.")
else:
    print("Invalid input. Please enter a valid year as a number.")