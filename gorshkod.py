"""
gorshkod.py

Implementation of RegularPolygon class, which is a subclass of Shape

Author: Daniil Gorshkov
"""

from shape import Shape
from math import tan, pi # For area calculation

class RegularPolygon(Shape):
    """
    RegularPolygon class, subclass of Shape
    Represents a regular (equilateral and equiangular) polygon with a given number of sides and side length
    """
    def __init__(self, name, num_sides: int, side_length: float) -> None:
        """
        Initializes RegularPolygon with name, number of sides, and side length
        """
        if num_sides < 3:
            raise ValueError("A polygon must have at least 3 sides")
        if side_length <= 0:
            raise ValueError("Side length must be positive")
        super().__init__(name)
        self.num_sides = num_sides
        self.side_length = side_length
    
    def area(self) -> float:
        """
        Calculates the area of the RegularPolygon using a generalized regular polygon area formula
        """
        return (self.num_sides * self.side_length ** 2) / (4 * tan(pi / self.num_sides))
    
    def perimeter(self) -> float:
        """
        Calculates the perimeter of the RegularPolygon by multiplying the number of sides by the side length
        """
        return self.num_sides * self.side_length
    
    def __str__(self) -> str:
        """
        Returns a string representation of the RegularPolygon
        """
        return f"{super().__str__()} is a regular {self.num_sides}-gon with side length {self.side_length}"
    
    def __eq__(self, other) -> bool:
        """
        Compares the RegularPolygon with another object
        """
        if not isinstance(other, RegularPolygon):
            return False
        return self.num_sides == other.num_sides and self.side_length == other.side_length
    
    