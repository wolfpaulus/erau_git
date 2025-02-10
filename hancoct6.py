"""Adding Polygon sub-class of Shape
Author: Taylor Hancock
Date:   02/09/2025
Class:  SE320 - Software Construction
Assignment: Extra Credit - Git Pull
"""

from math import dist
from shape import Shape

class Polygon(Shape):
    """
    Class for a generic polygon not described by more specific subclasses
    """
    
    def __init__(self, name: str, vertices: list[tuple]):
        """Create a polygon with a name and a set of vertices
        
        Arguments:
            name (string): name of the given polygon
            vertices (list): list of x-y pair coordinates for each vertex
                              of the polygon, assumed to be in order and
                              ending with the first point
        """

        # initialize with base class
        super().__init__(name)

        # initialize point list
        self.vertices = vertices

    def area(self) -> float:
        """Calculates the area of the polygon
        
        Utilizes Gauss's Area Formula
        A = (1/2)*(y_n * (x_n-1 - x_n+1) + ...)
        """

        # define constants for future use (easier readability)
        X_COMP = 0
        Y_COMP = 1

        total_area = 0
        num_verts = len(self.vertices)

        # calculate based on each position in vertices
        for i in range(num_verts):
            # since [-1] index loops to end, no additional logic is required
            # since [+1] ends up looping past, modulo is needed
            diff = self.vertices[i - 1][X_COMP] - self.vertices[(i + 1) % num_verts][X_COMP]
            total_area += self.vertices[i][Y_COMP] * diff

        # half of output creates final value
        return 0.5 * total_area

    def perimeter(self) -> float:
        """Calculates perimter of the polygon"""

        total_perimeter = 0
        num_verts = len(self.vertices)

        # sum distance between each pair of points
        for i in range(num_verts):
            # since [-1] index loops to end, no additional logic is required
            total_perimeter += dist(self.vertices[i - 1], self.vertices[i])

        return total_perimeter

# testing values
if __name__ == "__main__":
    # create polygons
    triangle = Polygon("Triangle n-gon", [(0, 0), (1, 0), (0, 1)])
    rectangle = Polygon("Rectangle n-gon", [(0, 0), (1, 0), (1, 1), (0, 1)])
    pentagon = Polygon("Pentagon n-gon", [(0, 0), (0, 1), (1, 2), (2, 2), (3, 5)])

    # print values of each polygon
    print(triangle)
    print(rectangle)
    print(pentagon)

    # test added function in shape.py (area_difference())
    print(f"Area difference of triangle and rectangle is: {triangle.area_difference(rectangle)}")
    print(f"Area difference of pentagon and triangle is: {pentagon.area_difference(triangle)}")
