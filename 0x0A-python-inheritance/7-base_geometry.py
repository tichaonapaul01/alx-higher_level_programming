#!/usr/bin/python3
"""
===================================
Module with the class BaseGeometry
===================================
"""


class BaseGeometry:
    """
    A base class for geometry-related operations.

    This class provides a foundation for implementing geometry-related functionality.
    """

    def area(self):
        """
        Method for calculating the area.

        Raises:
            Exception: This method is not implemented in the base class.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Method for validating if a number is an integer.

        Args:
            name (str): The name of the value being validated.
            value: The value to be validated.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than or equal to 0.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

