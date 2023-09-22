PASSWORD_MIN_LENGTH = 6


def main():
    password = get_password()
    print_password(password)


def print_password(password):
    print('*' * len(password))


def get_password():
    password = input('Please enter a password: ')
    while len(password) < PASSWORD_MIN_LENGTH:
        print(f'Password must be a minimum of {PASSWORD_MIN_LENGTH} characters')
        password = input('Please enter a password: ')
    return password


if __name__ == '__main__':
    main()
