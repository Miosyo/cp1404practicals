import random

MAX_QUICKPICK_NUMBER = 45
DRAWS_PER_QUICKPICK = 6


def main():
    number_of_quickpicks = int(input("How many quick picks? "))
    for i in range(number_of_quickpicks):
        quickpicks = sorted(random.sample(range(1, MAX_QUICKPICK_NUMBER), DRAWS_PER_QUICKPICK))
        print_quickpicks(quickpicks)


def print_quickpicks(quickpicks):
    for quickpick in quickpicks:
        print(f"{quickpick:3}", end="")
    print()


if __name__ == '__main__':
    main()
