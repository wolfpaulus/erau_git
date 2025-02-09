"""
Author: Isaac Jarrells
Email: jarrelli@my.erau.edu
Date: Feb 9, 2025
Purpose: Creation of a shape sub-class.
"""

from shape import Shape

class Rectangle(Shape):
    """Rectangle subclass"""
    def __init__(self, width, height):
        """Initialization of the Rectangle with height and width."""
        super().__init__(width, height)
        self.width = width
        self.height = height

    def area(self) -> float:
        """Area calculation of rectangle"""
        return self.width * self.height

    def perimeter(self) -> int:
        """Perimeter calculation of rectangle"""
        return 2 * self.width + 2 * self.height

