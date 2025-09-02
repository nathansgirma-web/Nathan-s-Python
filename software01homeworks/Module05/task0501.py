import random
dice = int(input("How many dice you want to roll? "))
total = 0
for i in range(dice):
    roll = random.randint(1, 6)
    print(f"Die {i + 1} rolled: {roll}")
    total += roll

    print(f"The total is: {total}")