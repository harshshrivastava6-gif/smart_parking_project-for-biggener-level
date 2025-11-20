parking = []

def add_vehicle():
    vehicle = input("Enter Vehicle Number: ")
    parking.append(vehicle)
    print("Vehicle Added!")

def remove_vehicle():
    vehicle = input("Enter Vehicle Number to Remove: ")
    if vehicle in parking:
        parking.remove(vehicle)
        print("Vehicle Removed!")
    else:
        print("Vehicle Not Found")

def show_parking():
    print("\n--- Parked Vehicles ---")
    for v in parking:
        print(v)
    print("-------------------------------")

while True:
    print("\n--- Smart Parking System ---")
    print("1. Add Vehicle")
    print("2. Remove Vehicle")
    print("3. Show Parked Vehicles")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        add_vehicle()
    elif choice == 2:
        remove_vehicle()
    elif choice == 3:
        show_parking()
    elif choice == 4:
        break
    else:
        print("Invalid Choice")
        

