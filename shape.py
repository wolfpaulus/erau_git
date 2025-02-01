"""
Demo Class for Shape
"""
from abc import ABC, abstractmethod


class Shape(ABC):
    """
    Abstract class for Shape
    """

    def __init__(self, name):
        """ Initialize Shape with a name """
        self.name = name
        print(f"Creating a {self.__class__.__name__} with name {self.name}!")

    @abstractmethod
    def area(self):
        """ Abstract method for area """
        pass

    @abstractmethod
    def perimeter(self):
        """ Abstract method for perimeter"""
        pass

    def __str__(self):
        """ str representation of the shape """
        return f"{self.name} with area {self.area()} and perimeter {self.perimeter()}"
