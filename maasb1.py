"""
Extra Credit: Git practice
Author: Blake Maas
Date: 2/10/25
"""
"""
hexagon subclass of Shape
Note: assumes regular hexagon
"""

from shape import Shape
import math

class hexagon(Shape):
    """
    Concrete class for hexagon
    """

    def __init__(self, name, side):
        """Initialize Hexagon with name and side length"""
        super().__init__(name)
        self.side = side

    def area(self) -> float:
        """Calculate the area of the regular hexagon"""
        return (3 * math.sqrt(3) / 2) * self.side ** 2

    def perimeter(self) -> float:
        """Calculate the perimeter of the hexagon"""
        return 6 * self.side
