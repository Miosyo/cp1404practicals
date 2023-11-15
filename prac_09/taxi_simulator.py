"""
Taxi simulator
Estimated Time: 20 mins
Actual Time: 35 mins
"""

from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi

MENU = "q)uit, c)hoose taxi, d)rive"


def main():
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    current_taxi = None
    bill_to_date = 0
    print("Let's drive!")
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            current_taxi = choose_taxi(taxis)
        elif choice == "D":
            bill_to_date += drive_taxi(current_taxi)
        else:
            print("Invalid option")
        print(f"Bill to date: ${bill_to_date:.2f}")
        print(MENU)
        choice = input(">>> ").upper()
    print(f"Total trip cost: ${bill_to_date:.2f}")
    print("Taxis are now:")
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")


def choose_taxi(taxis):
    print("Taxis available: ")
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")
    try:
        choice = int(input("Taxi choice: "))
        return taxis[choice]
    except ValueError:
        print("Invalid number")
    except IndexError:
        print("Invalid taxi choice")
    return None


def drive_taxi(taxi):
    if taxi:
        try:
            distance = int(input("Drive how far? "))
            taxi.drive(distance)
            print(f"Your {taxi.name} trip cost you ${taxi.get_fare():.2f}")
            return taxi.get_fare()
        except ValueError:
            print("Invalid number")
    else:
        print("You need to choose a taxi before you can drive")
    return 0


if __name__ == '__main__':
    main()
