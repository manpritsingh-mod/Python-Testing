"""
Test module for app module.
Contains tests for the main application functions.
"""

import pytest
from unittest.mock import patch, MagicMock
from calculator.app import process_operation, perform_binary_operation
from calculator.calculator import Calculator


class TestApp:
    """Test class for app functionality."""
    
    def setup_method(self):
        """Set up test fixtures before each test method."""
        self.calc = Calculator()
    
    @patch('builtins.input', side_effect=['5', '3'])
    @patch('builtins.print')
    def test_perform_binary_operation_addition(self, mock_print, mock_input):
        """Test binary operation with addition."""
        perform_binary_operation("addition", self.calc.add)
        mock_print.assert_called_with("Result of addition: 8.0")
    
    @patch('builtins.input', side_effect=['10', '2'])
    @patch('builtins.print')
    def test_perform_binary_operation_division(self, mock_print, mock_input):
        """Test binary operation with division."""
        perform_binary_operation("division", self.calc.divide)
        mock_print.assert_called_with("Result of division: 5.0")
    
    @patch('builtins.input', side_effect=['invalid'])
    @patch('builtins.print')
    def test_perform_binary_operation_invalid_input(self, mock_print, mock_input):
        """Test binary operation with invalid input."""
        perform_binary_operation("addition", self.calc.add)
        # Should print an error message
        assert any("Error:" in str(call) for call in mock_print.call_args_list)
    
    @patch('builtins.print')
    def test_process_operation_pi(self, mock_print):
        """Test processing PI operation."""
        process_operation("pi", self.calc)
        mock_print.assert_called_with("PI value: 3.14159")
    
    @patch('builtins.print')
    def test_process_operation_unknown(self, mock_print):
        """Test processing unknown operation."""
        process_operation("unknown", self.calc)
        mock_print.assert_called_with("Unknown operation: unknown")