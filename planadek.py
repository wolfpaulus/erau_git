from shape import Shape
from math import sqrt

class Pentagon(Shape):
    """
    Purpose:
        Initialize a pentagon shape with the provided side length.
        We will only be permitting regular pentagons for simplicity of area calculations
    Attributes:
        name(str): name of the pentagon
        side_length(float): The length of the pentagon side.
        sides(list): A list of side lengths.
    """
    def __init__(self, name: str, side_length: float):
        """Initialize a pentagon shape with the provided side length."""
        super().__init__(name)
        self.side_length = side_length
        self.sides = [side_length, side_length, side_length, side_length, side_length]

    def perimeter(self) -> float:
        """Calculates the perimeter of the pentagon."""
        return sum(self.sides)

    def area(self) -> float:
        """Calculates the area of the pentagon. Longer version of area formula to avoid the need for
        centroid calculations."""
        return (sqrt(5 * (5 + 2 * (sqrt(5)))) * self.side_length * self.side_length) / 4

#Creating pentagons
p1 = Pentagon("Pentagon 1", 1.2)
p2 = Pentagon("Pentagon 2", 1.2)
p3 = Pentagon("Pentagon 3", 1.5)

#Printing pentagons
print(p1)
print(p2)
print(p3)

#Equivalence check
print(p1 == p2)
print(p1 == p3)