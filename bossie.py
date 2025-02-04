"""
Rectangle subclass of Shape
"""

from shape import Shape

class Rectangle(Shape):
    """
    Concrete class for Rectangle
    """

    def __init__(self, name, width, height):
        """Initialize Rectangle with name, width, and height"""
        super().__init__(name)
        self.width = width
        self.height = height

    def area(self) -> float:
        """Calculate the area of the rectangle"""
        return self.width * self.height

    def perimeter(self) -> float:
        """Calculate the perimeter of the rectangle"""
        return 2 * (self.width + self.height)