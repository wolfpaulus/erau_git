"""
Author: Daniel Stone

Filename: cirlce.py

File Description: Implementation of a circle class, which is a subclass of shape.py 
"""

from shape import Shape
from math import pi

class Circle(Shape):
    """
    Circle class, subclass of Shape
    """
    def __init__(self, name, radius):
        """
        Creates instance of circle with name and radius
        """
        super().__init__(name)
        self.radius = radius

    def area(self) -> float:
        """
        Returns area of Circle instance
        """
        return pi * self.radius ** 2
    
    def perimeter(self) -> float:
        """
        Returns circumference (perimeter) of Circle instance
        """
        return 2 * pi * self.radius
    
    def __str__(self):
        """str representation of the Circle"""
        return f"{self.name} with area {self.area()} and circumference {self.perimeter()}"
    
    def __eq__(self, other):
        """
        Check if two Circles are equal by checking radius.
        """
        return self.radius() == other.radius()
    
