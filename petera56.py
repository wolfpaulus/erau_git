"""
Extra Credit Assignment: Git Pull Request
Author: Autumn Peterson
Date: 8 Feb. 2025
Description: Practice with forking a repo and creating a pull request

Disclaimer: I used chatgpt.com to help me with a couple of the steps when correctly
forking a repo
"""

from shape import Shape

class Trapezoid(Shape):
    """A Trapezoid Shape sub-class of Shape"""

    def __init__(self, base1: float, base2:float, side1:float, side2:float, height:float):
        """Initializing a Trapezoid Shape"""

        self.name = "Trapezoid"
        self.base1 = base1
        self.base2 = base2
        self.side1 = side1
        self.side2 = side2
        self.height = height

    def area(self)->float:
        """Area of a Trapezoid"""

        return (self.height*(self.base1 + self.base2))/2

    def perimeter(self)->float:
        """Perimeter of a Trapezoid"""

        return self.base1 + self.base2 + self.side1 + self.side2
    

if __name__ == "__main__":
    t = Trapezoid(12, 6, 5, 5, 4)
    t2 = Trapezoid(12, 6, 5, 5, 4)

    print(t) # printing the new Trapezoid with the __init__() from Shape
    print(t == t2) # showing the __eq__() working from Shape Inheritance
    print(t.get_type()) # getting the class type "Trapezoid"
    