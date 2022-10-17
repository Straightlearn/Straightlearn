#!/usr/bin/python3
"""Create a Class"""


class Rectangle:
    """A Rectangle class with different private attributes"""

    def __init__(self, width=0, height=0):
        """initialized the class with some private attribute"""
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

    def __str__(self):
        """prints an informal string representation"""
        string = ""
        if self.__width == 0 or self.__height == 0:
            return string

        for h in range(self.__height):
            for w in range(self.width):
                string += "#"
            if h is not self.__height - 1:
                string += "\n"
        return string

    @property
    def width(self):
        """gets the value of the width attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets a new validated value to the width attribute"""
        if type(value) is not int:
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
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def perimeter(self):
        """Gets the perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def area(self):
        """Gets the area of the rectangle"""
        return self.__width * self.__height
