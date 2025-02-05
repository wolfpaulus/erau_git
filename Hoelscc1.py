"""
Git Practice
Alec Hoelscher
2/4/2025

I added an xCoord and yCoord to the shape class to represent the shapes position.
"""

from shape import Shape
from math import pi

class Circle(Shape):
    """A circle shape class"""

    def __init__(self, name: str, xCoord: int, yCoord: int, radius: int):
        """Initialize circle with a given radius"""
        super().__init__(name, xCoord, yCoord)
        self.radius = radius

    def perimeter(self) -> float:
        """Calculate the perimeter of the Circle"""
        return pi * (self.radius ** 2)

    def area(self) -> float:
        """Calculate the area of the Circle"""
        return 2 * pi * self.radius
    