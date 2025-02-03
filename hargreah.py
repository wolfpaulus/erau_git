"""
Extra Credit: Git PR Practice
Author: Hayden Hargreaves with aid from GitHub Copilot
Date: 2/2/2025
Description: Practice creating a pull request on GitHub

NOTE: I modified the main shape.py file to include type
hints for the abstract methods that way I could actually
abstract them.
"""

from shape import Shape


class Triangle(Shape):
    """A simple triangle shape class."""

    def __init__(self, name: str, a: float, b: float, c: float):
        """Initialize the triangle with 3 sides."""
        super().__init__(name)
        self.a = a
        self.b = b
        self.c = c

    def perimeter(self) -> float:
        """Calculate the perimeter of the triangle."""
        # Since the base class does not return, we cannot return
        return self.a + self.b + self.c

    def area(self) -> float:
        """Calculate the area of the triangle using Heron's formula."""
        s: float = (self.a + self.b + self.c) // 2
        return (s * (s - self.a) * (s - self.b) * (s - self.c)) ** 0.5


if __name__ == "__main__":
    t: Triangle = Triangle("Jeff", 3, 4, 5)
    print(t)
