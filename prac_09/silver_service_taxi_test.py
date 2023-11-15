"""Silver service taxi tests."""
from prac_09.silver_service_taxi import SilverServiceTaxi


def main():
    test_taxi = SilverServiceTaxi("Test Taxi", 100, 2)
    print(test_taxi)
    test_taxi.drive(18)
    print(test_taxi)
    print(test_taxi.get_fare())

    silver_service_taxi = SilverServiceTaxi("Fancy Taxi", 100, 1.37)
    silver_service_taxi.drive(40)
    print(silver_service_taxi)
    silver_service_taxi.start_fare()
    silver_service_taxi.drive(100)
    print(f"Taxi: {silver_service_taxi}\nCurrent Fare: ${silver_service_taxi.get_fare()}")


if __name__ == '__main__':
    main()
