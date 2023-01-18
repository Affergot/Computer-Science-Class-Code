import time

OperatorsList = ["AND","OR","XOR"]

num1 = int(input("Enter first number:\n"))
num2 = int(input("Enter second number:\n"))
bin1 = bin(num1)[2:].zfill(8)
bin2 = bin(num2)[2:].zfill(8)

operator = input(f"Enter operator {OperatorsList}:\n").upper()

if operator == "AND":
    result = num1 & num2
elif operator == "OR":
    result = num1 | num2
elif operator == "XOR":
    result = num1 ^ num2
else:
    print("Invalid operator")
    result = None
time.sleep(1)
if result is not None:
    print(f'{num1}: {bin1}')
    print(f'{operator}')
    print(f'{num2}: {bin2}')
    time.sleep(2)
    print("Result in binary:", bin(result)[2:].zfill(8))
    print("Result in decimal:", result)    