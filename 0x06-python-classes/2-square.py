#!/usr/bin/python3
"""Class Square that defines a square by:
(based on 1-square.py)
"""


class Square:
    """ square with private instance attribute size """

    def __init__(self, size=0):
        """
        Args:
            size: size of square (must be an integer)
        """

        if type(size) is int:
            if size < 0:
                raise ValueError('size must be >= 0')
            else:
                self.__size = size
        else:
            raise TypeError('size must be an integer')
