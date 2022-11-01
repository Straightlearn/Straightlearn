#!/usr/bin/python3
"""Rectangle class"""


from models.base import Base


class Rectangle(Base):
    """Rectangle class with inheritance from Base class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """instantiate class"""
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    def get_width(self):
        """width getter"""
        return self.__width

    def set_width(self, width):
        """width setter"""
        if (type(width) is not int):
            raise TypeError("width must be an integer")
        elif (width <= 0):
            raise ValueError("width must be > 0")
        else:
            self.__width = width

    def get_height(self):
        """height getter"""
        return self.__height

    def set_height(self, height):
        """height setter"""
        if (type(height) is not int):
            raise TypeError("height must be an integer")
        elif (height <= 0):
            raise ValueError("height must be > 0")
        else:
            self.__height = height

    def get_x(self):
        """x getter"""
        return self.__x

    def set_x(self, x):
        """x setter"""
        if (type(x) is not int):
            raise TypeError("x must be an integer")
        elif (x < 0):
            raise ValueError("x must be >= 0")
        else:
            self.__x = x

    def get_y(self):
        """y getter"""
        return self.__y

    def set_y(self, y):
        """y setter"""
        if (type(y) is not int):
            raise TypeError("y must be an integer")
        elif (y <= 0):
            raise ValueError("y must be > 0")
        else:
            self.__y = y

    width = property(get_width, set_width)
    height = property(get_height, set_height)
    x = property(get_x, set_x)
    y = property(get_y, set_y)
