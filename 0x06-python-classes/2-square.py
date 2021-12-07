#!/usr/bin/python3
'''Defines a square'''


class Square:
    ''''Represents Square
    Args:size (int): The size of the new square.
    '''
    def __init__(self, size=0):

        if not isintance(size, int):
            raise TypeError("size must be an integer")

        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
