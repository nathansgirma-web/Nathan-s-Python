import random

secret_number = random.randint(1, 10)
guess = int(input("Guess a number between 1 and 10: "))

while guess != secret_number:
    if guess < secret_number:
        print("Too low.")
    elif guess > secret_number:
        print("Too high.")
    guess = int(input("Guess again: "))

print("Correct!")
