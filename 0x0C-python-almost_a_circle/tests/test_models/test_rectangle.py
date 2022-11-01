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
        self.__width = width

    def get_height(self):
        """height getter"""
        return self.__height

    def set_height(self, height):
        """height setter"""
        self.__height = height

    def get_x(self):
        """x getter"""
        return self.__x

    def set_x(self, x):
        """x setter"""
        self.__x = x

    def get_y(self):
        """y getter"""
        return self.__y

    def set_y(self):
        """y setter"""
        self.__y = y

    width = property(get_width, set_width)
    height = property(get_height, set_height)
    x = property(get_x, set_x)
    y = property(get_y, set_y)
