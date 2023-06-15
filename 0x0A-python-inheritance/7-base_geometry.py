#!/usr/bin/python3
"""Defines a class BaseGeometry."""


class BaseGeometry:
    """BaseGeometry class.
    """
    def area(self):
        """Area function.

        Raises:
            Exception: if area is not implemented.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates value.

        Args:
            name(str): name of the obj.
            value(int): value of the property.

        Raises:
            TypeError: if value is not an integer.
            ValueError: if value <= 0
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
