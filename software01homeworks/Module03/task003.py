gender = input("Enter your biological gender (male/female): ").strip().lower()
hemoglobin_value = input("Enter your hemoglobin value (g/l): ")

if hemoglobin_value != int:
    hemoglobin = float(hemoglobin_value)

    if gender == "female":
        if hemoglobin < 117:
            print("Your hemoglobin value is low.")
        elif hemoglobin > 155:
            print("Your hemoglobin value is high.")
        else:
            print("Your hemoglobin value is normal.")

    elif gender == "male":
        if hemoglobin < 134:
            print("Your hemoglobin value is low.")
        elif hemoglobin > 167:
            print("Your hemoglobin value is high.")
        else:
            print("Your hemoglobin value is normal.")
    else:
        print("Invalid gender. Please enter 'male' or 'female'.")
else:
    print("Invalid hemoglobin value. Please enter a number.")