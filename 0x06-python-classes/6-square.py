#!/usr/bin/python3

""" Creates a class with private instance attribute and validation"""


class Square:
    """ private instance attribute with validation"""
    def __init__(self, size=0, position=(0, 0)):
        if isinstance(size, int):
            if size >= 0:
                self.__size = size
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")
        self.__position = position

    def area(self):
        self.__size *= self.__size
        return self.__size

    def my_print(self):
        if self.__size == 0:
            print()
        else:
            i = 0
            while i < self.__size:
                j = 0
                while j < self.__position[0]:
                    if self.__position[1] > 0:
                        print("_", end="")
                    else:
                        print(" ", end="")
                    j += 1
                j = 0
                while j < self.size:
                    print("#", end="")
                    j += 1
                print()
                i += 1

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if isinstance(value, int):
            if value >= 0:
                self.__size = value
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if isinstance(value, tuple):
            if len(value) == 2:
                self.__position = value
            else:
                raise TypeError("position must be a tuple of 2 positive"
                                "integers")
        else:
            raise TypeError("position must be a tuple of 2 positive"

                            "integers")
