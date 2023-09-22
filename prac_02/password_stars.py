PASSWORD_MIN_LENGTH = 6

password = input('Please enter a password: ')
while len(password) < PASSWORD_MIN_LENGTH:
    print(f'Password must be a minimum of {PASSWORD_MIN_LENGTH} characters')
    password = input('Please enter a password: ')
print('*' * len(password))
