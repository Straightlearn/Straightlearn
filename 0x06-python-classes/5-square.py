#!/usr/bin/python3
"""Creates an initialized Class"""

class Square:
    """Square class that is initialized and gets the area of a square"""
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

    @property
    def size(self):
        """manipulates the value of the size attribute"""
        return self.__size 
    
    @size.setter
    def size(self, value):
        if type(value) == int:
            if value < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = value
        else:
            raise TypeError("size must be an integer")

    def area(self):
        """gets the area of a square"""
        return self.__size ** 2

    def my_print(self):
        """prints a square using #"""
        if self.__size == 0:
            print()
            return
        for i in range(self.__size):
            for j in range(self.__size):
                print("#", end="")
            print()
