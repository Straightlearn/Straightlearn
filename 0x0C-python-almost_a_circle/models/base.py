#!/usr/bin/python3
"""Base module"""


import unittest


class Base():
    """A Class for our test"""
    __nb_objects = 0

    def __init__(self, id=None):
        """initialize Base for instances"""

        if (id is not None):
            self.id = id
        else:
            Base.__nb_objects = Base.__nb_objects + 1
            self.id = Base.__nb_objects


if __name__ == "__main__":
    unittest.main()
