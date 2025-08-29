numbers = []

user_input = input("Enter a number (or press Enter to finish): ")

while user_input != "":
    if user_input.replace('.', '', 1).isdigit():
        numbers.append(float(user_input))
    user_input = input("Enter a number (or press Enter to finish): ")

if len(numbers) > 0:
    print(f"Smallest number: {min(numbers)}")
    print(f"Largest number: {max(numbers)}")
else:
    print("No numbers were entered.")
