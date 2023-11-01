"""A program to keep track of guitars someone owns
Estimated Time: 45mins
Actual Time:
"""

from guitar import Guitar

FILENAME = "guitars.csv"


def main():
    guitars = load_guitars()


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


if __name__ == '__main__':
    main()
