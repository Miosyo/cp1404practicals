"""
CP1404/CP5632 - Practical
Fill in the TODOs to complete the task
"""


def main():
    """Program to get a valid input"""
    is_finished = False
    while not is_finished:
        try:
            result = int(input("Enter a valid integer: "))
            is_finished = True
        except ValueError:
            print("Please enter a valid integer.")
    print("Valid result is:", result)


if __name__ == '__main__':
    main()
