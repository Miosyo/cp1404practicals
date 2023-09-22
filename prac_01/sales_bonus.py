"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus
If sales are $1,000 OR over, the bonus is 15%
"""

sales = float(input("Enter sales: $"))

while sales >= 0:
    bonus_percentage = 0.1
    if sales >= 1000:
        bonus_percentage = 0.15
    print(f'Bonus: ${sales * bonus_percentage:.2f}')
    sales = float(input("Enter sales: $"))
