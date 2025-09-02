import random


def dice(sides):
    dice_1 = random.randint(1, sides)
    return dice_1
sides = int(input("Enter the maximum number of sides: "))
max_number = sides
dices=0
while dices != max_number:
    dices = dice(sides)
    print(dices)

