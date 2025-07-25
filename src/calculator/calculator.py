"""
A simple calculator module with basic arithmetic operations.
This module intentionally contains some pylint violations for testing.
"""

import math


class Calculator:
    """A simple calculator class with basic arithmetic operations."""
    
    # Pylint violation: constant name should be uppercase
    pi_value = 3.14159
    
    def add(self, a, b):
        """Add two numbers."""
        return a + b
    
    def subtract(self, a, b):
        """Subtract second number from first."""
        return a - b
    
    def multiply(self, a, b):
        """Multiply two numbers."""
        return a * b
    
    def divide(self, a, b):
        """Divide first number by second."""
        if b == 0:
            raise ValueError("Division by zero is not allowed")
        return a / b
    
    # Pylint violation: line too long (over 100 characters)
    def calculate_circle_area(self, radius): return self.pi_value * radius * radius  # This line is intentionally too long to trigger pylint violation
    
    # Pylint violation: missing docstring
    def is_even(self, number):
        return number % 2 == 0
    
    def power(self, base, exponent):
        """Calculate power of a number."""
        return base ** exponent
    
    def square_root(self, number):
        """Calculate square root of a number."""
        if number < 0:
            raise ValueError("Cannot calculate square root of negative number")
        return math.sqrt(number)
    
    # Pylint violation: unused variable
    def factorial(self, n):
        """Calculate factorial of a number."""
        if n < 0:
            raise ValueError("Factorial is not defined for negative numbers")
        if n == 0 or n == 1:
            return 1
        
        result = 1
        unused_var = "this will trigger pylint warning"  # Intentional pylint violation
        for i in range(2, n + 1):
            result *= i
        return result
    
    # Pylint violation: method could be a function
    def get_pi(self):
        """Get the value of PI."""
        return self.pi_value