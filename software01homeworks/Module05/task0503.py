user_input = input("Enter a number: ")

if not user_input.isdigit() or int(user_input) < 0:
    print("That's not a valid positive integer.")
else:
    user_input = int(user_input)

    if user_input <= 1:
        print("The number is not a prime number.")
    elif user_input == 2:
        print("The number is a prime number.")
    else:
        prime = True
        for i in range(2, int(user_input ** 0.5) + 1):
            if user_input % i == 0:
                prime = False
                break
        if prime:
            print("The number is a prime number.")
        else:
            print("The number is not a prime number.")
