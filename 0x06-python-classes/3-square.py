#!/usr/bin/python3
"""Class Square that defines a square by:
(based on 2-square)
"""


class Square:
    """ square with private instance attribute size """

    def __init__(self, size=0):
        """ Initialization of square
        Arguments:
            size: size of side of square
        """

        if type(size) is int:
            if size < 0:
                raise ValueError('size must be >= 0')
            else:
                self.__size = size
        else:
            raise TypeError('size must be an integer')

    def area(self):
        """
        Finds the area of square
        Returns:
            The area of the square
        """

        return self.__size ** 2
