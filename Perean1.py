"""
Author:     Noah Perea
Date:       Feb 6. 2025
Decription: Creating a subclass of the shape class, and practice with github 
"""

from shape import Shape
from math import sqrt

class Diamond(Shape):
    """This is an implementation of a diamond using the shape base class"""

    def __init__(self, name:str, height: int, width:int):
        """Initializes a diamond with height and widtg, as well as calls the parent constructor for name"""
        super.__init__(name)
        self.height = height
        self.width = width

    def area(self) -> float:
        """This function returns the area of a diamond"""
        return (self.height * self.width)/2
    
    def perimeter(self) -> float:
        """This function returns the area of a diamond"""
        return 4 * (sqrt(((self.width/2)**2)+ ((self.height/2)**2)))
    
