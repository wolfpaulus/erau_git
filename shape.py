"""
Demo Class for Shape
"""

from abc import ABC, abstractmethod


class Shape(ABC):
    """
    Abstract class for Shape
    """

    def __init__(self, name, xCoord, yCoord):
        """Initialize Shape with a name, xCoord, and y Coord"""
        self.name = name
        self.xCoord = xCoord
        self.yCoord = yCoord
        print(f"Creating a {self.__class__.__name__} with name {self.name}, xCoord {self.xCoord}, and yCoord {self.yCoord}!")

    @abstractmethod
    def area(self) -> float:
        """Abstract method for area"""
        pass

    @abstractmethod
    def perimeter(self) -> float:
        """Abstract method for perimeter"""
        pass

    def __str__(self):
        """str representation of the shape"""
        return f"{self.name} with area {self.area()} and perimeter {self.perimeter()}"

    def __eq__(self, other):
        """Check if two shapes are equal
        subclasses could call this and/or improve it
        """
        return self.area() == other.area() and self.perimeter() == other.perimeter()

    def translate(self, xDist, yDist):
        """Method to translate a shape to a different (x,y) coordinate"""
        self.xCoord = self.xCoord + xDist
        self.yCoord = self.yCoord + yDist
