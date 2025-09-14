airports = {}

while True:
    print("\nOptions:")
    print("1 - Enter new airport")
    print("2 - Fetch airport information")
    print("3 - Quit")

    choice = input("Choose an option (1/2/3): ")

    if choice == "1":
        icao = input("Enter ICAO code: ")
        name = input("Enter airport name: ")
        airports[icao] = name
        print(f"Airport '{name}' with ICAO code '{icao}' saved.")

    elif choice == "2":
        icao = input("Enter ICAO code: ")
        if icao in airports:
            print(f"Airport name: {airports[icao]}")
        else:
            print("No airport found with that ICAO code.")

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please enter 1, 2, or 3.")
