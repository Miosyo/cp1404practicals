"""A program to keep track of guitars someone owns
Estimated Time: 45mins
Actual Time:
"""

from guitar import Guitar

FILENAME = "guitars.csv"


def main():
    guitars = load_guitars()
    print_guitars(guitars)
    get_guitars_from_user(guitars)
    print_guitars(guitars)
    save_guitars(guitars)


def get_guitars_from_user(guitars):
    print("Add another guitar?")
    guitar_name = input("Name: ")
    while guitar_name != "":
        guitar_year = int(input("Year: "))
        guitar_cost = float(input("Cost: $"))
        guitars.append(Guitar(guitar_name, guitar_year, guitar_cost))
        guitar_name = input("Name: ")


def load_guitars():
    guitars = []
    with open(FILENAME, encoding="utf-8") as file_in:
        file_in.readline()
        for line in file_in.readlines():
            # Format: Name,Year,Cost
            parts = line.split(',')
            name = parts[0]
            year = int(parts[1])
            cost = float(parts[2])
            guitars.append(Guitar(name, year, cost))
    return guitars


def save_guitars(guitars):
    with open(FILENAME, 'w', encoding="utf-8") as file_out:
        for guitar in guitars:
            file_out.write(f"{guitar.name},{guitar.year},{guitar.cost}\n")


def print_guitars(guitars):
    guitars.sort(reverse=True)
    print("My guitars:")
    for guitar in guitars:
        print(f"- {guitar}")


if __name__ == '__main__':
    main()
