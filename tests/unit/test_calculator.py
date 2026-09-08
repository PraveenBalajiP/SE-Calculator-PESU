"""
Unit Tests for Calculator
Students start with 2 passing tests, then add more
"""
import pytest
from src.calculator import add, divide, multiply, power, sqrt, subtract

class TestBasicOperations:
    """Test basic arithmetic operations"""
    
    def test_add_positive_numbers(self):
        """Test adding positive numbers"""
        assert add(2, 3) == 5
        assert add(10, 15) == 25
    
    def test_subtract_positive_numbers(self):
        """Test subtracting positive numbers"""
        assert subtract(5, 3) == 2
        assert subtract(10, 4) == 6

class TestMultiplyDivideWithValidation:
    """Test multiplication and division with input validation."""
    
    def test_multiply_input_validation(self):
        """Test multiply rejects non-numeric inputs."""
        with pytest.raises(TypeError, match="Both arguments must be numbers"):
            multiply("5", 3)
        with pytest.raises(TypeError, match="Both arguments must be numbers"):
            multiply(5, "3")
    
    def test_divide_input_validation(self):
        """Test divide rejects non-numeric inputs."""
        with pytest.raises(TypeError, match="Division requires numeric inputs"):
            divide("10", 2)

    def test_multiply_positive_numbers(self):
        """Test multiplying positive numbers."""
        assert multiply(2, 3) == 6
        assert multiply(10, 1.5) == 15

    def test_divide_numbers(self):
        """Test dividing numbers."""
        assert divide(6, 3) == 2
        assert divide(5, 2) == 2.5

    def test_divide_by_zero(self):
        """Test division by zero raises an error."""
        with pytest.raises(ValueError, match="Cannot divide .* by zero"):
            divide(10, 0)


class TestPowerAndSquareRoot:
    """Test power and square-root operations."""

    def test_power_numbers(self):
        """Test raising a number to a power."""
        assert power(2, 3) == 8
        assert power(9, 0) == 1

    def test_power_input_validation(self):
        """Test power rejects non-numeric inputs."""
        with pytest.raises(TypeError, match="Power requires numeric inputs"):
            power("2", 3)

    def test_sqrt_numbers(self):
        """Test square roots of non-negative numbers."""
        assert sqrt(9) == 3
        assert sqrt(2) == pytest.approx(2 ** 0.5)

    def test_sqrt_input_validation(self):
        """Test square root rejects invalid inputs."""
        with pytest.raises(TypeError, match="Square root requires a numeric input"):
            sqrt("9")
        with pytest.raises(ValueError, match="negative number"):
            sqrt(-1)