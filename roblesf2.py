"""
Extra Credit
Fjor Robles
"""

from shape import Shape


class Rhombus(Shape):
    """Rhombus class shape"""

    def __init__(self, name: str, p:float, q:float, a:float):
        """Initialize the rhombus and the values needed to calculate the perimeter and area ."""
        super().__init__(name)
        self.p = p
        self.q = q 
        self.a = a

    def perimeter(self) -> float:
        """Calculate the perimeter of the rhombus."""
        # Since the base class does not return, we cannot return
        return self.a * 4

    def area(self) -> float:
        """Calculate the area of the rhombus."""
        return  0.5* self.p * self.q


if __name__ == "__main__":
    r: Rhombus = Rhombus("Rhombi", 3, 4, 5)
    print(r)
