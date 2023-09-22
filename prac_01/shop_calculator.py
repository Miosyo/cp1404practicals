DISCOUNT_THRESHOLD = 100
DISCOUNT_MULTIPLIER = 0.9

number_of_items = int(input('Number of items: '))
while number_of_items < 0:
    print('Invalid number of items!')
    number_of_items = int(input('Number of items: '))
total_cost = 0
for i in range(0, number_of_items):
    total_cost += float(input('Price of item: '))
if total_cost >= DISCOUNT_THRESHOLD:
    total_cost *= DISCOUNT_MULTIPLIER
print(f'Total price for {number_of_items} items is ${total_cost:.2f}')
