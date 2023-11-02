"""
Module to define a simple calculator class.
"""

class Calculator:
    """
    A simple calculator class.
    """
    
    def add(self, x, y):
        """
        Add two numbers.

        :param x: The first number.
        :param y: The second number.
        :return: The result of x + y.
        """
        return x + y
    
    def subtract(self, x, y):
        """
        Subtract two numbers.

        :param x: The first number.
        :param y: The second number.
        :return: The result of x - y.
        """
        return x - y
    
    def multiply(self, x, y):
        """
        Multiply two numbers.

        :param x: The first number.
        :param y: The second number.
        :return: The result of x * y.
        """
        return x * y
    
    def divide(self, x, y):
        """
        Divide two numbers.

        :param x: The dividend.
        :param y: The divisor.
        :return: The result of x / y.
        :raises ValueError: If y is 0 (division by zero is not allowed).
        """
        if y == 0:
            raise ValueError("Division by zero is not allowed")
        return x / y
