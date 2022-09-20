calc_art = '''
 _____________________
|  _________________  |
| | NJ           0. | |
| |_________________| |
|  ___ ___ ___   ___  | 
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________|

'''
print(calc_art)
def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def divide(a,b):
    return a/b
def multiply(a,b):
    return a*b

operators = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}
choice = "r"
result = 0
while True:
    if choice == 'r':
        print("--------------------------------------")
        num1 = float(input("enter the 1st number: "))
    elif choice == 'c':
        print(f"your first number is {num1}")
    for i in operators:
        print(i)
    operator = input("pick an operator: ")
    num2 = float(input("enter the 2nd number: "))
    operation = operators[operator]
    result = operation(num1, num2)
    print(f"the result of {num1} {operator} {num2} is {result}")

    choice = input("'c' to continue, 'r' to restart, 'x' to quit: ")
    if choice == 'x':
        break
    elif choice == 'c':
        num1 = result
        print()

