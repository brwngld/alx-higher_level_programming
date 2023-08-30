#!/usr/bin/python3
"""Class Square that defines a square by:
based on a 0-square.py)
"""


class Square:
    """ Represents a square
    Attributes:
        __size (int): size of a side of the square
    """
    def __init__(self, size):
        """Initialization of a square
        Arguements:
            size (int): The size of a side of the square
        Returns: None
        """
        self.__size = size
