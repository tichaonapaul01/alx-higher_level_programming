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

    @classmethod
    def area(cls):
        """
        Method for calculating the area.

        Raises:
            Exception: This method is not implemented in the base class.
        """
        raise Exception("area() is not implemented")
