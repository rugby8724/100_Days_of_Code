
#calculator

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide
}

def calculate(n1, n2, operation):
    calculation_funtion = operations[operation]
    return calculation_funtion(n1, n2)

def calculator():
    more_operations = True
    num1 = None
    while more_operations:
        if num1 == None:
            num1 = float(input('What\'s the first number?  '))
        for symbol in operations:
            print(symbol)
        operation_symbol = input('Pick an operation from the line above ')
        num2 = float(input('What\'s the second number?  '))
        answer = calculate(num1, num2, operation_symbol)
        print(f'{num1} {operation_symbol} {num2} = {answer}')

        countinue_calculator = input(f'Type "y" to countine calculating with {answer} '
                 'type "n" for new caculation or to "e" to exit ')
        if countinue_calculator == 'y':
            num1 = answer
        elif countinue_calculator == 'n':
            calculator()
        else:
            more_operations = False
            break

calculator()
