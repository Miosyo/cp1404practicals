"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

import random


def main():
    score = float(input("Enter score: "))
    print(determine_score(score))
    random_score = random.randint(0, 100)
    print(f'Testing random score of {random_score}, Result: {determine_score(random_score)}')


def determine_score(score):
    if score < 0 or score > 100:
        return 'Invalid score'
    elif score < 50:
        return 'Bad'
    elif score < 90:
        return 'Pass'
    else:
        return 'Excellent'


if __name__ == '__main__':
    main()
