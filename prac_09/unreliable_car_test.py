"""
Test file for car class
"""
from prac_09.unreliable_car import UnreliableCar


def main():
    """Test the unreliable car class."""
    # An unreliable car with 100% reliability, should never break down
    old_faithful = UnreliableCar("Old Faithful", 100, 100)
    old_faithful.drive(10)
    old_faithful.drive(10)
    old_faithful.drive(10)
    old_faithful.drive(10)
    old_faithful.drive(10)
    print(old_faithful)

    # An unreliable car with 50% reliability, should break down sometimes
    big_bertha = UnreliableCar("Big Bertha", 100, 50)
    big_bertha.drive(10)
    big_bertha.drive(10)
    big_bertha.drive(10)
    big_bertha.drive(10)
    big_bertha.drive(10)
    print(big_bertha)

    # An unreliable car with 0% reliability, should always break down
    rusty = UnreliableCar("Rusty", 100, 0)
    rusty.drive(10)
    rusty.drive(10)
    rusty.drive(10)
    print(rusty)


if __name__ == '__main__':
    main()
