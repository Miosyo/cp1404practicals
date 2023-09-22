from prac_02.score import determine_score


# With the structure of score.py importing does not work as intended

def main():
    score = get_valid_score()
    print_menu()
    choice = input('').upper()
    while choice != 'Q':
        if choice == 'G':
            score = get_valid_score()
        elif choice == 'P':
            print_result(score)
        elif choice == 'S':
            print_stars(score)
        else:
            print('Invalid choice')

        print_menu()
        choice = input('').upper()
    print('Farewell')


def print_menu():
    print('(G)et a valid score\n(P)rint result)\n(S)how stars\n(Q)uit')


def get_valid_score():
    score = int(input('Score: '))
    while score > 100 or score < 0:
        print('Invalid score')
        score = int(input('Score: '))
    return score


def print_result(score):
    print(determine_score(score))


def print_stars(score):
    print('*' * score)


if __name__ == '__main__':
    main()
