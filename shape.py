"""
Demo Class for Shape
"""

from abc import ABC, abstractmethod


class Shape(ABC):
    """
    Abstract class for Shape
    """

    def __init__(self, name):
        """Initialize Shape with a name"""
        self.name = name
        print(f"Creating a {self.__class__.__name__} with name {self.name}!")

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
    
    def get_type(self) -> str:
        """
        Returns type of instance as a string
        """
        return self.__class__.__name__

    def __add__(self, other):
        """
        Adds the area of two shapes together.
        """
        return f"{self.name} and {other.name} have a combined area of {self.area() + other.area()}"