from guitar import Guitar


def main():
    print("My guitars!")
    guitars = get_guitars()
    # guitars = [Guitar("Gibson L-5 CES", 1922, 16035.40), Guitar("Line 6 JTV-59", 2010, 1512.9),
    #            Guitar("Ibanez SA Series", 2008, 849.00), Guitar("Fender Stratocaster", 2014, 765.40)]
    print_guitars(guitars)


def get_guitars():
    guitars = []
    guitar_name = input("Name: ")
    while guitar_name != "":
        guitar_year = int(input("Year: "))
        guitar_cost = int(input("Cost: $"))
        guitars.append(Guitar(guitar_name, guitar_year, guitar_cost))
        guitar_name = input("Name: ")
    return guitars


def print_guitars(guitars):
    for i, guitar in enumerate(guitars, 1):
        print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f}"
              f"{' (Vintage)' if guitar.is_vintage() else ''}")


if __name__ == '__main__':
    main()
