#!/usr/bin/python3
"""
This module defines a class Rectangle that inherits from BaseGeometry.
It validates the width and height and initializes a rectangle object.
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """rectangle that inherits from BaseGeometry
    """
    def __init__(self, width, height):
              """Initialize the Rectangle with width and height.

        Args:
            width (int): width of the rectangle.
            height (int): height of the rectangle.

        Raises:
            TypeError: if width or height are not integers.
            ValueError: if width or height are <= 0.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
