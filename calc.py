# Simple Calculator

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y
    result = SimpleCalculator.multiplication(7, 1)
    assert result == 7

def divide(x, y):
    # If the division is by zero
    if y == 0:
        return "Division by zero."
    return x / y


