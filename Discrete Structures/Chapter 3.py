total_money = 15.37

dollar = 0
quaters = 0
dimes = 0
nickels = 0
pennies = 0

while total_money > 0:
    if total_money >= 1:
        dollar += 1
        total_money -= 1
    if total_money >= 0.25:
        quaters += 1
        total_money -= 0.25
    elif total_money >= 0.10:
        dimes += 1
        total_money -= 0.10
    elif total_money >= 0.05:
        nickels += 1
        total_money -= 0.05
    else:
        pennies += 1
        total_money -= 0.01

print('Dollars: ', dollar)
print('Quaters: ', quaters)
print('Dimes: ', dimes)
print('Nickels: ', nickels)
print('Pennies: ', pennies)