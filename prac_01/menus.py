def print_menu():
    print('(H)ello\n(G)oodbye\n(Q)uit')


name = input('Enter name: ')
print_menu()
choice = input('>>> ').upper()
while choice != 'Q':
    if choice == 'H':
        print(f'Hello {name}')
    elif choice == 'G':
        print(f'Goodbye {name}')
    else:
        print('Invalid choice')
    print_menu()
    choice = input('>>> ').upper()
print('Finished.')
