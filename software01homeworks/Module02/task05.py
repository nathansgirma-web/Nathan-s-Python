talents= int(input("Enter a mass in talents: "))
pounds= int(input("Enter a mass in pounds: "))
lots= int(input("Enter a mass in lots: "))
#I converted everything to grams to make it easier.
grams= (talents*8512) + (pounds*425.6) + (lots*13.3)
kilograms= int(grams/1000)
remaining_grams= grams%1000
print(f"The weight in modern units: {kilograms} kilograms and {remaining_grams:.2f} grams")

