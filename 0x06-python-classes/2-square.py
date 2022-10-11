#!/usr/bin/python3
"""Creates an initialized Class"""


class Square:
    """Square class with __init__"""
    def __init__(self, size=0):
        """initialize an instance of the Square class and validate the size arg
        Args:
            size (int): size of the square
        """
        if type(size) == int:
            if size < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = size
        else:
            raise TypeError("size must be an integer")
