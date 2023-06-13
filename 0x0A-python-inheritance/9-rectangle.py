#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry

"""
===================================
Module with the class Rectangle
===================================
"""


class Rectangle(BaseGeometry):
    """
    Rectangle class that inherits from BaseGeometry.

    Class represents rectangle and inherits functional from BaseGeometry class.
    """

    def __init__(self, width, height):
        """
        Initializes a new Rectangle object.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.

        Raises:
            TypeError: If width or height is not an integer.
            ValueError: If width or height is less than or equal to 0.
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
