from guitar import Guitar


def main():
    gibson = Guitar("Gibson L-5 CES", 1922, 16035.4)
    another_guitar = Guitar("Another Guitar", 1999, 843.22)
    print(f"{gibson.name} get_age() - Expected 101. Got {gibson.get_age()}")
    print(f"{another_guitar.name} get_age() - Expected 24. Got {another_guitar.get_age()}")
    print(f"{gibson.name} is_vintage() - Expected True. Got {gibson.is_vintage()}")
    print(f"{another_guitar.name} is_vintage() - Expected False. Got {another_guitar.is_vintage()}")


if __name__ == '__main__':
    main()
