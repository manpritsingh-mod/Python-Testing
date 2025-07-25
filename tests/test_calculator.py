"""
Test module for Calculator class.
Contains comprehensive tests for all calculator operations.
"""

import pytest
import math
from calculator.calculator import Calculator


class TestCalculator:
    """Test class for Calculator functionality."""
    
    def setup_method(self):
        """Set up test fixtures before each test method."""
        self.calc = Calculator()
    
    def test_addition(self):
        """Test addition operation."""
        assert self.calc.add(2.0, 3.0) == 5.0
        assert self.calc.add(-1.0, 1.0) == 0.0
        assert self.calc.add(0.0, 0.0) == 0.0
        assert self.calc.add(-5.0, -3.0) == -8.0
    
    def test_subtraction(self):
        """Test subtraction operation."""
        assert self.calc.subtract(5.0, 3.0) == 2.0
        assert self.calc.subtract(1.0, 1.0) == 0.0
        assert self.calc.subtract(-1.0, -1.0) == 0.0
        assert self.calc.subtract(0.0, 5.0) == -5.0
    
    def test_multiplication(self):
        """Test multiplication operation."""
        assert self.calc.multiply(2.0, 3.0) == 6.0
        assert self.calc.multiply(-2.0, 3.0) == -6.0
        assert self.calc.multiply(0.0, 5.0) == 0.0
        assert self.calc.multiply(-2.0, -3.0) == 6.0
    
    def test_division(self):
        """Test division operation."""
        assert self.calc.divide(6.0, 2.0) == 3.0
        assert self.calc.divide(5.0, 2.0) == 2.5
        assert self.calc.divide(-6.0, 2.0) == -3.0
        assert self.calc.divide(-6.0, -2.0) == 3.0
    
    def test_division_by_zero(self):
        """Test division by zero raises exception."""
        with pytest.raises(ValueError, match="Division by zero is not allowed"):
            self.calc.divide(5.0, 0.0)
    
    @pytest.mark.parametrize("number,expected", [
        (2, True),
        (4, True),
        (6, True),
        (8, True),
        (10, True),
        (0, True),
        (-2, True),
        (-4, True),
    ])
    def test_even_numbers(self, number, expected):
        """Test even number detection."""
        assert self.calc.is_even(number) == expected
    
    @pytest.mark.parametrize("number,expected", [
        (1, False),
        (3, False),
        (5, False),
        (7, False),
        (9, False),
        (-1, False),
        (-3, False),
        (-5, False),
    ])
    def test_odd_numbers(self, number, expected):
        """Test odd number detection."""
        assert self.calc.is_even(number) == expected
    
    @pytest.mark.parametrize("base,exponent,expected", [
        (2.0, 3, 8.0),
        (3.0, 2, 9.0),
        (5.0, 0, 1.0),
        (2.0, -2, 0.25),
        (10.0, 1, 10.0),
        (-2.0, 3, -8.0),
    ])
    def test_power(self, base, exponent, expected):
        """Test power calculation."""
        assert self.calc.power(base, exponent) == expected
    
    def test_circle_area(self):
        """Test circle area calculation."""
        radius = 5.0
        expected_area = 3.14159 * radius * radius
        assert self.calc.calculate_circle_area(radius) == expected_area
    
    def test_circle_area_zero_radius(self):
        """Test circle area with zero radius."""
        assert self.calc.calculate_circle_area(0.0) == 0.0
    
    @pytest.mark.parametrize("number,expected", [
        (4.0, 2.0),
        (9.0, 3.0),
        (16.0, 4.0),
        (25.0, 5.0),
        (0.0, 0.0),
        (1.0, 1.0),
    ])
    def test_square_root(self, number, expected):
        """Test square root calculation."""
        result = self.calc.square_root(number)
        assert abs(result - expected) < 1e-10
    
    def test_square_root_negative(self):
        """Test square root of negative number raises exception."""
        with pytest.raises(ValueError, match="Cannot calculate square root of negative number"):
            self.calc.square_root(-4.0)
    
    @pytest.mark.parametrize("n,expected", [
        (0, 1),
        (1, 1),
        (2, 2),
        (3, 6),
        (4, 24),
        (5, 120),
    ])
    def test_factorial(self, n, expected):
        """Test factorial calculation."""
        assert self.calc.factorial(n) == expected
    
    def test_factorial_negative(self):
        """Test factorial of negative number raises exception."""
        with pytest.raises(ValueError, match="Factorial is not defined for negative numbers"):
            self.calc.factorial(-1)
    
    def test_get_pi(self):
        """Test getting PI value."""
        assert self.calc.get_pi() == 3.14159