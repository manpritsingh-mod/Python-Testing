"""
Main application module for the calculator.
This module contains the main function and user interface.
"""

import sys
from calculator.calculator import Calculator


def main():
    """Main function to run the calculator application."""
    calc = Calculator()
    
    print("Simple Calculator")
    print("Available operations: +, -, *, /, ^, sqrt, area, even, factorial, pi")
    print("Type 'quit' to exit")
    
    while True:
        try:
            operation = input("Enter operation: ").strip()
            
            if operation.lower() == 'quit':
                break
                
            process_operation(operation, calc)
            
        except KeyboardInterrupt:
            print("\nCalculator closed.")
            break
        except Exception as e:
            print(f"Error: {e}")


def process_operation(operation, calc):
    """Process the user's operation choice."""
    if operation == "+":
        perform_binary_operation("addition", calc.add)
    elif operation == "-":
        perform_binary_operation("subtraction", calc.subtract)
    elif operation == "*":
        perform_binary_operation("multiplication", calc.multiply)
    elif operation == "/":
        perform_binary_operation("division", calc.divide)
    elif operation == "^":
        perform_power_operation(calc)
    elif operation == "sqrt":
        perform_sqrt_operation(calc)
    elif operation == "area":
        perform_area_operation(calc)
    elif operation == "even":
        perform_even_check(calc)
    elif operation == "factorial":
        perform_factorial_operation(calc)
    elif operation == "pi":
        print(f"PI value: {calc.get_pi()}")
    else:
        print(f"Unknown operation: {operation}")


def perform_binary_operation(operation_name, operation_func):
    """Perform a binary operation (requires two numbers)."""
    try:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        result = operation_func(a, b)
        print(f"Result of {operation_name}: {result}")
    except ValueError as e:
        print(f"Error: {e}")


def perform_power_operation(calc):
    """Perform power operation."""
    try:
        base = float(input("Enter base: "))
        exponent = float(input("Enter exponent: "))
        result = calc.power(base, exponent)
        print(f"Result: {result}")
    except ValueError as e:
        print(f"Error: {e}")


def perform_sqrt_operation(calc):
    """Perform square root operation."""
    try:
        number = float(input("Enter number: "))
        result = calc.square_root(number)
        print(f"Square root: {result}")
    except ValueError as e:
        print(f"Error: {e}")


def perform_area_operation(calc):
    """Perform circle area calculation."""
    try:
        radius = float(input("Enter radius: "))
        area = calc.calculate_circle_area(radius)
        print(f"Circle area: {area}")
    except ValueError as e:
        print(f"Error: {e}")


def perform_even_check(calc):
    """Check if a number is even."""
    try:
        number = int(input("Enter integer: "))
        is_even = calc.is_even(number)
        print(f"{number} is {'even' if is_even else 'odd'}")
    except ValueError as e:
        print(f"Error: {e}")


def perform_factorial_operation(calc):
    """Perform factorial calculation."""
    try:
        number = int(input("Enter non-negative integer: "))
        result = calc.factorial(number)
        print(f"Factorial of {number}: {result}")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()