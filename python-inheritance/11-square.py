#!/usr/bin/python3
"""
This module defines a class Square that inherits from Rectangle.
includes validation n implements area calculation n string
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """class Square that inherits from Rectangle"""
    def __init__(self, size):
        """"Instantiation with size
        """
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """area() method"""
        return self.__size ** 2

    def __str__(self):
        """prints square's description"""
        return ("[Square] {}/{}".format(self.__size, self.__size))
