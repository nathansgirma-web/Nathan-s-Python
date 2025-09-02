import random
def dice():
    dice_1 = random.randint(1, 6)
    return dice_1
dices = 0
while dices != 6:
    dices = dice()
    print(dices)



