"""
Files.py
Practical 3 CP1404
"""


def main():
    # 1
    name = input('Name: ')
    with open('name.txt', 'w') as file_out:
        print(name, file=file_out)

    # 2
    with open('name.txt', 'r') as file_in:
        print(file_in.readline())

    # 3
    with open('numbers.txt') as file_in:
        first_number = int(file_in.readline())
        second_number = int(file_in.readline())
        print(first_number + second_number)

    # 4
    # Would prefer as a function
    with open('numbers.txt') as file_in:
        lines = file_in.readlines()
        total = 0
        for line in lines:
            total += int(line)
        print(total)


# Function 4
def print_sum_of_file(filename):
    """Read in a file and print the sum of all numbers found"""
    total = 0
    with open(filename) as file_in:
        lines = file_in.readlines()
    for line in lines:
        try:
            total += float(line)
        except TypeError:  # Ignore any line that doesn't cast to a number
            pass
    print(total)


main()
