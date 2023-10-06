def main():
    numbers = get_5_numbers()
    print(f"The first number is {numbers[0]}")
    print(f"The last number is {numbers[-1]}")
    print(f"The smallest number is {min(numbers)}")
    print(f"The largest number is {max(numbers)}")
    print(f"The average of the numbers is {sum(numbers) / len(numbers)}")

    usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface',
                 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer',
                 'bob']
    username = input("Login: ")
    if username in usernames:
        print("Access Granted")
    else:
        print("Access Denied")


def get_5_numbers():
    """Gets 5 numbers from the user"""
    numbers = []
    for i in range(5):
        numbers.append(int(input("Number: ")))
    return numbers


if __name__ == '__main__':
    main()
