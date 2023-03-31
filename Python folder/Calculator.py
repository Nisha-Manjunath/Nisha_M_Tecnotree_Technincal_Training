#Calculator using python
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        raise ValueError('Division by zero')
    return x / y

while True:
    # Prompt the user to enter the operation and the operands
    op = input('Enter the operation (+, -, *, /) or "exit" to quit: ')
    if op == 'exit':
        print('App terminated')
        break
    try:
        x = float(input('Enter the first number: '))
        y = float(input('Enter the second number: '))
        # Perform the chosen operation
        if op == '+':
            result = add(x, y)
        elif op == '-':
            result = subtract(x, y)
        elif op == '*':
            result = multiply(x, y)
        elif op == '/':
            result = divide(x, y)
        else:
            raise ValueError(f'Invalid operation: {op}')
        # Print the result
        print(f'{x} {op} {y} = {result}\n')
    except ValueError as e:
        print(f'Error: {e}\n')
