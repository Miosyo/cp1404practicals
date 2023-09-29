"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
When a non-numerical value is entered for user input
2. When will a ZeroDivisionError occur?
When the denominator is zero
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
By ensuring that the denominator input is non-zero
"""


def main():
    """Exceptions demo"""
    try:
        numerator = int(input("Enter the numerator: "))
        denominator = int(input("Enter the denominator: "))
        while denominator == 0:
            print('Denominator cannot be zero(0)')
            denominator = int(input("Enter the denominator: "))
        fraction = numerator / denominator
        print(fraction)
    except ValueError:
        print("Numerator and denominator must be valid numbers!")
    except ZeroDivisionError:
        print("Cannot divide by zero!")
    print("Finished.")


if __name__ == '__main__':
    main()
