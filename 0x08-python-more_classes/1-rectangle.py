#!/usr/bin/python3
"""Create a Class"""


class Rectangle:
    """A Rectangle class with different private attributes"""

    def __init__(self, width=0, height=0):
        """initialized the class with some private attribute
        and validated them
        """
        if type(width) != int:
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = width

        if type(height) != int:
            raise TypeError("height must be an integer")
        elif height < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = height

    @property
    def width(self):
        """gets the value of the width attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets a new validated value to the width attribute"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """gets the value of the height attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets a new validated value to the height attribute"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
