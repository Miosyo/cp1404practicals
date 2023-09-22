for i in range(1, 21, 2):
    print(i, end=' ')
print()

for i in range(0, 101, 10):
    print(i, end=' ')
print()

for i in reversed(range(1, 21)):
    print(i, end=' ')
print()

number_of_stars = int(input('Number of stars: '))
for i in range(0, number_of_stars):
    print('*', end='')
print()

number_of_stars = int(input('Number of stars: '))
for i in range(1, number_of_stars + 1):
    print('*'*i)
print()
