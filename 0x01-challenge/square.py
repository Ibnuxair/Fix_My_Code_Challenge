#!/usr/bin/python3

"""This module defines a class named  Square."""


class Square():
    """Defines Square."""

    def __init__(self, width):
        """Initializes instances."""
        self.width = width
        self.height = width

    def area_of_my_square(self):
        """ Area of the square """
        return self.width * self.width

    def perimeter_of_my_square(self):
        """ Perimeter of the square """
        return self.width * 4

    def __str__(self):
        """String method"""
        return f"Square with side {self.width}"
    
if __name__ == "__main__":
    s = Square(width=12)
    print(s)
    print("Area:", s.area_of_my_square())
    print("Perimeter:", s.perimeter_of_my_square())
                                                                                                    
